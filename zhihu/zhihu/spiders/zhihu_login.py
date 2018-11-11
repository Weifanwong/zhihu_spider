# -*- coding: utf-8 -*-
import scrapy
import requests
import time
import re

import json

from zhihu.items import ZhihuItem
import time

#name = 'zhihu_login'
#capsion_ticket 与 z_c0是两个会更改的参量

class ZhLoginSpider(scrapy.Spider):
	name = 'zhihu_login'
# #capsion_ticket 与 z_c0是两个会更改的参量


	cookies={
	'_gads':'ID=6e8f432804cef60c:T=1541602740:S=ALNI_MY3N0Qg8ks3k6pe3zHhUKSaAvNCnA',
	'_zap':'0cf72f5d-dc99-40d8-9cca-451a23e81323',
	'_xsrf':'myD3YXkHGE6Qw0z1xdAcvCuuFG1tWNwR',
	'cap_id':'"YzA2NzZjN2RkZTU2NDI5Mzg1YzMwZmFjMWJiNTY0OWY=|1541636683|d368a4221ccbd7745d4f01677b0662e32d78c806"',
	#'capsion_ticket':"2|1:0|10:1541652226|14:capsion_ticket|44:NzcyOWExNWFlYTFjNDk3ZTgyMzU2ODI3MzBhZjJkMjU=|387a0118714705538ea998819ea154cd996c37b9e84ca039e4d746d118385055",
	#'"2|1:0|10:1541642698|14:capsion_ticket|44:NjJkNTg2N2IwZDJjNDI4MGIxMzc4YzgxNGFjMzBhOGE=|01c8fd6861ed3c4b13fb246392066101d35087181f8881710990dad4b73cf2ea"',
	'd_c0':'"ALDnGDCudw6PTuSQ2Y9Ovf2VKEZWLbtizEQ=|1541329785"',
	'l_cap_id':'"ZmM4Y2U3ODEwNDI5NDdmNmFlZDgwYmNjYWNiMDQ0MTc=|1541636683|4369e0e7865af5bdf7d49965ff9755ea6ec3f40f"',
	'l_n_c':'1',
	'n_c':'1',
	'q_c1':'39108a0da0c745718940ad289a5e608f|1541329802000|1541329802000',
	'r_cap_id':'"Mzg2YTIwOGNiOTVjNDY4YjljYWEzNWFiYWIwMDQyZGU=|1541636683|a1696f8a3f3ed4d81de283859a3ac0cf42acb0f5"',
	'tst':'r',
	#'z_c0': '"2|1:0|10:1541652241|4:z_c0|92:Mi4xQ2VDLUJBQUFBQUFBc09jWU1LNTNEaVlBQUFCZ0FsVk5FUTNSWEFCU1FEZXZUTkZ6c2xQUXc3bFFteHZOOWRWMjhB|3140b96820fce9db9f6ac58db04d280429779edd80e9a597800f92a71f3fbf92"',
	#'"2|1:0|10:1541642717|4:z_c0|92:Mi4xQ2VDLUJBQUFBQUFBc09jWU1LNTNEaVlBQUFCZ0FsVk4zZWZRWEFETkwxVW1GUnFWLWEtTXh1UWlOM3F5YjJSYzN3|a887da3e3e4f331eefccdfe64bb8366455e220c216fd74b4970a4249ffee0b83"',
}
# _zap=0cf72f5d-dc99-40d8-9cca-451a23e81323; 
# _xsrf=myD3YXkHGE6Qw0z1xdAcvCuuFG1tWNwR; 
# d_c0="ALDnGDCudw6PTuSQ2Y9Ovf2VKEZWLbtizEQ=|1541329785"; 
# tst=r; 
# q_c1=39108a0da0c745718940ad289a5e608f|1541329802000|1541329802000; 
# __gads=ID=6e8f432804cef60c:T=1541602740:S=ALNI_MY3N0Qg8ks3k6pe3zHhUKSaAvNCnA;
#  l_n_c=1; n_c=1; 
#  l_cap_id="ZmM4Y2U3ODEwNDI5NDdmNmFlZDgwYmNjYWNiMDQ0MTc=|1541636683|4369e0e7865af5bdf7d49965ff9755ea6ec3f40f";
#  r_cap_id="Mzg2YTIwOGNiOTVjNDY4YjljYWEzNWFiYWIwMDQyZGU=|1541636683|a1696f8a3f3ed4d81de283859a3ac0cf42acb0f5"; 
#  cap_id="YzA2NzZjN2RkZTU2NDI5Mzg1YzMwZmFjMWJiNTY0OWY=|1541636683|d368a4221ccbd7745d4f01677b0662e32d78c806"; 
#  capsion_ticket="2|1:0|10:1541652226|14:capsion_ticket|44:NzcyOWExNWFlYTFjNDk3ZTgyMzU2ODI3MzBhZjJkMjU=|387a0118714705538ea998819ea154cd996c37b9e84ca039e4d746d118385055"; 
#  z_c0="2|1:0|10:1541652241|4:z_c0|92:Mi4xQ2VDLUJBQUFBQUFBc09jWU1LNTNEaVlBQUFCZ0FsVk5FUTNSWEFCU1FEZXZUTkZ6c2xQUXc3bFFteHZOOWRWMjhB|3140b96820fce9db9f6ac58db04d280429779edd80e9a597800f92a71f3fbf92"; 
#  tgw_l7_route=860ecf76daf7b83f5a2f2dc22dccf049
	headers = {
#     ':authority': 'www.zhihu.com',
# ':method': 'POST',
# ':path': '/api/v3/oauth/sign_in',
# ':scheme': 'https',
# 'accept': '*/*',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
# 'content-type': 'application/x-www-form-urlencoded',
# 'dnt': '1',
# 'origin': 'https://www.zhihu.com',
# 'referer': 'https://www.zhihu.com/signup?next=%2F',
# 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
#      ':authority': 'www.zhihu.com',
# ':method': 'GET',
# ':path': '/',
# ':scheme': 'https',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
# #'cache-control': 'max-age=0',
#'content-type': 'application/x-www-form-urlencoded',
# 'dnt': '1',
# #'origin': 'https://www.zhihu.com',
# 'upgrade-insecure-requests': '1',
#'referer': 'https://www.zhihu.com/signup?next=%2F',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    
    }
#     HEADERS = {
#     'Host': 'www.zhihu.com',
#     'Referer': 'https://www.zhihu.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }

	def start_requests(self):
		self.flag = 0
		#url = 'https://www.zhihu.com/'
		url = 'https://www.zhihu.com/people/fei-ming-39-77/activities'
		url = 'https://www.zhihu.com/people/supergo/activities'
		#url = 'https://www.zhihu.com/people/lishangyuan/activities'
		# url = 'https://www.zhihu.com/people/ggg-ah/activities'
		#url = 'https://www.zhihu.com/people/li-shuai-mai-mai-ti/activities'
	# 	formdata = {
	# #'ToOk0KPwMtBtNXtzltBlMKpxBduq0PQzppOk0KPwMtBtNX0x1hBlMK6z8p9a01AzwLAlMK-pRsNa0oslkgrhcLolMsabR58lvkNkbHolMsabIgNkggslPGohbhbbMsapks8k0KKlSwNdMkNojs8k0K5jMwN3Ps8k1gslPGoh-lbbMs7kjs8k0Cc2I0AtKXd2k-BzDH5kPgbfbhrljsapPK5k0orbbhrljsakKG5oPsNa0cOkkgrhMGolMsavU0Q1A2uzDH5kPgbfa2rljsapNKpwClurKdQwngrhLGKkOsNbBTuwodRxI6P2clbf9hRzmlR1609lMsaaLcrklorlNG_mLwr_ahrljsapNKpxHdQtMtQ1kx8k0K5xMseu6lbl20rxMK_xOoeaTwemloukT9Kw8-b_Qcbl_c8xROKkMsu4Nsqxjtf262PxDlRbMs7w12BjPdtyCDRdHXQwXlrh0D01PXAqQgrhj9blSComTkNbLorlgoOk09sz6pBq0Puylx8k0O01J2BqNde1Xlrh00s3OXtrIdA13x8k095k0-NbLkrxgcAl0-owNgu_Albl-crwQWKwRwev8lNwXlrh9-PvOTevDLQw: '
	# }
		yield scrapy.Request(url,cookies=self.cookies,headers = self.headers,callback = self.parse)
		#resp = requests.get(url,headers=self.headers,cookies=self.cookies)
		#print(resp.text)
	def parse(self,response):

		#global followers_list
		item = ZhihuItem()
		user_name = response.xpath('//span[@class="ProfileHeader-name"]/text()').extract()
		one_sentence_intro = response.xpath('//span[@class="RichText ztext ProfileHeader-headline"]/text()').extract()
		
		#包含个人信息的部分
		intro_detail = response.xpath('//script[@id="js-initialData"]/text()').extract()[0]
		res_str1 = r'"initialState":{"common":{"ask":{}}(.*?)}},"questions":'
		intro_use = re.findall(res_str1,intro_detail)
		intro_use = intro_use[0]

		#gender
		res_str2 = r'"gender":.+'
		gender_str = re.findall(res_str2,intro_use)[0]
		gender_num = int(gender_str.replace('"gender":',''))
		if gender_num == 1:
			gender = '男'
		elif gender_num == 0:
			gender = '女'
		else:
			gender = ''

		#one_sentence_intro
		res_str3 = r'"headline":"(.*?)","urlToken"'
		one_sentence_intro = re.findall(res_str3,intro_use)[0]
		
		#user_location
		res_str4_1 = r'"locations":(.*?)","url":"'
		location_str = re.findall(res_str4_1,intro_use)
		if len(location_str) ==0:
			location = ''
		else:
			res_str4_2 = r'","name":".+'
			location_str = re.findall(res_str4_2,location_str[0])[0]
			location = location_str.replace('","name":"','')

		#user_job 
		res_str4_1 = r'"business":(.*?)","url":'
		business_str = re.findall(res_str4_1,intro_use)
		if len(business_str) == 0:
			business = ''
		else:
			res_str4_2 = r'","name":".+'
			business_str = re.findall(res_str4_2,business_str[0])[0]
			business = business_str.replace('","name":"','')

		#school&college
		res_str4_1 = r'"school":(.*?)","url":'
		education_str = re.findall(res_str4_1,intro_use)
		if len(education_str) == 0:
			education = ''
		elif len(education_str) ==1:
			res_str4_2 = r'","name":".+'
			education_str = re.findall(res_str4_2,education_str[0])[0]
			education = education_str.replace('","name":"','')
		else:
			education = []
			for i in range(len(education_str)):
				res_str4_2 = r'","name":".+'
				tmp = re.findall(res_str4_2,education_str[i])[0]
				tmp = tmp.replace('","name":"','')
				education.append(tmp)
		#major

		res_str4_1 = r'"major":(.*?)","url":'
		major_str = re.findall(res_str4_1,intro_use)
		if len(major_str) == 0:
			major = ''
		else:
			res_str4_2 = r'","name":".+'
			major_str = re.findall(res_str4_2,major_str[0])[0]
			major = major_str.replace('","name":"','')

		#brief_introduction
		res_str4_1 = r'"description":"(.*?)","'
		brief_intro_str = re.findall(res_str4_1,intro_use)
		if len(brief_intro_str) == 0:
			brief_intro = ''
		else:
			brief_intro = brief_intro_str[0]
		# print(response.text)
		# print(brief_intro)

		
		#followers
		# https://www.zhihu.com/people/xingzhe8848/activities
		base_url = 'https://www.zhihu.com'
		followers_url = response.xpath('//a[@class="Button NumberBoard-item Button--plain"]/@href').extract()[1]
		followings_url = response.xpath('//a[@class="Button NumberBoard-item Button--plain"]/@href').extract()[0]
		followers_url = base_url + followers_url 
		followings_url = base_url + followings_url
		# followings_url = self.url.replace('activities','followings')
		# followers_url = self.url.replace('activities','followers')


		#followers_num & followings_num
		followings_num = response.xpath('//strong[@class="NumberBoard-itemValue"]/text()').extract()[0]
		followers_num = response.xpath('//strong[@class="NumberBoard-itemValue"]/text()').extract()[1]


		item['user_name'] = user_name[0]
		item['one_sentence_intro'] = one_sentence_intro
		item['user_gender'] = gender 
		item['user_location'] = location
		item['education_exp'] = education
		item['user_major'] = major
		item['job_exp'] = business
		item['brief_intro'] = brief_intro
		item['followers_list'] = []
		item['followings_list'] = []
		item['followers_num'] = followers_num
		item['followings_num'] = followings_num
		 

		#获得粉丝的最大页码
		max_page_followers = int(int(followers_num)/20) + 1

		item['max_page_followers'] = max_page_followers

		base_url = followers_url + '?page='
		for page in range(1,max_page_followers + 1):
		# for page in range(1,2):
			
			followers_url = base_url + str(page)
			yield scrapy.Request(followers_url,cookies=self.cookies,headers = self.headers,meta={'ikey':item,'page':page,'followers_url':followers_url,'followings_url':followings_url},callback = self.followers_list_p,dont_filter=True)

		#print(item)
		#yield scrapy.Request('https://www.zhihu.com',cookies=self.cookies,headers = self.headers,callback = self.test)


	# def followers_list_p(self,response):

	# 	item = response.meta['ikey']
	# 	followers_script = response.xpath('//script[@id="js-initialData"]/text()').extract()
	# 	# time.sleep(5)
	# 	res_str1 = r'"initialState":(.*?)"followingColumnsByUser"'
	# 	followers_detail = re.findall(res_str1,followers_script[0])[0]

	# 	res_str2 = r'"name":"(.*?)","url"'
	# 	res_str3 = r'"name":".+'
	# 	followers_name = re.findall(res_str2,followers_detail)

	# 	if followers_name == []:
	# 		#print(response.text)
	# 		lost_page = response.meta['page']
	# 		yield scrapy.Request(response.url,cookies=self.cookies,headers = self.headers,meta={'ikey':item,'page':lost_page,'followers_url':response.meta['followers_url'],'followings_url':response.meta['followings_url']},callback = self.followers_list_p,dont_filter=True)
		


		
	# 	item['followers_list'].extend(followers_name)

	# 	if len(item['followers_list']) > (item['max_page_followers'] - 1) * 20:  #当粉丝读取完毕
	# 		max_page_followings = int(int(item['followings_num'])/20) + 1
	# 		item['max_page_followings'] = max_page_followings
	# 		base_url = response.meta['followings_url'] + '?page='
	# 		for page in range(1,max_page_followings + 1):  
	# 			followings_url = base_url + str(page)
	# 			yield scrapy.Request(followings_url,cookies=self.cookies,headers = self.headers,meta={'ikey':item,'followings_url':followings_url,'page':page},callback = self.followings_list_p,dont_filter=True)

	def followers_list_p(self,response):
		#time.sleep(2)
		item = response.meta['ikey']
		followers_script = response.xpath('//script[@id="js-initialData"]/text()').extract()
		# time.sleep(5)
		res_str1 = r'"initialState":(.*?)"followingColumnsByUser"'
		followers_detail = re.findall(res_str1,followers_script[0])[0]

		res_str2 = r'","urlToken(.*?)","url":"'
		res_str3 = r'"name":".+'
		res_str4 = r'":"(.*?)","id":"'
		followers_info = re.findall(res_str2,followers_detail)

		# if len(followers_info) < 2 and followers_info != [] :
		if followers_info == [] or len(followers_info) == 1:
			#print(response.text)
			lost_page = response.meta['page']
			yield scrapy.Request(response.url,cookies=self.cookies,headers = self.headers,meta={'ikey':item,'page':lost_page,'followers_url':response.meta['followers_url'],'followings_url':response.meta['followings_url']},callback = self.followers_list_p,dont_filter=True)
		
		#找到粉丝的昵称与url
		base_url = 'https://www.zhihu.com/people/'
		for ele in followers_info:
			if len(ele) < 200:
				ele_name = re.findall(res_str3,ele)[0]
				ele_name = ele_name.replace('"name":"','')
				ele_url = base_url + re.findall(res_str4,ele)[0]
				item['followers_list'].extend([[ele_name,ele_url]])
			else:
				continue
			# item['followers_list']['followers_url'].extend(ele_url)

		if len(item['followers_list']) > (item['max_page_followers'] - 1) * 20:  #当粉丝读取完毕
			max_page_followings = int(int(item['followings_num'])/20) + 1
			item['max_page_followings'] = max_page_followings
			base_url = response.meta['followings_url'] + '?page='
			for page in range(1,max_page_followings + 1):  
				followings_url = base_url + str(page)
				yield scrapy.Request(followings_url,cookies=self.cookies,headers = self.headers,meta={'ikey':item,'followings_url':followings_url,'page':page},callback = self.followings_list_p,dont_filter=True)



	def followings_list_p(self,response):

		item = response.meta['ikey']
		followings_script = response.xpath('//script[@id="js-initialData"]/text()').extract()
		# time.sleep(5)
		res_str1 = r'"initialState":(.*?)"unlockTicketStatus"'
		followings_detail = re.findall(res_str1,followings_script[0])[0]
		# print(followings_detail)

		res_str2 = r'","urlToken(.*?)","url":"'
		res_str3 = r'"name":".+'
		res_str4 = r'":"(.*?)","id":"'
		followings_info = re.findall(res_str2,followings_detail)

		res_str5 = r'"headline":".+'
		res_str6 = r'","urlToken":"(.*?)","id":"'
#or len(followings_info) < 20
		if followings_info == [] or len(followings_info) <7:
			lost_page = response.meta['page']
			yield scrapy.Request(response.url,cookies=self.cookies,headers = self.headers,meta={'ikey':item,'page':lost_page,'followings_url':response.meta['followings_url']},callback = self.followings_list_p,dont_filter=True)
		#这里的dont filter特别重要，因为scrapy会自动过滤重复请求！
		
		#找到关注用户的昵称与url
		base_url = 'https://www.zhihu.com/people/'
		# if len(followings_info) < 7:
		# 	print(followings_info)

		for ele in followings_info:
			if len(ele) > 300:
				tmp = re.findall(res_str5,ele)
				if len(tmp) == 0:
					continue
				else:
				#print(tmp)
					ele_name = re.findall(res_str3,tmp[0])[0]
					ele_name = ele_name.replace('"name":"','')
					ele_url = base_url + re.findall(res_str6,tmp[0])[0]
					item['followings_list'].extend([[ele_name,ele_url]])
				#print(123)
			else:

				ele_name = re.findall(res_str3,ele)[0]
				ele_name = ele_name.replace('"name":"','')
				ele_url = base_url + re.findall(res_str4,ele)[0]
				item['followings_list'].extend([[ele_name,ele_url]])



		if len(item['followings_list']) > (item['max_page_followings'] - 1) * 20:
			print(item)
			yield item

	def second_parse(self,response):

			user_name = response.xpath('//span[@class="ProfileHeader-name"]/text()').extract()
			one_sentence_intro = response.xpath('//span[@class="RichText ztext ProfileHeader-headline"]/text()').extract()
			
			#包含个人信息的部分
			intro_detail = response.xpath('//script[@id="js-initialData"]/text()').extract()[0]
			res_str1 = r'"initialState":{"common":{"ask":{}}(.*?)}},"questions":'
			intro_use = re.findall(res_str1,intro_detail)
			intro_use = intro_use[0]

			#gender
			res_str2 = r'"gender":.+'
			gender_str = re.findall(res_str2,intro_use)[0]
			gender_num = int(gender_str.replace('"gender":',''))
			if gender_num == 1:
				gender = '男'
			elif gender_num == 0:
				gender = '女'
			else:
				gender = ''

			#one_sentence_intro
			res_str3 = r'"headline":"(.*?)","urlToken"'
			one_sentence_intro = re.findall(res_str3,intro_use)[0]
			
			#user_location
			res_str4_1 = r'"locations":(.*?)","url":"'
			location_str = re.findall(res_str4_1,intro_use)
			if len(location_str) ==0:
				location = ''
			else:
				res_str4_2 = r'","name":".+'
				location_str = re.findall(res_str4_2,location_str[0])[0]
				location = location_str.replace('","name":"','')

			#user_job 
			res_str4_1 = r'"business":(.*?)","url":'
			business_str = re.findall(res_str4_1,intro_use)
			if len(business_str) == 0:
				business = ''
			else:
				res_str4_2 = r'","name":".+'
				business_str = re.findall(res_str4_2,business_str[0])[0]
				business = business_str.replace('","name":"','')

			#school&college
			res_str4_1 = r'"school":(.*?)","url":'
			education_str = re.findall(res_str4_1,intro_use)
			if len(education_str) == 0:
				education = ''
			elif len(education_str) ==1:
				res_str4_2 = r'","name":".+'
				education_str = re.findall(res_str4_2,education_str[0])[0]
				education = education_str.replace('","name":"','')
			else:
				education = []
				for i in range(len(education_str)):
					res_str4_2 = r'","name":".+'
					tmp = re.findall(res_str4_2,education_str[i])[0]
					tmp = tmp.replace('","name":"','')
					education.append(tmp)
			#major

			res_str4_1 = r'"major":(.*?)","url":'
			major_str = re.findall(res_str4_1,intro_use)
			if len(major_str) == 0:
				major = ''
			else:
				res_str4_2 = r'","name":".+'
				major_str = re.findall(res_str4_2,major_str[0])[0]
				major = major_str.replace('","name":"','')

			#brief_introduction
			res_str4_1 = r'"description":"(.*?)","'
			brief_intro_str = re.findall(res_str4_1,intro_use)
			if len(brief_intro_str) == 0:
				brief_intro = ''
			else:
				brief_intro = brief_intro_str[0]

