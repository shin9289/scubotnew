import gspread
import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

# 初始化gspread
gc = gspread.service_account(filename="C:\Users\吳欣晏\Desktop\scubotnew\scubotgo\linebotscu\linebotscu.json") #這裡你下要下載json金鑰文件然後複製路徑
SPREADSHEET_ID = '1noXSpkwTT7qVeMTaOJwTPd4OM2VvLxTJ67q1FdJB59k'
SHEET_NAME = '雙溪'

def get_google_sheets_data():
    try:
        sh = gc.open_by_key(SPREADSHEET_ID)
        worksheet = sh.worksheet(SHEET_NAME)
        values = worksheet.get_all_values()

        if not values:
            return "No data found."
        else:
            return "\n".join(["\t".join(row) for row in values])

    except Exception as e:
        return f"Error accessing Google Sheets: {str(e)}"

def line_bot_webhook(request):
    # 處理Line消息
    signature = request.headers['X-Line-Signature']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponse(status=400)

    return HttpResponse(status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    user_id = event.source.user_id
    received_text = event.message.text

    # 如果收到的文字是觸發關鍵字
    if "雙溪美食推薦" in received_text:
        data = get_google_sheets_data()

        # 將Google Sheets數據發送給使用者
        try:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=data)
            )
        except LineBotApiError as e:
            print(f"LineBot API Error: {e}")
            # 這裡你可以處理API錯誤的情況
    #最新消息
    elif "最新消息" in received_text:
        latest_news = func.get_latest_news()  # 调用func.py中的函数
        try:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=latest_news)
            )
        except LineBotApiError as e:
            print(f"LineBot API Error: {e}")

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
               events = handler.parse(body, signature)
        except InvalidSignatureError:
               return HttpResponseForbidden()
        except LineBotApiError:
               return HttpResponseBadRequest()

        for event in events:
               if isinstance(event, MessageEvent):
                     if isinstance(event.message,TextMessage):
                           mtext=event.message.text
                           if mtext =='測試':
                                 func.sendText(event)
        return HttpResponse()
    else:
         return HttpResponseBadRequest ()
