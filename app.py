# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('IfUIzR1KSVXN6quJD7Q+YCoKyYApnyf54Af7nVJ8in1e5yMJ+4K9rE+kVJL1dskL9gdrDDfiZZ2Mo1SJTzuqnTo63ByT42H6j4zBR5j8pJRPkohv+RmaUwDk1tpk3XdTZNuXjDGGJSv1uRVFjadpsgdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('d77c3bebde95d5628c5c1ba78a12c0b9') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
