import requests
import os
import json

# !!
print("\033[0;31m!! Please don't leak your access token to anyone !!\033[0m")
# !!

sAccessToken = input("Please enter your access token: ")
os.system("cls")

url = "https://app-api.salad.io/api/v1/profile/balance"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
}

cookies = {
    # sIdRefreshToken is used to refresh the authentication token, it not needed for API requests unless you're trying to refresh the token.
    "sIdRefreshToken": "a",
    "sAccessToken": sAccessToken
}

response = requests.get(url=url, headers=headers, cookies=cookies)

if response.status_code != 200:
    print('It doesn\'t look like that was successful!')
else:
    print('It look like that was successful!')
    response_json = response.json()
    print(f"""
    Your current balance is {response_json["currentBalance"]}!
    Your lifetime balance is {response_json["lifetimeBalance"]}!
    """)

print(f'Status code: {response.status_code}')
print(f'Data: {response.text}')