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

   
@app.get('/api/hotmail/{gmail}')
async def ga(gmail):
    global cok,uuid
    req=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',});amsc=req.cookies.get_dict()['amsc'];encoded=req.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1];canary = encoded.encode().decode('unicode-escape')
    cookies = {
                            'mkt': 'ar-YE',
                            f'MicrosoftApplicationsTelemetryDeviceId': '{Lol}',
                            'MUID': f'{cok}',
                            'mkt1': 'ar-AR',
                            'ai_session': 'CyuLoU6vSi7HJzZeYNyVoH|1709731817506|1709731817506',
                            'amsc': f'{amsc}',
                            'clrc': '{%2219789%22%3a[%22+VC+x0R6%22%2c%22FutSZdvn%22%2c%22d7PFy/1V%22]}',
                        }
    headers = {
                            'authority': 'signup.live.com',
                            'accept': 'application/json',
                            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                            'canary': f'{canary}',
                            'content-type': 'application/json',
                            'hpgid': '200639',
                            'origin': 'https://signup.live.com',
                            'referer': 'https://signup.live.com/signup?mkt=AR-AR&lic=1&uaid=ad311362ab454b14bb81937965f86b8d',
                            'scid': '100118',
                            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'tcxt': 'VWlP20OW8k/xH6tFupQw1HwrEFETf+tDxcIS0OeqhsBSbBIMy4srnqBeqY1i2lMA5VbPfXSuTUEhdSw9AWoPPSNJeuzfyYceefIZ/1EGoBqppRyXgczQuaM5teemKuAKiUXDaBYMj8Ng8fhejlVVuQmHCBl+PgEGlG7A/8uqXNwqIlrg9tbOqIzHkn5X1jUytMlmFxmEjdLCQnainFfCoxqgPZjkQwcE6hQFElIuxniqWRWk6lmEleIPwhGFID2kbSE5kxjiT5eoUt/S5zxP2a1Yp+shu8ITJrys5pkwMbsWO+L18h8bH4+BG3LFLJk00zd28yeJz7uTq3NRNR1uK+OiCVwGdB5JhxmvsItOIwHc83/xeN0XuTlXGgueChmPKulABKjR4v0VDkutbyPQwRVqRPRALfutQaEjOXdx9FXOCUTySJLtPpeMPIj172+PUSlBhgueKn3Iiz2mzKbR8Kv4JgBlQF5m3dVYyNpSN998fVQE3x94ruAsioYwEOBdfEViB34QpbzAuNfoNmNisCvzI9PKzc+cDKeWkcVd7OtYQSR0AR2Ibr6LE0iulNI5/zqg/BYp3Vf2zaExAmpf8Q==:2:3',
                            'uaid': f'{uuid}',
                            'uiflvr': '1001',
                            'user-agent': generate_user_agent(),
                            'x-ms-apitransport': 'xhr',
                            'x-ms-apiversion': '2',
                        }
    params = {
                            'mkt': 'AR-AR',
                            'lic': '1',
                            'uaid': f'{uuid}',
                        }
    data = {
                                'signInName': f'{gmail}',
                                'uaid': f'{uuid}',
                                'includeSuggestions': True,
                                'uiflvr': 1001,
                                'scid': 100118,
                                'hpgid': 200639,
                            }
    req = requests.post('https://signup.live.com/API/CheckAvailableSigninNames',params=params,cookies=cookies,headers=headers,json=data,).text
    if '"isAvailable":true' in req:
    		data2={
    		"email":f"{gmail}",
    		"status":"Hit",
    		"Dev":"Marko_Bots",
    		}
    		return JSONResponse(content=data2)
    	

    else:
    		
    		dta={
    		"email":f"{gmail}",
    		"status":"Taken",
    		"Dev":"Marko_Bots",
    		}
    		return JSONResponse(content=dta)
#uvicorn.run(app,host='0.0.0.0',port=8080)