#class creating connection to mediasite api
#Last modified: Oct 2016
#By: Dave Bunten

import base64
import json
import ssl
import requests
requests.packages.urllib3.disable_warnings()

class client:
	def __init__(self, serviceroot, sfapikey, username, password):
		self.serviceroot = serviceroot
		self.sfapikey = sfapikey
		self.username = username
		self.password = password

	#formatting for login credentials needed by Mediasite
	def get_basic_auth_header_value(self):
		return_string  = "Basic "+str(base64.b64encode(bytes(self.username+":"+self.password,"utf-8")).decode("utf-8"))
		return return_string

	def do_request(self, request_type, resource, odata_attributes, post_vars):
		self.resource = resource
		self.odata_attributes = odata_attributes
		
		#What we're requesting
		url = self.serviceroot + self.resource + "?" + self.odata_attributes

		# Header values required for request
		values = {
			"sfapikey" : self.sfapikey,
			"Accept":"application/json",
			"Authorization":self.get_basic_auth_header_value()
		}

		try:
			if request_type == "get":
				rsp = requests.get(url, headers=values, verify=False)
				return rsp.text
			elif request_type == "post":
				rsp = requests.post(url, headers=values, json=post_vars, verify=False)
				return rsp.text
			elif request_type == "get stream":
				rsp = requests.get(resource, headers=values, verify=False, stream=True)
				return rsp
			elif request_type == "get job":
				rsp = requests.get(resource, headers=values, verify=False)
				return rsp.text
		except HTTPError as e:
			return e.response.status_code

	
	
	

	
	
	
	
	
	
