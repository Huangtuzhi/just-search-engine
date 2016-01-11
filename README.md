## just-search-engine

基于 Wikipedia 网页数据构建文档集，从头开始写的一个全文搜索引擎。

## 目录结构

```
├── just-search-engine
│   ├── documentManager.py # 文档管理器
│   ├── indexer.py         # 索引构建器
│   ├── indexSearcher.py   # 索引检索器
│   ├── README.md          
│   ├── seedbase           # 抓取 WIKI 的 set 对象持久化
│   ├── wiki-postings      # 构建的倒排索引 map 对象持久化
│   ├── text
│   │   └── wiki-result    # 对所有 MongoDB 中的文档统计的结果

```

##依赖

 + pymongo
 + mongodb-server
 + BeautifulSoup
 + pickle
 + requests

## 步骤
* 启动 MongoDB服务器

```
mongod --dbpath =/opt/mongodb-data --logpath=/opt/mongodb-data/mongodb.log
```

* 运行 documentManager.py 构建文档集
* 运行 indexer.py 构建倒排索引
* 运行 indexSearcher.py 进行检索

## 文档排名——计算 TF-IDF

搜索引擎检索出文档之后，需要选择和查询最相关的文档返回给用户，因此需要对文档进行评估。一般有下列方法：

* TF-IDF 词频-逆文档频率
* 余弦相似度
* Okapi BM25

看一下 TF-IDF 的计算

```
def caculate_TFIDF(self, word):
    score_dictionary = {}
    for posting in self.word_dictionary[word]:
        DocID = posting[0]
        freq = posting[1]

        idf = math.log(float(100) / len(self.word_dictionary[word]))
        tf = 1 + math.log(int(freq)) if freq > 0 else 0
        tfidf_score = tf * idf
        score_dictionary[DocID] = tfidf_score
            
    score = sorted(score_dictionary.iteritems(), key=lambda d:d[1], \
    reverse = True)
    print score
```

idf 是文档总数和该词元出现过文档总数的商。TF-IDF 作为衡量“词元在文档集合中是否特殊”的一个指标。

将算得的 TF-IDF 分数存储在字典中，最后按值进行排序。

## 参考

[https://www.coursera.org/course/textretrieval](https://www.coursera.org/course/textretrieval)

[自制搜索引擎](http://book.douban.com/subject/26681675/)

[http://fuzhii.com/2016/01/08/develop-search-engine/](http://fuzhii.com/2016/01/08/develop-search-engine/)


