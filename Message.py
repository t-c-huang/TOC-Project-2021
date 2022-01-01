from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            TemplateSendMessage, ButtonsTemplate, MessageTemplateAction,
                            PostbackAction, MessageAction, URIAction)

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