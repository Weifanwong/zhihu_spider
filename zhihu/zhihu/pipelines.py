# -*- coding: utf-8 -*-
import pymongo
import logging 
import scrapy 


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

conn=pymongo.MongoClient('127.0.0.1',27017)
db = conn.wwf_database01
myset = db.Zh_user
# followers_list = db.Zh_user


class ZhihuPipeline(object):
    def process_item(self, item, spider):
    	myset.insert({'user_name':item['user_name'],'one_sentence_intro':item['one_sentence_intro'],
    		'user_gender':item['user_gender'],'user_location':item['user_location'],
    		'education_exp':item['education_exp'],'user_major':item['user_major'],
    		'job_exp':item['job_exp'],'brief_intro':item['brief_intro'],
    		'followers_list':item['followers_list'],'followings_list':item['followings_list']})
    	return item

    # def extract_followings_url(self,item,spider):
    # 	pass



    	
