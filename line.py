import requests,json
import urllib.parse
import sys

LINE_ACCESS_TOKEN="YOUR TOKEN"
url = "https://notify-api.line.me/api/notify" 

def line_text(message):	
	msg = urllib.parse.urlencode({"message":message})
	LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
	session = requests.Session()
	a=session.post(url, headers=LINE_HEADERS, data=msg)
	print(a.text)
	
def line_pic(file):	
	msg = {"imageFile": open(file, 'rb')}
	LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
	session = requests.Session()
	b=session.post(url, headers=LINE_HEADERS, files=msg)
	print(b.text)

line_text(sys.argv[1])