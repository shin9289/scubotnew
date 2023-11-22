# -*- coding: utf-8 -*-
import requests

channel_access_token = 'r9DlNu35EuZc5YMW71rHCYFc5tm5Q9ep+hQFoqq56uw8jfoJaSVhoGCFNobMaIdUYS/07Dqd3T4PlnKJZGvdHbw/A6lJaNq1wn9AZEXcJQwlAno5TF4FT8tnbu3SQbk5/rDL8KUNWU2NLrzrkM4YFQdB04t89/1O/w1cDnyilFU='
headers = {"Authorization": f"Bearer {channel_access_token}"}

rich_menu_ids = [
    "richmenu-4dfba927b800b5746b5a6f7bc0a6e4c2", 
    "richmenu-6478058e571a0fea33abd2379d8ec9ee",
    "richmenu-9b6344cc6653faa31b5e028ec524c30e",
    "richmenu-678baccfc071d93c6edc1cad7eb4b11e"
    ]

for rich_menu_id in rich_menu_ids:
    url = f'https://api.line.me/v2/bot/user/all/richmenu/{rich_menu_id}'
    req = requests.post(url, headers=headers)
    print(req.text)