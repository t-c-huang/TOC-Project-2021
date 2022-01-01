import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            TemplateSendMessage, ButtonsTemplate, MessageTemplateAction,
                            PostbackAction, MessageAction, URIAction)

from fsm import TocMachine
from utils import send_text_message
import Template as tpl
import Message as Msg

load_dotenv()
state_system = ["begin", "menu", "relation"]

#   father's family
state_fathers_family = ["父親","父親的父母", "父親的兄弟姊妹", "父親的姪男/女、甥男/女", "父親的祖父母、外祖父母"]
                        #["父親", "祖父/祖母（爺爺/奶奶）", "叔父(叔母)/伯父(伯母)", "姑姑(姑父)", "堂兄弟姊妹", "(姑)表兄弟姊妹",
                        #"曾祖父/曾祖母", "曾外祖父/曾外祖母", "兄弟姐妹", "姪男/女 or 甥男/女", "祖父母 or 外祖父母"]
transition_fathers_family = [
        {"trigger": "fathers_family","source": "relation","dest": "父親"},
        {"trigger": "fathers_parent","source": "父親","dest": "父親的父母"},
        {"trigger": "fathers_sibling","source": "父親","dest": "父親的兄弟姊妹"},
        {"trigger": "fathers_nephew","source": "父親","dest": "父親的姪男/女、甥男/女"},
        {"trigger": "fathers_grandparent","source": "父親","dest": "父親的祖父母、外祖父母"},
        {"trigger": "go_menu","source": state_fathers_family,"dest": "menu"},
        # {"trigger": "父母","source": "爸爸","dest": "祖父/祖母（爺爺/奶奶）"},
        # {"trigger": "兄弟","source": "爸爸","dest": "叔父(叔母)/伯父(伯母)"},
        # {"trigger": "姐妹","source": "爸爸","dest": "姑姑(姑父)"},
        # {"trigger": "姪男姪女","source": "爸爸","dest": "堂兄弟姊妹"},
        # {"trigger": "甥男甥女","source": "爸爸","dest": "(姑)表兄弟姊妹"},
        # {"trigger": "祖父母","source": "爸爸","dest": "曾祖父/曾祖母"},
        # {"trigger": "外祖父母","source": "爸爸","dest": "曾外祖父/曾外祖母"},
        # {"trigger": "兒女","source": "叔父(叔母)/伯父(伯母)","dest": "堂兄弟姊妹"},
        # {"trigger": "兒女","source": "姑姑(姑父)","dest": "(姑)表兄弟姊妹"}, 
]

#   mother's family
state_mothers_family = ["母親", "母親的父母", "母親的兄弟姊妹", "母親的姪男/女、甥男/女", "母親的祖父母、外祖父母"]
                        #["媽媽", "外祖父/外祖母（外公/外婆）", "舅父（舅母）", "姨母（姨父）", "(舅)表兄弟姊妹",
                        #"姨兄弟姊妹", "外曾祖父/外曾祖母","外曾外祖父/外曾外祖母"]
transition_mothers_family = [
    {"trigger": "mothers_family","source": "relation","dest": "母親"},
    {"trigger": "mothers_parent","source": "母親","dest": "母親的父母"},
    {"trigger": "mothers_sibling","source": "母親","dest": "母親的兄弟姊妹"},
    {"trigger": "mothers_nephew","source": "母親","dest": "母親的姪男/女、甥男/女"},
    {"trigger": "mothers_grandparent","source": "母親","dest": "母親的祖父母、外祖父母"},
    {"trigger": "go_menu","source": state_mothers_family,"dest": "menu"},
    # {"trigger": "父母","source": "媽媽","dest": "外祖父/外祖母（外公/外婆）"},
    # {"trigger": "兄弟","source": "媽媽","dest": "舅父（舅母）"},
    # {"trigger": "姐妹","source": "媽媽","dest": "姨母（姨父）"},
    # {"trigger": "姪男姪女","source": "媽媽","dest": "(舅)表兄弟姊妹"},
    # {"trigger": "甥男甥女","source": "媽媽","dest": "姨兄弟姊妹"},
    # {"trigger": "祖父母","source": "媽媽","dest": "外曾祖父/外曾祖母"},
    # {"trigger": "外祖父母","source": "媽媽","dest": "外曾外祖父/外曾外祖母"},
    # {"trigger": "兒女","source": "舅父（舅母）","dest": "(舅)表兄弟姊妹"},
    # {"trigger": "兒女","source": "姨母（姨父）","dest": "姨兄弟姊妹"},
]

#   son's family
# state_sons_family = ["兒子", "媳婦", "孫子/孫女", "孫媳婦", "孫女婿",
#                      "曾孫/曾孫女", "親家公/親家母"]
# transition_sons_family = [
#     {"trigger": "sons_family","source": "relation","dest": "兒子"},
#     {"trigger": "妻子","source": "兒子","dest": "媳婦"},
#     {"trigger": "兒女","source": "兒子","dest": "孫子/孫女"},
#     {"trigger": "兒婦","source": "兒子","dest": "孫媳婦"},
#     {"trigger": "兒婿","source": "兒子","dest": "孫女婿"},
#     {"trigger": "兒子孫","source": "兒子","dest": "曾孫/曾孫女"},
#     {"trigger": "配偶父母","source": "兒子","dest": "親家公/親家母"}, 
#     {"trigger": "父母","source": "媳婦","dest": "親家公/親家母"}, 
    
# ]

# #   daughter's family
# state_daughters_family = ["女兒", "媳婦", "外孫/外孫女", "外孫媳婦", "外孫女婿",
#                          "外曾孫/外曾孫女", "親家公/親家母"]
# transition_daughters_family = [
#     {"trigger": "daughts_family","source": "relation","dest": "女兒"},
#     {"trigger": "丈夫","source": "女兒","dest": "女婿"},
#     {"trigger": "兒女","source": "女兒","dest": "外孫/外孫女"},
#     {"trigger": "兒婦","source": "女兒","dest": "外孫媳婦"},
#     {"trigger": "兒婿","source": "女兒","dest": "外孫女婿"},
#     {"trigger": "兒女孫","source": "女兒","dest": "外曾孫/外曾孫女"},
#     {"trigger": "配偶父母","source": "女兒","dest": "親家公/親家母"},
#     {"trigger": "父母","source": "女婿","dest": "親家公/親家母"}, 
# ]

transition_system = [
    {"trigger": "go_menu","source": "begin","dest": "menu"},
    {"trigger": "go_relation","source": "menu","dest": "relation"},
    # {"trigger": "back","source": state_fathers_family,"dest": "relation"},
    # {"trigger": "back","source": state_mothers_family,"dest": "relation"},
    # {"trigger": "back","source": state_sons_family,"dest": "relation"},
    # {"trigger": "back","source": state_daughters_family,"dest": "relation"},
]
# main_functions = ["relation", "card", "red_envlope"]
machine = TocMachine(
    states=state_system + state_fathers_family + state_mothers_family,# + state_sons_family + state_daughters_family,
    transitions=transition_system + transition_fathers_family + transition_mothers_family, # + transition_sons_family+ transition_daughters_family,
    initial="begin",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
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
    # # parse webhook body
    # try:
    #     events = parser.parse(body, signature)
    # except InvalidSignatureError:
    #     abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    # for event in events:
    #     if not isinstance(event, MessageEvent):
    #         continue
    #     if not isinstance(event.message, TextMessage):
    #         continue

    # return "OK"

# 學你說話

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(f'\nFSM STATE: {machine.state}')
    if machine.state == "begin":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    
    elif machine.state == "menu":
        if msg == "親戚稱謂查詢":
            machine.go_relation()
            tpl.relation(line_bot_api, event)  
        
    elif machine.state == "relation":
        if msg == "爸爸的":
            machine.fathers_family()
            tpl.fathers_family(line_bot_api, event)
        elif msg == "媽媽的":
            machine.mothers_family()
            tpl.mothers_family(line_bot_api, event)
        # elif msg == "兒子":
        #     machine.sons_family()
        #     tpl.sons_family(line_bot_api, event)
        # elif msg == "女兒":
        #     machine.daughters_family()
        #     tpl.daughters_family_family
    elif machine.state == "父親":
        if msg == "父母":
            machine.fathers_parent()
            Msg.fathers_patrent(line_bot_api, event)
        elif msg == "兄弟姐妹":
            machine.fathers_sibling()
            Msg.fathers_sibling(line_bot_api, event)
            #tpl.fathers_family_L2(line_bot_api, event)
        elif msg == "姪男/女 or 甥男/女":
            machine.fathers_nephew()
            Msg.fathers_nephew(line_bot_api, event)
        elif msg == "祖父母 or 外祖父母":
            machine.fathers_grandparent()
            Msg.fathers_grandparent(line_bot_api, event)
    
    elif machine.state == "母親":
        if msg == "父母":
            machine.mothers_parent()
            Msg.mothers_patrent(line_bot_api, event)
        elif msg == "兄弟姐妹":
            machine.mothers_sibling()
            Msg.mothers_sibling(line_bot_api, event)
            #tpl.mothers_family_L2(line_bot_api, event)
        elif msg == "姪男/女 or 甥男/女":
            machine.mothers_nephew()
            Msg.mothers_nephew(line_bot_api, event)
        elif msg == "祖父母 or 外祖父母":
            machine.mothers_grandparent()
            Msg.mothers_grandparent(line_bot_api, event)
    elif machine.state == "父親的父母":
        machine.go_menu()
        tpl.menu(line_bot_api, event) 
    elif machine.state == "父親的兄弟姊妹":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    elif machine.state == "父親的姪男/女、甥男/女":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    elif machine.state == "父親的祖父母、外祖父母":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    elif machine.state == "母親的父母":
        machine.go_menu()
        tpl.menu(line_bot_api, event) 
    elif machine.state == "母親的兄弟姊妹":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    elif machine.state == "母親的姪男/女、甥男/女":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    elif machine.state == "母親的祖父母、外祖父母":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
     
@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
