from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            TemplateSendMessage, ButtonsTemplate, MessageTemplateAction,
                            PostbackAction, MessageAction, URIAction)


def menu(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=event.message.text)
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                # thumbnail_image_url='https://example.com/image.jpg',
                title='Menu',
                text='Please select',
                actions=[
                    # PostbackAction(
                    #     label='postback',
                    #     display_text='postback text',
                    #     data='action=buy&itemid=1'
                    # ),
                    MessageAction(
                        label='親戚稱謂查詢',
                        text='親戚稱謂查詢'
                    ),
                    # MessageAction(
                    #     label='紅包規劃',
                    #     text='紅包規劃'
                    # ),
                    # MessageAction(
                    #     label='新年訊息',
                    #     text='新年訊息'
                    # ),
                    URIAction(
                        label='Document',
                        uri='https://c5e4-111-254-58-230.ngrok.io/show-fsm'
                    )
                ]
            )
        )
    )
    

def relation(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='親戚稱謂查詢',
                text='Please select (Enter q for showing family graph!)',
                actions=[
                    MessageAction(
                        label='爸爸的',
                        text='爸爸的'
                    ),
                    MessageAction(
                        label='媽媽的',
                        text='媽媽的'
                    ),
                    # MessageAction(
                    #     label='兒子的',
                    #     text='兒子的'
                    # ),
                    # MessageAction(
                    #     label='女兒的',
                    #     text='女兒的'
                    # ),
                ]
            )
        )
    )

def fathers_family(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你父親的',
                text='Please select (Enter q for showing family graph!)',
                actions=[
                    MessageAction(
                        label='父母',
                        text='父母'
                    ),
                    MessageAction(
                        label='兄弟姊妹',
                        text='兄弟姐妹'
                    ),
                    MessageAction(
                        label='姪男/女 or 甥男/女',
                        text='姪男/女 or 甥男/女'
                    ),
                    MessageAction(
                        label='祖父母 or 外祖父母',
                        text='祖父母 or 外祖父母'
                    ),
                ]
            )
        )
    )
    
def fathers_family_L2(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你父親的',
                text='Please select (Enter q for showing family graph!)',
                actions=[
                    MessageAction(
                        label='哥哥',
                        text='哥哥',
                    ),
                    MessageAction(
                        label='弟弟',
                        text='弟弟'
                    ),
                    MessageAction(
                        label='姊姊',
                        text='姊姊'
                    ),
                    MessageAction(
                        label='妹妹',
                        text='妹妹'
                    ),
                ]
            )
        )
    )
    

def mothers_family(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你母親的',
                text='Please select (Enter q for showing family graph!)',
                actions=[
                    MessageAction(
                        label='父母',
                        text='父母'
                    ),
                    MessageAction(
                        label='兄弟姊妹',
                        text='兄弟姐妹'
                    ),
                    MessageAction(
                        label='姪男/女 or 甥男/女',
                        text='姪男/女 or 甥男/女'
                    ),
                    MessageAction(
                        label='祖父母 or 外祖父母',
                        text='祖父母 or 外祖父母'
                    ),
                ]
            )
        )
    )
def mothers_family_L2(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你母親的',
                text='Please select (Enter q for showing family graph!)',
                actions=[
                    MessageAction(
                        label='哥哥',
                        text='哥哥',
                    ),
                    MessageAction(
                        label='弟弟',
                        text='弟弟'
                    ),
                    MessageAction(
                        label='姊姊',
                        text='姊姊'
                    ),
                    MessageAction(
                        label='妹妹',
                        text='妹妹'
                    ),
                ]
            )
        )
    )
 
# def sons_family(line_bot_api, event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TemplateSendMessage(
#             alt_text='Buttons template',
#             template=ButtonsTemplate(
#                 title='你兒子的',
#                 text='Please select (Enter q for showing family graph!)',
#                 actions=[
#                     MessageAction(
#                         label='配偶',
#                         text='配偶'
#                     ),
#                     MessageAction(
#                         label='兒女',
#                         text='兒女'
#                     ),
#                     MessageAction(
#                         label='孫子/女',
#                         text='孫子/女'
#                     ),                   
#                 ]
#             )
#         )
#     ) 

# def daughters_family_family(line_bot_api, event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TemplateSendMessage(
#             alt_text='Buttons template',
#             template=ButtonsTemplate(
#                 title='你女兒的',
#                 text='Please select (Enter q for showing family graph!)',
#                 actions=[
#                     MessageAction(
#                         label='配偶',
#                         text='配偶'
#                     ),
#                     MessageAction(
#                         label='兒女',
#                         text='兒女'
#                     ),
#                     MessageAction(
#                         label='孫子/女',
#                         text='孫子/女'
#                     ),                   
#                 ]
#             )
#         )
#     )  

# line_bot_api.reply_message(
#     event.reply_token,
#     # TextSendMessage(text=event.message.text)
#     TemplateSendMessage(
#         alt_text='Buttons template',
#         template=ButtonsTemplate(
#             thumbnail_image_url='https://example.com/image.jpg',
#             title='Menu',
#             text='Please select',
#             actions=[
#                 PostbackAction(
#                     label='postback',
#                     display_text='postback text',
#                     data='action=buy&itemid=1'
#                 ),
#                 MessageAction(
#                     label='message',
#                     text='message text'
#                 ),
#                 URIAction(
#                     label='uri',
#                     uri='http://example.com/'
#                 )
#             ]
#         )
#     )
# )