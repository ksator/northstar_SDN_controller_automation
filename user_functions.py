import json
from pprint import pprint
import os
from jinja2 import Environment, FileSystemLoader
import rest_call

def get_node_info(hostname):
  network_info = rest_call.get_node()

  for i in network_info.json():
    #pprint(i['hostName'])
    if i['hostName'] == hostname:
      name = i['name']
      index_number = i['nodeIndex']
  return name, index_number

def generate_node_maitenance_json(index_number, name):
  THIS_DIR = os.path.dirname(os.path.abspath(__file__))

  j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)

  payload = j2_env.get_template('maintenance.json').render(
        index_number=index_number,
        name=name
    )

  return(payload)
