import json
import requests

#import BaseFile as bc


#class Project_name_base_class():
url = "https://reqres.in/api/users"
f=open("Project_Name.json")
data1 = json.load(f)

def commmon_method(self):
   for i in data1["Project_name_validation"]:
     response_body = requests.post(url, i)