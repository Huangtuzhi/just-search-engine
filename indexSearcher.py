#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle
import math
from documentManager import documentManager

class indexSearcher(object):
	
	def __init__(self):
		self.mydb = open('wiki-postings', 'r')
		self.word_dictionary = pickle.load(self.mydb)

	# 计算每个文档的 TF-IDF 值，进行排序
	def caculate_TFIDF(self, word):
		score_dictionary = {}

		if not self.word_dictionary.has_key(word):
			return 0
		
		for posting in self.word_dictionary[word]:
			DocID = posting[0]
			freq = posting[1]

			idf = math.log(float(100) / len(self.word_dictionary[word]))
			tf = 1 + math.log(int(freq)) if freq > 0 else 0
			tfidf_score = tf * idf
			score_dictionary[DocID] = tfidf_score

		score = sorted(score_dictionary.iteritems(), key=lambda d:d[1], reverse = True)
		return score

	def get_wordcount_in_document(self, word, content):
		word_list = content.split(' ')
		cnt = 0
		for one in word_list:
			if one == word:
				cnt += 1
		return cnt

	def DocID2Doc(self, DocID):
		manager = documentManager()
		collection = manager.connect_mongo()
		url = collection.find_one({"DocID": DocID})["url"]
		return url

	# 计算 BM25，设定　ｃ(w,q) 为　１，即查询中每个词出现一次
	def caculate_BM25(self, query_words):
		manager = documentManager()
		collection = manager.connect_mongo()
		
		score_dictionary = {}
		b = 0.5 #参数调节因子
		k = 10 # 调节因子
		avdl = 800 # 文档平均长度

		# query_words 中至少一个单元词出现的所有文档
		DocId_of_query_words = set([])
		for word in query_words.split(' '):

			if not self.word_dictionary.has_key(word):
				continue

			for posting in self.word_dictionary[word]:
				DocID = posting[0]
				DocId_of_query_words.add(DocID)
		
		for id in DocId_of_query_words:
			BM25_score = 0
			for word in query_words.split(' '):
				content = collection.find_one({"DocID": int(id)})["content"]
				freq = self.get_wordcount_in_document(word ,content)
				
				doc_len = len(self.word_dictionary[word])
				idf = math.log(float(100) / doc_len)
				normalizer = 1 - b + b * (doc_len / avdl) 

				BM25_score += (float)((k + 1) * freq) / (freq + k * normalizer) * idf
			# 计算某个文档对　Query 的 BM25 分数 
			score_dictionary[id] = BM25_score

		score = sorted(score_dictionary.iteritems(), key=lambda d:d[1], reverse = True)

		for i in score:
			print self.DocID2Doc(int(i[0]))


	def retrive_word(self, word):
		# 找出 DocID 对应的 url
		manager = documentManager()
		collection = manager.connect_mongo()

		id_list = []
		for word in self.word_dictionary[word]:
			url = collection.find_one({"DocID": int(word[0])})["url"]
			id_list.append(int(word[0]))
		return id_list

	def perform_query(self, query_input):
		id_list = []
		output_num = 5 #返回用户的结果个数
		words = query_input.split(' ')
		
		for word in words:
			self.retrive_word(word)
			score_dict = self.caculate_TFIDF(word)

			count = 0
			for pair in score_dict:
				if count == output_num:
					break
				else:
					count += 1
					id_list.append(pair[0])
		return id_list
				
if __name__ == '__main__':
	searcher = indexSearcher()
	# print searcher.perform_query("literature science")
	searcher.caculate_BM25("literature science")