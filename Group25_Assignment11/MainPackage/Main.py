'''
Name: Madison Bratton and Ava Berling
email: brattomn@mail.uc.edu, berlinag@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project
Citations:
Anything else that's relevant
'''

import json
import requests

response = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=xY7N9nKVP0JFQt75s6SIqf5mlGARADhMoYBovMtK')
json_string = response.content

parsed_json = json.loads(json_string) 
