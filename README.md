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

## 参考

[https://www.coursera.org/course/textretrieval](https://www.coursera.org/course/textretrieval)

[自制搜索引擎](http://book.douban.com/subject/26681675/)

[http://fuzhii.com/2016/01/08/develop-search-engine/](http://fuzhii.com/2016/01/08/develop-search-engine/)


