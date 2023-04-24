import requests
from bs4 import BeautifulSoup
import time

class Revistas(object):
	def __init__(self,host,user,passw):
		self.user = user
		self.passw = passw
		self.host = host
		self.proxy = None
		self.session = requests.session()
		self.csrfToken = ''
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}

	def verify_login(self):
		try:
			url = self.host + 'user/profile'
			resp = self.session.get(url,headers=self.headers,verify=False)
			if resp.url == url:
				print('Login Exito')
				return True
			else:
				print('Login Error')
				return False
		except Exception as ex:
			print(str(ex))
			return False

	def login(self):
		try:
			resp = self.session.get(self.host + 'login',headers=self.headers,verify=False)
			soup = BeautifulSoup(markup=resp.text,features="html.parser")
			self.csrfToken = soup.find("input",attrs={"name":"csrfToken"})['value']
			url_post = self.host + 'login/signIn'
			payload = {}
			payload['csrfToken'] = self.csrfToken
			payload['source'] = ''
			payload['username'] = self.user
			payload['password'] = self.passw
			payload['remember'] = '1'
			resp1 = self.session.post(url_post,data=payload,headers=self.headers,verify=False)
			return self.verify_login()
		except Exception as ex:
			print(str(ex))
			return False