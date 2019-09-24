import urllib.request
import  urllib.parse
url='https://www.baidu.com/s'
word={"wd":"pyton"}
word1=urllib.parse.urlencode(word)
new_url=url+"?"+word1
print(new_url)
header={"User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.171314"}
request=urllib.request.Request(new_url,headers=header)

response=urllib.request.urlopen(request)

html=response.read().decode("utf-8")
print(html)
