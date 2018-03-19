#!/usr/bin/env python3

import requests
import json

node_url = 'http://10.102.180.160:8091/NorthStar/API/v1/tenant/1/topology/1/nodes'
url = 'http://10.102.180.160:8091/NorthStar/API/v2/tenant/1/topology/1/te-lsps'
url_maint = 'http://10.102.180.160:8091/NorthStar/API/v2/tenant/1/topology/1/maintenances'
headers = {'Authorization':'Bearer r2xvTYKhYTgkar1x7y4fKy17daTOpw8o/LVHAxXFBVk=','Accept' : 'application/json', 'Content-Type' : 'application/json'}



def move_traffic():
    contents = open('new_path.json', 'rb').read()
    print(contents)
    r = requests.post(url, data=contents, headers=headers, verify=False)
    #print(r)

def move_traffic_back():
    contents = open('original_path.json', 'rb').read()
    print(contents)
    r = requests.post(url, data=contents, headers=headers, verify=False)

def get_node():
    r = requests.get(node_url, headers=headers,verify=False)
    #pprint r.json()
    #result = r.json()
    #with open('data.txt', 'w') as outfile:
    #  json.dump(result, outfile)
    return(r)

def create_node_maintenance(payload):
    #contents = open('node_maintenance.json', 'rb').read()
    print(payload)
    r = requests.post(url_maint, data=payload, headers=headers, verify=False)
