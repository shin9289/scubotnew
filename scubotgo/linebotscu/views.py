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


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
               events = handler.handle(body, signature)
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
