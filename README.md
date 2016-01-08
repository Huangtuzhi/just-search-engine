## just-search-engine

In the process of learning Text Retrieval and Search Engines on Coursea, try to develop a simple search engine.

## 目录结构

```
├── just-search-engine
│   ├── documentManager.py # 文档管理器
│   ├── indexer.py         # 索引构建器
│   ├── README.md          
│   ├── seedbase           # 抓取 WIKI 的 set 对象持久化
│   ├── wiki-postings      # 构建的倒排索引 map 对象持久化
│   ├── text
│   │   ├── text-1
│   │   ├── text-2
│   │   ├── text-3
│   │   ├── text-4
│   │   ├── text-result
│   │   ├── text-result-sorted
│   │   └── wiki-result   # 对所有 MongoDB 中的文档统计的结果

```

##依赖

 + pymongo
 + mongodb-server
 + BeautifulSoup
 + pickle
 + requests

## todoList

* <del>在内存上构建索引项</del>
* <del>map 对象持久化，使用 pickle 来序列化</del>
* <del>抓取的 WIKI 数据存放在 MongoDB 中</del>
* <del>博客整理</del>

## 遇到的问题
* 新浪微博的登录方式
* 异步加载的网页如何爬取内容？微博内容不好爬，换成今日头条

## 步骤
* 启动 MongoDB服务器

```
mongod --dbpath =/opt/mongodb-data --logpath=/opt/mongodb-data/mongodb.log
```

## 参考

[https://www.coursera.org/course/textretrieval](https://www.coursera.org/course/textretrieval)

[自制搜索引擎](http://book.douban.com/subject/26681675/)


