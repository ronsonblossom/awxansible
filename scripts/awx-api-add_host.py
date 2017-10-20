#!/bin/python
#Author: Ronson Blossom

import requests
import json
import commands
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_token():
    token_url = "https://10.0.2.6/api/v2/authtoken/"
    token_payload = "{\"username\": \"admin\", \"password\": \"Welcome@12345\"}"
    token_headers = {'content-type': "application/json",}

    response = requests.request("POST", token_url, data=token_payload, headers=token_headers, verify=False).json()
    awx_token = response['token']
    return(awx_token)

def get_local_ip():
	intf = 'eth0'
	intf_ip = commands.getoutput("ip address show dev " + intf).split()
	intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]
	return(intf_ip)

def add_host():
        url = "https://10.0.2.6/api/v2/hosts/"
	payload = "{\r\n    \"name\": \"get_local_ip()\",\r\n    \"description\": \"api added\",\r\n    \"inventory\": \"2\",\r\n    \"enabled\": true,\r\n    \"instance_id\": \"\",\r\n    \"variables\": \"\"\r\n}"
        headers = {
        'content-type': "application/json",
        'authorization': "token "+get_token(),
        }

        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
	add_host_result = response.json()
        add_host_status = response.status_code

	print add_host_result
	print add_host_status

add_host()

