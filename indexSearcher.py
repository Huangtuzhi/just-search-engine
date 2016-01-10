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
		for posting in self.word_dictionary[word]:
			DocID = posting[0]
			freq = posting[1]

			idf = math.log(float(100) / len(self.word_dictionary[word]))
			tf = 1 + math.log(int(freq)) if freq > 0 else 0
			tfidf_score = tf * idf
			score_dictionary[DocID] = tfidf_score

		score = sorted(score_dictionary.iteritems(), key=lambda d:d[1], reverse = True)
		return score

	# 计算 BM25
	def caculate_BM25(self, word):
		pass

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
	# 进行搜索  
	# print searcher.retrive_word('good')
	print searcher.perform_query("literature science")	