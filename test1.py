import requests

#r=requests.get("https://i.qq.com/?rd=1")
#r.raise_for_status()
#print (r.status_code)
#url='https://user.qzone.qq.com/1121883342/infocenter'
#re=requests.get(url)
#re.raise_for_status()
#print re.text
s=requests.session()
data={'username':'1121883342','password':'123456'}
res=s.post('http://www.zimuku.net/User/login.html',data=data)
re=s.get('http://www.zimuku.net/User/index.html')
print re.text
