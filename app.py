import os
import sys
import json

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

machine_dict = {}
def create_machine():
    return TocMachine(
    states=sat.state_system + sat.state_fathers_family + sat.state_mothers_family,# + state_sons_family + state_daughters_family,
    transitions=sat.transition_system + sat.transition_fathers_family + sat.transition_mothers_family, # + transition_sons_family+ transition_daughters_family,
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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    uid = event.source.user_id
    if uid not in machine_dict.keys():
        family = ["祖父", "祖母", '伯父', '叔父', '姑母', '堂兄弟姐妹', '(姑)表兄弟姐妹',
                         '舅父', '姨母', '外祖父', '外祖母', '(舅)兄弟姐妹', '姨兄弟姐妹']
        income_record = dict.fromkeys(family, [])
        expense_record = dict.fromkeys(family, [])
        user_data = {"income_record": income_record, "expense_record": expense_record}
        with open(f"user_data/{uid}.json", 'w', encoding='utf8') as f:
            json.dump(user_data, f, ensure_ascii=False)
        new_machine = create_machine()
        machine_dict[uid] = new_machine
    
    machine = machine_dict[uid]
    
    print(f'\nFSM STATE: {machine.state}')
    
    machine.advance(line_bot_api, event, machine)
     
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
        uid = event.source.user_id
        if uid in machine_dict.keys():
            uid_dict = machine_dict[uid]
            machine = uid_dict["machine"]
        else:
            machine = create_machine()
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine = create_machine()
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

# def update_earning_record(uid, num, who):
#     print(machine_dict)
#     uid_dict = machine_dict[uid]
#     income_record = uid_dict["income_record"]
#     income_record[who] += num
    
# def update_expense_record(uid, num, who):
#     print(machine_dict)
#     uid_dict = machine_dict[uid]
#     expense_record = uid_dict["expense_record"]
#     expense_record[who] += num
if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
