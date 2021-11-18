from os import name
from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))
temp2 = ENV.get_template("switch.j2")
#temp1 = ENV.get_template("vlans.j2")
#with open("port_data.yml") as f:
#    interfaces = yaml.load(f)
#    print(template.render(interface_list=interfaces))

with open("interfaces_data.yml", "r") as f:
    try:
        interfaces  = yaml.safe_load(f)
        #i =  interfaces["vlan"]
        i = interfaces
       #print(i)
        print(temp2.render(interface_list= i))
    except yaml.YAMLError as exc:
        print(exc)

#with open("interfaces_data.yml", "r") as f:
#    try:
#        interfaces = yaml.safe_load(f)
#       # print(temp2.render(interface_list=interfaces))
 #       a = interfaces["interface"][0]['name']
 #       b = interfaces
 #       print(a)
 #   except yaml.YAMLError as exc:
 #       print(exc)