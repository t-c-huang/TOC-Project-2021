from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            TemplateSendMessage, ButtonsTemplate, MessageTemplateAction,
                            PostbackAction, MessageAction, URIAction)
import json
# line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))

def fathers_patrent(line_bot_api, event):
    text = "- 父親的父親 => 祖父\n\
            - 父親的母親 => 祖母\n\n\
            - 你是他們的孫子/孫女\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))

def fathers_sibling(line_bot_api, event):
    text = "- 父親的哥哥 => 伯父\
            - 父親的弟弟 => 叔父\n\
            - 父親的姐姐、妹妹 => 姑姑\n\n\
            - 你是他們的姪子/姪女\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))

def fathers_nephew(line_bot_api, event):
    text = "- 父親的哥哥、弟弟(伯父、叔父)的小孩 => 堂兄弟姐妹\n\
            - 父親的姐姐、妹妹(姑姑)的小孩 => (姑)表兄弟姐妹\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))

def fathers_grandparent(line_bot_api, event):
    text = "父親的父親的父母 => 曾祖父母\n\
            父親的母親的父母 => 曾外祖父母\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))

def mothers_patrent(line_bot_api, event):
    text = "- 母親的父親 => 外祖父\n\
            - 母親的母親 => 外祖母\n\n\
            - 你是他們的外孫/外孫女\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))
    
def mothers_sibling(line_bot_api, event):
    text = "- 母親的哥哥、弟弟 => 舅父\n\
            - 母親的姐姐、妹妹 => 姨母\n\n\
            - 你是他們的甥男/甥女\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))
    
def mothers_nephew(line_bot_api, event):
    text = "- 母親的哥哥、弟弟(舅父)的小孩 => (舅)兄弟姐妹\n\
            - 母親的姐姐、妹妹(姨母)的小孩 => 姨兄弟姐妹\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))

def mothers_grandparent(line_bot_api, event):
    text = "母親的父親的父母 => 外曾祖父母\n\
            母親的母親的父母 => 外曾外祖父母\n\
            （傳送任意鍵回選單）"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))
    
def show_income(line_bot_api, event):
    uid = event.source.user_id
    text = ""
    with open(f"user_data/{uid}.json", "r", encoding='utf8') as f:
        user_data = json.load(f)
        text = "紅包收入：\n" + str(user_data['income_record']).replace('{', '').replace('}', '').replace('],', ',\n').replace('[', '').replace('\'', '').replace("]", "")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))

def show_expense(line_bot_api, event):
    uid = event.source.user_id
    text = ""
    with open(f"user_data/{uid}.json", "r", encoding='utf8') as f:
        user_data = json.load(f)
        text = "紅包支出：\n" + str(user_data['expense_record']).replace('{', '').replace('}', '').replace('],', ',\n').replace('[', '').replace('\'', '').replace("]", "")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))
    
def show_state_money(line_bot_api, event, income_record, expense_record, state):
    text = f"{state}\n\
            收入 NTD {income_record[state]}\n\
            支出 NTD {expense_record[state]}\n\
            輸入 +NUMBER 新增收入\n\
            輸入 -NUMBER 新增支出\n\
            輸入 q 回到主選單"
    line_bot_api.push_message(
        event.source.user_id,
        TextSendMessage(text=text))
    print(income_record)
    print(expense_record)
    
def how_much_receive(line_bot_api, event):
    text = f"輸入正整數數字表示收到的紅包金額"
    line_bot_api.push_message(
        event.source.user_id,
        TextSendMessage(text=text))
    
def how_much_spend(line_bot_api, event):
    text = f"輸入正整數數字表示支出的紅包金額"
    line_bot_api.push_message(
        event.source.user_id,
        TextSendMessage(text=text))