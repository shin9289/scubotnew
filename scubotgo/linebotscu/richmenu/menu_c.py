# -*- coding: utf-8 -*-
"""
richmenuc交通資訊
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
  "name": "交通資訊",
  "chatBarText": "查看更多資訊",
  "areas": [
    {
      "bounds": {
        "x": 243,
        "y": 401,
        "width": 804,
        "height": 1091
      },
      "action": {
        "type": "uri",
        "uri": "https://pda.5284.gov.taipei/MQS/route.jsp?rid=17333"
      }
    },
    {
      "bounds": {
        "x": 1376,
        "y": 406,
        "width": 815,
        "height": 1089
      },
      "action": {
        "type": "uri",
        "uri": "https://web-ch.scu.edu.tw/storage/app/media/194/112-1/1121121006202310061732.pdf"
      }
    },
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 732,
        "height": 203
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-a",
        "data": "richmenu=a"
      }
    },
    {
      "bounds": {
        "x": 765,
        "y": 4,
        "width": 736,
        "height": 194
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-b",
        "data": "richmenu=b"
      }
    },
    {
      "bounds": {
        "x": 1536,
        "y": 0,
        "width": 716,
        "height": 213
      },
      "action": {
        "type": "postback",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 2283,
        "y": 6,
        "width": 212,
        "height": 188
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-d",
        "data": "richmenu=d"
      }
    }
  ]
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
             headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
