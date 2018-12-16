# -*- coding: utf-8 -*-
import pymongo
import logging 
import scrapy 
import pandas as pd
import numpy
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

conn=pymongo.MongoClient('127.0.0.1',27017)
db = conn.wwf_database01
myset = db.Zh_user1
myset2 = db.Zh_user2
# followers_list = db.Zh_user

followers_url_list = []
followings_url_list = []

class ZhihuPipeline1(object):
    def process_item(self, item, spider):
        myset.insert({'user_name':item['user_name'],'one_sentence_intro':item['one_sentence_intro'],
    		'user_gender':item['user_gender'],'user_location':item['user_location'],
    		'education_exp':item['education_exp'],'user_major':item['user_major'],
    		'job_exp':item['job_exp'],'brief_intro':item['brief_intro'],
    		'followers_list':item['followers_list'],'followings_list':item['followings_list']})
        # numpy.savetxt('followers_list.txt',followers_url_list)
        return item

class Zhihu_save(object):
    def process_item(self,item,spider):
        followers = pd.DataFrame(list(myset.find()))
        followers = followers['followers_list'][0]
        # numpy.savetxt('followers_list.txt',followers_url_list)
        file = open('followers_list.txt','w')
        for ele in followers:
            file.write(str(ele[1]))
            file.write('\n')
        file.close()

        followings = pd.DataFrame(list(myset.find()))
        followings = followings['followings_list'][0]
        file = open('followings_list.txt','w')
        for ele in followings:
            file.write(str(ele[1]))
            file.write('\n')
        file.close()
        # file = open('followings_list.txt','w')
        # file.write(str(followings_url_list))
class ZhihuPipeline2(object):
    def process_item(self, item, spider):
        # print(item)
        myset2.insert({'user_name':item['user_name'],'one_sentence_intro':item['one_sentence_intro'],
            'user_gender':item['user_gender'],'user_location':item['user_location'],
            'education_exp':item['education_exp'],'user_major':item['user_major'],
            'job_exp':item['job_exp'],'brief_intro':item['brief_intro'],
            'followers_list':item['followers_list'],'followings_list':item['followings_list']})
        # numpy.savetxt('followers_list.txt',followers_url_list)
        return item


    # def extract_followings_url(self,item,spider):
    # 	pass



    	
