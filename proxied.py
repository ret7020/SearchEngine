import requests 
a = requests.get("https://ident.me", proxies={"https": "socks5://72.210.208.101:4145"})
print(a)