# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_name = scrapy.Field()
    url = scrapy.Field()
    one_sentence_intro = scrapy.Field()
    user_gender = scrapy.Field()
    user_location = scrapy.Field()
    education_exp = scrapy.Field()
    user_major = scrapy.Field()
    job_exp = scrapy.Field()
    brief_intro = scrapy.Field()
    answer_title = scrapy.Field()
    anser_poster = scrapy.Field()
    followers_num = scrapy.Field()
    followers_list = scrapy.Field()
    followings_num = scrapy.Field()
    followings_list = scrapy.Field()
    max_page_followings = scrapy.Field()
    max_page_followers = scrapy.Field()


    
    
