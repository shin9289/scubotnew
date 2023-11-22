# -*- coding: utf-8 -*-
"""
richmenua校園網站一覽
"""

import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)

headers = {"Authorization":"Bearer 'r9DlNu35EuZc5YMW71rHCYFc5tm5Q9ep+hQFoqq56uw8jfoJaSVhoGCFNobMaIdUYS/07Dqd3T4PlnKJZGvdHbw/A6lJaNq1wn9AZEXcJQwlAno5TF4FT8tnbu3SQbk5/rDL8KUNWU2NLrzrkM4YFQdB04t89/1O/w1cDnyilFU='"} 
line_bot_api = LineBotApi('r9DlNu35EuZc5YMW71rHCYFc5tm5Q9ep+hQFoqq56uw8jfoJaSVhoGCFNobMaIdUYS/07Dqd3T4PlnKJZGvdHbw/A6lJaNq1wn9AZEXcJQwlAno5TF4FT8tnbu3SQbk5/rDL8KUNWU2NLrzrkM4YFQdB04t89/1O/w1cDnyilFU=') 

body = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": true,
  "name": "校園網站一覽",
  "chatBarText": "查看更多資訊",
  "areas": [
    {
      "bounds": {
        "x": 237,
        "y": 1127,
        "width": 727,
        "height": 397
      },
      "action": {
        "type": "uri",
        "uri": "https://web.sys.scu.edu.tw/default.asp"
      }
    },
    {
      "bounds": {
        "x": 1463,
        "y": 1128,
        "width": 601,
        "height": 391
      },
      "action": {
        "type": "uri",
        "uri": "https://api.sys.scu.edu.tw/academic/"
      }
    },
    {
      "bounds": {
        "x": 425,
        "y": 362,
        "width": 528,
        "height": 435
      },
      "action": {
        "type": "uri",
        "uri": "https://web.sys.scu.edu.tw/class40.asp?option=1"
      }
    },
    {
      "bounds": {
        "x": 1532,
        "y": 349,
        "width": 668,
        "height": 382
      },
      "action": {
        "type": "uri",
        "uri": "https://psv.scu.edu.tw/portal/index.html"
      }
    },
    {
      "bounds": {
        "x": 29,
        "y": 577,
        "width": 251,
        "height": 329
      },
      "action": {
        "type": "uri",
        "uri": "https://tronclass.scu.edu.tw/cas/login?service=https://tronclass.scu.edu.tw/user/index&locale=zh_TW&ts=1667105586.532928"
      }
    },
    {
      "bounds": {
        "x": 1061,
        "y": 261,
        "width": 300,
        "height": 233
      },
      "action": {
        "type": "uri",
        "uri": "https://www.zuvio.com.tw/"
      }
    },
    {
      "bounds": {
        "x": 2228,
        "y": 1430,
        "width": 258,
        "height": 256
      },
      "action": {
        "type": "uri",
        "uri": "http://isee.scu.edu.tw/"
      }
    },
    {
      "bounds": {
        "x": 52,
        "y": 30,
        "width": 630,
        "height": 155
      },
      "action": {
        "type": "postback",
        "data": "no-data"
      }
    },
    {
      "bounds": {
        "x": 824,
        "y": 5,
        "width": 620,
        "height": 198
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-b",
        "data": "richmenu=b"
      }
    },
    {
      "bounds": {
        "x": 1589,
        "y": 0,
        "width": 601,
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
        "y": 14,
        "width": 189,
        "height": 180
      },
      "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu-d",
        "data": "richmenu=d"
      }
    }
  ]
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
