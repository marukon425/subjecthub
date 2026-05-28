import requests

response = requests.get('https://qiita.com/')
text = response.text
print(text)