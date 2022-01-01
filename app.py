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
import state_and_transition as sat

load_dotenv()

machine = TocMachine(
    states=sat.state_system + sat.state_fathers_family + sat.state_mothers_family,# + state_sons_family + state_daughters_family,
    transitions=sat.transition_system + sat.transition_fathers_family + sat.transition_mothers_family, # + transition_sons_family+ transition_daughters_family,
    initial="begin",
    auto_transitions=False,
    show_conditions=True,
)

income_record = dict.fromkeys(sat.state_fathers_family + sat.state_mothers_family, 10)
expense_record = dict.fromkeys(sat.state_fathers_family + sat.state_mothers_family, 10)


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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(f'\nFSM STATE: {machine.state}')
    if machine.state == "begin":
        machine.go_menu()
        tpl.menu(line_bot_api, event)
    
    elif machine.state == "menu":
        if msg == "親戚稱謂查詢&紅包紀錄":
            machine.go_relation()
            tpl.relation(line_bot_api, event)
        if msg == "紅包規劃":
            machine.go_money()
            tpl.money(line_bot_api, event)
    
    elif machine.state == "money":
        if msg == "紅包收入":
            Msg.show_income(line_bot_api, event, income_record)
            print(income_record)
        elif msg == "紅包支出":
            Msg.show_expense(line_bot_api, event, expense_record)
            print(expense_record)
        # elif msg == "查看收入"
        # elif msg == "查看支出”
           
        
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
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
        elif msg == "兄弟姐妹":
            machine.fathers_sibling()
            Msg.fathers_sibling(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
            #tpl.fathers_family_L2(line_bot_api, event)
        elif msg == "姪男/女 or 甥男/女":
            machine.fathers_nephew()
            Msg.fathers_nephew(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
        elif msg == "祖父母 or 外祖父母":
            machine.fathers_grandparent()
            Msg.fathers_grandparent(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    
    elif machine.state == "母親":
        if msg == "父母":
            machine.mothers_parent()
            Msg.mothers_patrent(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
        elif msg == "兄弟姐妹":
            machine.mothers_sibling()
            Msg.mothers_sibling(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
            #tpl.mothers_family_L2(line_bot_api, event)
        elif msg == "姪男/女 or 甥男/女":
            machine.mothers_nephew()
            Msg.mothers_nephew(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
        elif msg == "祖父母 or 外祖父母":
            machine.mothers_grandparent()
            Msg.mothers_grandparent(line_bot_api, event)
            Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "父親的父母":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state) 
    elif machine.state == "父親的兄弟姊妹":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "父親的姪男/女、甥男/女":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "父親的祖父母、外祖父母":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "母親的父母":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event) 
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "母親的兄弟姊妹":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "母親的姪男/女、甥男/女":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
    elif machine.state == "母親的祖父母、外祖父母":
        if msg == "q":
            machine.go_menu()
            tpl.menu(line_bot_api, event)
        else:
            try:
                num = int(msg)
                if msg > 0:
                    income_record[machine.state] += num
                else:
                    expense_record[machine.state] += num
            except:
               Msg.show_state_money(line_bot_api, event, income_record, expense_record, machine.state)
     
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
