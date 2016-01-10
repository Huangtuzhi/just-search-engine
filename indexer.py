#!/usr/bin/python
# -*- coding:utf-8 -*-
import string
import pickle
from documentManager import documentManager

class Indexer(object):
	
	def __init__(self):
		pass

	# 将每个文档去除标点后，再进行词频统计
	def count_words(self, document, docID):
		result_dict = {}
		delset = string.punctuation

		line = str(document)
		line = line.translate(None, delset) #去除标点
		word_array = []
		words = line.split()
		for word in words:
			if not result_dict.has_key(word):
				result_dict[word] = 1
			else:
				result_dict[word] += 1

		file_out = open('text/wiki-result','a')
	        for key in result_dict.keys():
	    	    file_out.write(key + '\t' + str(docID) + '\t' + str(result_dict[key]) + '\n')
	        file_out.close()

	# 处理所有 MongoDB 中的文档，统计结果 <word, DocID, Freq> 写入到文本 wiki-result 中
	def process_all_documents(self):
		manager = documentManager()
		collection = manager.connect_mongo()
		for loop in range(1, 101):
			text = collection.find_one({"DocID": loop})["content"]
			self.count_words(text, loop)

	# 对统计结果 <word, DocID, Freq> 排序
	def sort_index(self):
		index_list = []
		file_in = open('text/text-result','r')
		line = file_in.readline()
		while line:
			index_list.append(line)
			line = file_in.readline()
		file_in.close

		index_list.sort()
		file_out = open('text/text-result-sorted','a')
		for index in index_list:
			file_out.write(index)
		file_out.close()

	# 把文本中的数据构建为内存中的倒排项
	def make_dictionnary(self):
		word_dictionary = {}

		file_in = open('text/wiki-result','r')
		line = file_in.readline()
		while line:
			items = line[:-1].split('\t')
			if not word_dictionary.has_key(items[0]):
				posting = []
				posting.append(items[1])
				posting.append(items[2])
				val = []
				val.append(posting)
				word_dictionary[items[0]] = val
			else:
				posting = []
				posting.append(items[1])
				posting.append(items[2])
				val = word_dictionary[items[0]]
				val.append(posting)
				word_dictionary[items[0]] = val

			line = file_in.readline()
		file_in.close

		# count = 0
		# for (d,x) in word_dictionary.items():
		# 	count += 1
		# 	print "K:" + d + "   " + "V:" + str(x)

		# 	if count == 10:
		# 		break

		# 将 Dic 对象持久化
		mydb = open('wiki-postings', 'w')
		pickle.dump(word_dictionary, mydb)
		

if __name__ == '__main__':
	indexer = Indexer()
	# file_in = open('text/text-1','r')
	# indexer.count_words(file_in, 10000)
	# indexer.process_all_documents()
	# indexer.sort_index()

	# 构建倒排索引
	# indexer.make_dictionnary()	