from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            TemplateSendMessage, ButtonsTemplate, MessageTemplateAction,
                            PostbackAction, MessageAction, URIAction, ImageSendMessage, ConfirmTemplate, CarouselTemplate, CarouselColumn)
import urllib
import re
import random

def menu(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=event.message.text)
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://lh3.googleusercontent.com/proxy/YyRPaDhpvXqBSV0JAYpofUAyPfFVVafTRhNC31akWltJjrCPJTvLZAugbCNO5o2Dusfvy1OtZ6gNgpdCRWTftoceEvvDy7oE_Vc0Z9pW1q8',
                title='Menu',
                text='歡迎使用我打造的過年實用工具\nPlease select',
                actions=[
                    # PostbackAction(
                    #     label='postback',
                    #     display_text='postback text',
                    #     data='action=buy&itemid=1'
                    # ),
                    MessageAction(
                        label='親戚稱謂查詢&紅包收發',
                        text='親戚稱謂查詢&紅包收發'
                    ),
                    MessageAction(
                        label='紅包管理',
                        text='紅包管理'
                    ),
                    MessageAction(
                        label='產生賀年貼圖',
                        text='產生賀年貼圖'
                    ),
                    MessageAction(
                        label='Document',
                        text='Document'
                    )
                ]
            )
        )
    )

def doc(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://p2.bahamut.com.tw/HOME/creationCover/56/0004385956_B.PNG',
                title='Repository or transition graph?',
                text='Please select',
                actions=[
                    URIAction(
                        label='Repository',
                        uri='https://github.com/tc-huang/TOC-Project-2021'
                    ),
                    URIAction(
                        label='Transition graph',
                        uri='https://fsm-line-bot.herokuapp.com//show-fsm'
                    ),
                    MessageAction(
                        label='回主選單',
                        text='回主選單'
                    ),
                ]
            )
        )
    )

def image(line_bot_api, event):
    text = "顯示隨機三張年長輩圖\n\
            看到看到喜歡的就轉傳吧"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))
    img_list = []

    img_search = {'tbm': 'isch', 'q': "新年+長輩圖"}#event.message.text}
    query = urllib.parse.urlencode(img_search)
    base  = "https://www.google.com/search?"
    url   = str(base+query)

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    res  = urllib.request.Request(url, headers=headers)
    con  = urllib.request.urlopen(res)
    data = con.read()

    pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'

    for match in re.finditer(pattern, str(data, "utf-8")):
        if len(match.group(1)) < 150:
            img_list.append(match.group(1))
    
    for i in range(3):
        random_img_url = img_list[random.randint(0, len(img_list)+1-2)]
        line_bot_api.push_message(
            event.source.user_id,
            ImageSendMessage(random_img_url, random_img_url
            ))
    
    line_bot_api.push_message(
            event.source.user_id,
            TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='再三張 or 回主選單',
                    actions=[
                        MessageAction(
                            label='再三張',
                            text='再三張'
                        ),
                        MessageAction(
                            label='回主選單',
                            text='回主選單'
                        )
                    ]
                )
            )
        )

def money(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='紅包規劃',
                text='Please select',
                actions=[
                    # MessageAction(
                    #     label='紅包收入',
                    #     text='紅包收入'
                    # ),
                    # MessageAction(
                    #     label='紅包支出',
                    #     text='紅包支出'
                    # ),
                    MessageAction(
                        label='查看收入',
                        text='查看收入'
                    ),
                    MessageAction(
                        label='查看支出',
                        text='查看支出'
                    ),
                ]
            )
        )
    )

def relation(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        # thumbnail_image_url='https://example.com/item1.jpg',
                        title='親戚稱謂查詢 & 紅包收發紀錄',
                        text='Please select',
                        actions=[
                            MessageAction(
                                label='爸爸的親戚(含)',
                                text='爸爸的親戚'
                            ),
                            MessageAction(
                                label='媽媽的親戚(含)',
                                text='媽媽的親戚'
                            ),
                            MessageAction(
                                label='回主選單',
                                text='回主選單'
                            )
                        ]
                    ),
                    # CarouselColumn(
                    #     # thumbnail_image_url='https://example.com/item2.jpg',
                    #     title='親戚稱謂查詢 & 紅包收發紀錄',
                    #     text='Please select',
                    #     actions=[
                    #         MessageAction(
                    #             label='老公的親戚(含)',
                    #             text='老公的親戚'
                    #         ),
                    #         MessageAction(
                    #             label='老婆的親戚(含)',
                    #             text='媽媽的親戚'
                    #         ),
                    #             MessageAction(
                    #             label='朋友相關（記帳）',
                    #             text='朋友相關'
                    #         ),
                    #     ]
                    # )
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
                text='Please select (輸入其他鍵回主選單)',
                actions=[
                    MessageAction(
                        label='父母',
                        text='父母'
                    ),
                    MessageAction(
                        label='兄弟姊妹',
                        text='兄弟姊妹'
                    ),
                    MessageAction(
                        label='姪男/女 or 甥男/女',
                        text='姪男/女 or 甥男/女'
                    ),
                    # MessageAction(
                    #     label='祖父母 or 外祖父母',
                    #     text='祖父母 or 外祖父母'
                    # ),
                ]
            )
        )
    )
def f_parents(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你父親的父母',
                text='Please select',
                actions=[
                    MessageAction(
                        label='祖父(爺爺)',
                        text='祖父',
                    ),
                    MessageAction(
                        label='祖母(奶奶)',
                        text='祖母'
                    ),
                    # MessageAction(
                    #     label='其他成員',
                    #     text='其他成員'
                    # ),
                    # MessageAction(
                    #     label='回主選單',
                    #     text='回主選單'
                    # ),
                ]
            )
        )
    )
def f_sibling(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你父親的兄弟姊妹',
                text='Please select',
                actions=[
                    MessageAction(
                        label='伯父（父親的哥哥）',
                        text='伯父',
                    ),
                    MessageAction(
                        label='叔父（父親的弟弟）',
                        text='叔父'
                    ),
                    MessageAction(
                        label='姑母（父親的姊妹）',
                        text='姑母'
                    ),
                ]
            )
        )
    )
def f_nephews(line_bot_api, event):
   line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你父親的姪男/女 or 甥男/女',
                text='Please select',
                actions=[
                    MessageAction(
                        label='堂兄弟姐妹(父親的姪男/女)',
                        text='堂兄弟姐妹',
                    ),
                    MessageAction(
                        label='(姑)表兄弟姐妹(父親的甥男/女)',
                        text='(姑)表兄弟姐妹'
                    ),
                ]
            )
        )
    ) 
who_dict = {}
def dothings(line_bot_api, event, msg):
    global who_dict
    uid = event.source.user_id
    who_dict[uid] = msg
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title=f"{msg} - 紅包收發紀錄 ＆ 賀年貼圖",
                text='Please select',
                actions=[
                    MessageAction(
                        label='收紅包',
                        text='收紅包',
                    ),
                    MessageAction(
                        label='包紅包',
                        text='包紅包'
                    ),
                    MessageAction(
                        label='產生賀年貼圖',
                        text='產生賀年貼圖'
                    ),
                    MessageAction(
                        label='回主選單',
                        text='回主選單'
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
                text='Please select',
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
                    # MessageAction(
                    #     label='祖父母 or 外祖父母',
                    #     text='祖父母 or 外祖父母'
                    # ),
                ]
            )
        )
    )
def m_parents(line_bot_api, event):
   line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你母親的父母',
                text='Please select',
                actions=[
                    MessageAction(
                        label='外祖父(外公)',
                        text='外祖父',
                    ),
                    MessageAction(
                        label='外祖母(外婆)',
                        text='外祖母'
                    ),
                    # MessageAction(
                    #     label='其他成員',
                    #     text='其他成員'
                    # ),
                    # MessageAction(
                    #     label='回主選單',
                    #     text='回主選單'
                    # ),
                ]
            )
        )
    ) 
def m_sibling(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你母親的兄弟姐妹',
                text='Please select',
                actions=[
                    MessageAction(
                        label='舅父（母親的哥哥）',
                        text='舅父',
                    ),
                    MessageAction(
                        label='姨母（母親的姐妹）',
                        text='姨母'
                    ),

                ]
            )
        )
    )
def m_nephews(line_bot_api, event):
     line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='你母親的姪男/女 or 甥男/女',
                text='Please select',
                actions=[
                    MessageAction(
                        label='(舅)表兄弟姐妹(母親的姪男/女)',
                        text='(舅)表兄弟姐妹',
                    ),
                    MessageAction(
                        label='姨兄弟姐妹(母親的甥男/女)',
                        text='姨兄弟姐妹'
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