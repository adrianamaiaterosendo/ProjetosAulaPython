import requests
res = requests.get("https://digitalinnovation.one/blog/")
print(res)
res.encoding = "uft-8"
