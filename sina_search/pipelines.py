# encoding=utf-8
import pymongo


class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["sina_search"]
        self.weibo = db["weibo"]

    def process_item(self, item, spider):

            try:

                self.weibo.insert(dict(item))
                print "插入数据" + str(item)
            except BaseException,Argument:
                print Argument
