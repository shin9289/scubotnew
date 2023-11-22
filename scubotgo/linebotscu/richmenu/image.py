# -*- coding: utf-8 -*-
from linebot import (
  LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('r9DlNu35EuZc5YMW71rHCYFc5tm5Q9ep+hQFoqq56uw8jfoJaSVhoGCFNobMaIdUYS/07Dqd3T4PlnKJZGvdHbw/A6lJaNq1wn9AZEXcJQwlAno5TF4FT8tnbu3SQbk5/rDL8KUNWU2NLrzrkM4YFQdB04t89/1O/w1cDnyilFU=')

#生成的id要改#路徑可能也要改看你放在哪裡我是先複製我的路徑

rich_menu_info = [
    {"id": "richmenu-4dfba927b800b5746b5a6f7bc0a6e4c2", "image_path": "D:\anaconda3\scubotgo\linebotscu\richmenu\校園網站一覽.png"},
    {"id": "richmenu-6478058e571a0fea33abd2379d8ec9ee", "image_path": "D:\anaconda3\scubotgo\linebotscu\richmenu\學生資源.png"},
    {"id": "richmenu-9b6344cc6653faa31b5e028ec524c30e", "image_path": "D:\anaconda3\scubotgo\linebotscu\richmenu\我好餓.png"},
    {"id": "richmenu-678baccfc071d93c6edc1cad7eb4b11e", "image_path": "D:\anaconda3\scubotgo\linebotscu\richmenu\交通資訊.png"},
]

#這裡就不用更改
for menu_info in rich_menu_info:
    with open(menu_info["image_path"], 'rb') as f:
        line_bot_api.set_rich_menu_image(menu_info["id"], "image/png", f)

# 設定預設的richMenu
line_bot_api.set_default_rich_menu(rich_menu_info[0]["id"])