# -*- coding: utf-8 -*-
"""
richmenub學生資源借用
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
  "name": "學生學習資源",
  "chatBarText": "查看更多資訊",
  "areas": [
    {
      "bounds": {
        "x": 179,
        "y": 707,
        "width": 649,
        "height": 271
      },
      "action": {
        "type": "uri",
        "uri": "https://booking.scu.edu.tw/booking/"
      }
    },
    {
      "bounds": {
        "x": 960,
        "y": 1003,
        "width": 668,
        "height": 304
      },
      "action": {
        "type": "uri",
        "uri": "https://seat.lib.scu.edu.tw/scudesk/login.jsp"
      }
    },
    {
      "bounds": {
        "x": 1725,
        "y": 623,
        "width": 620,
        "height": 277
      },
      "action": {
        "type": "uri",
        "uri": "https://e-rent.scu.edu.tw/rent/"
      }
    },
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 737,
        "height": 213
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-a",
        "data": "richmenu=a"
      }
    },
    {
      "bounds": {
        "x": 786,
        "y": 0,
        "width": 688,
        "height": 198
      },
      "action": {
        "type": "postback",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 1570,
        "y": 0,
        "width": 639,
        "height": 203
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-c",
        "data": "richmenu=c"
      }
    },
    {
      "bounds": {
        "x": 2272,
        "y": 19,
        "width": 199,
        "height": 160
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-d",
        "data": "richmenu=d"
      }
    },
    {
      "bounds": {
        "x": 34,
        "y": 1447,
        "width": 218,
        "height": 199
      },
      "action": {
        "type": "uri",
        "uri": "https://www-ch.scu.edu.tw/october/"
      }
    }
  ]
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
