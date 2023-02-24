#https://www.dns-shop.ru/search/?q=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D1%8B&category=17a89aab16404e77&p=3

import requests 
res = requests.get(f"https://www.dns-shop.ru/search/?q=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D1%8B&category=17a89aab16404e77")     
text = res.text
