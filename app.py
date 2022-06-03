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
4HwoSO9r1rc0uTGNTEKitwlLNwh8MC/uTisf9Ew/Kcwc27qElE5U6FlgXTEUQ/0BUcNy57///BBV3YP8FFTa2wEVJ54wSirJMosQZrqlY2MEMSdAG4j23eiwvvk5M/igCNA9B8fPzRZEOPFgVLw/8AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('333daf7ad1f4627bece51c7b60aa375e')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()