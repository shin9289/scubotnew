
from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='成功'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤'))

def get_latest_news(event):
    url = "https://www-news.scu.edu.tw/news-7"
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('.table.table-striped tbody td a')

    news_info = []
    news_info.append("🎉最新消息🎉")
    for each_title in titles[:5]:
        title_text = each_title.text.strip()
        link_href = each_title['href'].strip()
        news_info.append(f"\n{title_text}\n{link_href}")

    if news_info:
        news_text = "\n".join(news_info)
        try:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=news_text))
                
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="抱歉，沒有找到最新消息。"))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="錯誤2"))
