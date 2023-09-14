import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/wenhan6/lab1/main/lab1.py")

print(resp.text)
