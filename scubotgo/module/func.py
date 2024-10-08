
from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='成功'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤'))

#校園頭條
def get_latest_news(event):
    url = "https://news.scu.edu.tw/news-7"
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('.table.table-striped tbody td a')

    news_info = []
    news_info.append("🎉校園頭條🎉")
    for each_title in titles[:10]:
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

#一般公告
def get_announcement(event):
    url = "https://news.scu.edu.tw/news-3"
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('.table.table-striped tbody td a')

    news_info = []
    news_info.append("🎉一般公告🎉")
    for each_title in titles[:10]:
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

#學術活動
def academic_activity(event):
    url = "https://news.scu.edu.tw/news-5"
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('.table.table-striped tbody td a')

    news_info = []
    news_info.append("🎉學生活動🎉")
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

#學術公告
def academic_announcement(event):
    url = "https://news.scu.edu.tw/news-4"
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('.table.table-striped tbody td a')

    news_info = []
    news_info.append("🎉學術公告🎉")
    for each_title in titles[:10]:
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
'''
def menu(event):
    carousel_template = {
        "type": "flex",
        "altText": "This is a Carousel Template",
        "contents": {
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://example.com/item1.jpg",
                        "size": "full",
                        "aspectRatio": "1:1",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Item 1",
                                "weight": "bold",
                                "size": "lg"
                            },
                            {
                                "type": "text",
                                "text": "Description of Item 1",
                                "wrap": True
                            }
                        ]
                    }
                },
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://example.com/item2.jpg",
                        "size": "full",
                        "aspectRatio": "1:1",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Item 2",
                                "weight": "bold",
                                "size": "lg"
                            },
                            {
                                "type": "text",
                                "text": "Description of Item 2",
                                "wrap": True
                            }
                        ]
                    }
                }
            ]
        }
    }

    # 建立 FlexSendMessage 物件
    #flex_message = FlexSendMessage(alt_text="This is a Carousel Template", contents=carousel_template)

    
    try:
        line_bot_api.reply_message(event.reply_token,FlexSendMessage(alt_text="This is a Carousel Template", contents=carousel_template))
                
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="失敗"))
'''