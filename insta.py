import requests,re


def  decoder(v):
 headers = {
     'authority': 'dencode.com',
     'accept': '*/*',
     'accept-language': 'ar-SA,ar;q=0.9,en-FR;q=0.8,en;q=0.7,en-US;q=0.6',
     'cache-control': 'max-age=0',
     'content-type': 'application/json',
  
     'origin': 'https://dencode.com',
     'referer': 'https://dencode.com/',
     'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
     'sec-ch-ua-mobile': '?1',
     'sec-ch-ua-platform': '"Android"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
 }

 json_data = {
     'type': 'all',
     'method': 'all.all',
     "value":v,
   
     'oe': 'UTF-8',
     'nl': 'crlf',
     'tz': 'Asia/Riyadh',
     'options': {
        'encStrUnicodeEscapeNotation': 'cubu',
       
     },
 }
 response = requests.post('https://dencode.com/dencode', 
 headers=headers,json=json_data)
 ddd=response.json()["response"]["decStrUnicodeEscape"]
 nnn=response.json()["response"]["decStrUnicodeEscape"].find('War')
 return ddd[nnn:1150]
 
 
cookies = {
    'csrftoken': 'k1zDqHJTkG9Vg9lLrqgrJQYJt3agxVnj',
    'mid': 'ZPtZ0wAEAAHpvXdfKsUnPNV3kXJ8',
    'ig_did': '0A3A4425-C5A0-44CD-8D1A-50AE8B478CBD',
    'ig_nrcb': '1',
    'datr': 'xGIAZZne58T8JTElldHuzspd',
    'dpr': '3.2983407974243164',
}

headers = {
    'authority': 'help.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-SA,ar;q=0.9,en-FR;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
  'content-type': 'application/x-www-form-urlencoded',
   
    'origin': 'https://help.instagram.com',
    'pragma': 'no-cache',
    'referer': 'https://help.instagram.com/contact/1784471218363829?fbclid=PAAaZIGWZG9umGh3poJsQPjrbQli-h-eQAydipIq4KaMRUMLbzNvfjXA3hPjU',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVp6Rcd1kE4',
}


name="koko"
username="hadokoko"
email=""

comment="i love you"

data = f'jazoest=2875&lsd=AVp6Rcd1kE4&name={name}&username={username}&email={email}&Field236858559849125_iso2_country_code=SA&Field236858559849125=%D8%A7%D9%84%D9%85%D9%85%D9%84%D9%83%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9&user_comment={comment}&support_form_id=1784471218363829&support_form_locale_id=ar_AR&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&user=0&a=1&req=8&hs=19628.BP%3ADEFAULT.2.0..0.0&dpr=3&ccg=GOOD&rev=1008913870&s=y5yjtj%3A6ys42d%3A6qk9hx&hsi=7283913828603360571&dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&csr=&spin_r=1008913870&spin_b=trunk&spin_t=1695918345&jssesw=1&confirmed=1'

res = requests.post('https://help.instagram.com/ajax/help/contact/submit/page', 

headers=headers, 
data=data)

text=decoder(res.text)

est=re.findall("[أ-ي]+",text)

print(" ".join(est))
