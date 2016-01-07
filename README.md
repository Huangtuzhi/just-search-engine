## just-search-engine

In the process of learning Text Retrieval and Search Engines on Coursea, I try to construct a simple search engine.

## 目录结构

```
├── just-search-engine
│   ├── README.md
│   ├── indexer.py    # 索引构建器
│   └── text
│       ├── text-1
│       ├── text-2
│       ├── text-3
│       ├── ...
│       ├── text-n
│       ├── text-result         # 对所有 text 词频统计结果
│       └── text-result-sorted  # 对 text-result 排序的结果
```


## todoList

* <del>在内存上构建索引项</del>
* text-result-sorted 在二级缓存上建立 B+ 树
* 抓取微博数据，对微博数据建立一个搜索应用