#!/usr/bin/python
# -*- coding:utf-8 -*-
import string

class Indexer(object):
	
	def __init__(self):
		pass

	# 将每个文档去除标点后，再进行词频统计
	def count_words(self, document, docID):
		result_dict = {}
		delset = string.punctuation

		for line in document:
			line = line.translate(None, delset) #去除标点
			word_array = []
			words = line.split()
			for word in words:
				if not result_dict.has_key(word):
					result_dict[word] = 1
				else:
					result_dict[word] += 1

		file_out = open('text/text-result','a')
	        for key in result_dict.keys():
	    	    file_out.write(key + '\t' + str(docID) + '\t' + str(result_dict[key]) + '\n')
	        file_out.close()

	# 处理所有文档，统计结果 <word, DocID, Freq> 写入到文本中
	def process_all_documents(self):
		for loop in range(1, 5):
			text_name = 'text/text-' + str(loop)
			file_in = open(text_name, 'r')
			self.count_words(file_in, loop)
		file_in.close()

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

if __name__ == '__main__':
	indexer = Indexer()
	# file_in = open('text/text-1','r')
	# indexer.count_words(file_in, 10000)
	# indexer.process_all_documents()
	indexer.sort_index()