# -*- coding: utf-8 -*-
"""
richmenud我好餓
"""

import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)

headers = {"Authorization":"Bearer 'r9DlNu35EuZc5YMW71rHCYFc5tm5Q9ep+hQFoqq56uw8jfoJaSVhoGCFNobMaIdUYS/07Dqd3T4PlnKJZGvdHbw/A6lJaNq1wn9AZEXcJQwlAno5TF4FT8tnbu3SQbk5/rDL8KUNWU2NLrzrkM4YFQdB04t89/1O/w1cDnyilFU='"} #這裡要改
line_bot_api = LineBotApi('r9DlNu35EuZc5YMW71rHCYFc5tm5Q9ep+hQFoqq56uw8jfoJaSVhoGCFNobMaIdUYS/07Dqd3T4PlnKJZGvdHbw/A6lJaNq1wn9AZEXcJQwlAno5TF4FT8tnbu3SQbk5/rDL8KUNWU2NLrzrkM4YFQdB04t89/1O/w1cDnyilFU=') #這裡要改

body = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": true,
  "name": "我好餓",
  "chatBarText": "查看更多資訊",
  "areas": [
    {
      "bounds": {
        "x": 78,
        "y": 401,
        "width": 736,
        "height": 1124
      },
      "action": {
        "type": "postback",
        "text": "雙溪地餐菜單",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 1652,
        "y": 305,
        "width": 611,
        "height": 909
      },
      "action": {
        "type": "postback",
        "text": "城中學餐菜單",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 915,
        "y": 285,
        "width": 625,
        "height": 465
      },
      "action": {
        "type": "postback",
        "text": "遊戲轉盤尚未設定",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 912,
        "y": 1234,
        "width": 653,
        "height": 397
      },
      "action": {
        "type": "postback",
        "text": "周邊美食尚未設定",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 276,
        "y": 0,
        "width": 649,
        "height": 194
      },
      "action": {
        "type": "postback",
        "data": "richmenu=a"
      }
    },
    {
        "bounds":{
            "x": 24,
            "y": 5,
            "width":183,
            "height":183           
        },
        "action":{
        "type": "postback",
        "richMenuAliasId": "richmenu-a",
        "data": "richmenu=a"
        }
    }
  ]
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
             headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)