from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event, message):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發送訊息時出現錯誤'))

def get_latest_news():
    url = "https://www-ch.scu.edu.tw/october/search?category=5"
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('.table.table-striped [headers="header"] a')

    news_info = []
    for each_title in titles[:5]:
        title_text = each_title.text.strip()
        link_href = each_title['href'].strip()
        news_info.append(f"{title_text}\n{link_href}\n")