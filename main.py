import os,sys
#os.system("pip install fastapi")
#os.system("pip install uvicorn")
from fastapi import Response
import requests
import os
import random
import uvicorn
from fastapi import Request
import json
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
app = FastAPI()
a=int(0)
from fastapi import FastAPI, UploadFile
from secrets import token_hex
import uuid,secrets
cok = token_hex(8) * 2
uuid = str(uuid.uuid4())
app = FastAPI()
from requests import post
import random,threading,time
from user_agent import generate_user_agent

   
@app.get('/api/{email}')
async def check(email):
		url="https://i.instagram.com/api/v1/users/check_email/"
		headers={'X-Pigeon-Session-Id':'f42d4ab9-5a5e-4be0-b06c-fd5cb5a17527',
'X-Pigeon-Rawclienttime':'1711282869.187',
'X-IG-Connection-Speed':'-1kbps',
'X-IG-Bandwidth-Speed-KBPS':'-1.000',
'X-IG-Bandwidth-TotalBytes-B':'0',
'X-IG-Bandwidth-TotalTime-MS':'0',
'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
'X-IG-Connection-Type':'WIFI',
'X-IG-Capabilities':'3brTvw==',
'X-IG-App-ID':'567067343352427',
'User-Agent':'Instagram 100.0.0.17.129 Android (31/12; 320dpi; 720x1444; TECNO; TECNO BF6; TECNO-BF6; BF6; ar_BH; 161478664)',
'Accept-Language':'ar-BH, en-US',
'Cookie':'mid=ZgAaUwABAAFbkj4DEwxlXgTq3aqW; csrftoken=oxRENlfRHtGGyWXLD9tyr7J0Dd4mVaMO',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Accept-Encoding':'gzip, deflate',
'Host':'i.instagram.com',
'X-FB-HTTP-Engine':'Liger',
'Connection':'keep-alive',
'Content-Length':'427',};da={
 'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","email":"'f'{email}''"}',
 
 'ig_sig_key_version':'4',
 }
		s=post(url,headers=headers,data=da).text
		if "email_is_taken" in s:
			dta={
    		"email":f"{email}",
    		"status":"Good",
    		"Dev":"Marko_Bots",
    		}
			return JSONResponse(content=dta)	
		elif "يرجى الانتظار لبضع دقائق قبل إعادة المحاولة." in s:
			url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
			h={
 'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
 'X-Pigeon-Rawclienttime':'1707104597.347',
 'X-IG-Connection-Speed':'-1kbps',
 'X-IG-Bandwidth-Speed-KBPS':'-1.000',
 'X-IG-Bandwidth-TotalBytes-B':'0',
 'X-IG-Bandwidth-TotalTime-MS':'0',
 'X-IG-VP9-Capable':'false',
 'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
 'X-IG-Connection-Type':'WIFI',
 'X-IG-Capabilities':'3brTvw==',
 'X-IG-App-ID':'567067343352427',
 'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
 'Accept-Language':'ar-IQ, en-US',
 'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'Accept-Encoding':'gzip, deflate',
 'Host':'i.instagram.com',
 'X-FB-HTTP-Engine':'Liger',
 'Connection':'keep-alive',
 'Content-Length':'364',
 }
			da={
 'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',
 
 'ig_sig_key_version':'4',
 }
			s=post(url,headers=h,data=da).text
			if '"تم إرسال البريد الإلكتروني"' in s:
				dta={
    		"email":f"{email}",
    		"status":"Good",
    		"Dev":"Marko_Bots",
    		}
				return JSONResponse(content=dta)
			elif "لم يتم العثور على المستخدم" in s:
				dta={
    		"email":f"{email}",
    		"status":"Bad",
    		"Dev":"Marko_Bots",
    		}
				return JSONResponse(content=dta)
			else:
				url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/';headers = {
            'accept':'*/*',
            'accept-encoding':'gzip, deflate',
            'accept-language':'en-US,en;q=0.8',
            'content-length':'303',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'mid=ZQZC9QAEAAG9NicS3jBHkYqHlp8C; ig_nrcb=1; ig_did=AC6A65E6-8577-4CDE-8F3F-4B24D5787A91; datr=D0MGZZ_cUrCctc7jPE92HUgb; csrftoken=NYaOlpVmXUwzESZVfuFOYqbJ0gHzcvks',
            'dpr':'1',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/',
            'user-agent':str(generate_user_agent()),
            'viewport-width':'808',
            'x-asbd-id':'129477',
            'x-csrftoken':'NYaOlpVmXUwzESZVfuFOYqbJ0gHzcvks',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'1008686036',
            'x-requested-with':'XMLHttpRequest',
            }

				tim = str(time.time()).split('.')[0]

				data = {
            'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{tim}:tgffghgfh',
            'optIntoOneTap':'false',
            'queryParams':'{}',
            'trustedDeviceRecords':'{}',
            'username':email,
            }

				re = requests.post(url,headers=headers,data=data).text
				if ('"user":true') in re:
					dta={
    		"email":f"{email}",
    		"status":"Good",
    		"Dev":"Marko_Bots",
    		}
					return JSONResponse(content=dta)
				else:
					dta={
    		"email":f"{email}",
    		"status":"Bad",
    		"Dev":"Marko_Bots",
    		}
					return JSONResponse(content=dta)
		else:
			dta={
    		"email":f"{email}",
    		"status":"Bad",
    		"Dev":"Marko_Bots",
    		}
			return JSONResponse(content=dta)
#uvicorn.run(app,host='0.0.0.0',port=8080)
