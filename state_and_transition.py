state_system = ["begin", "menu", "relation", "money", "income", "expense"]

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
    {"trigger": "go_money","source": "menu","dest": "money"},
    {"trigger": "income","source": "money","dest": "income"},
    {"trigger": "expense","source": "money","dest": "expense"},
    # {"trigger": "back","source": state_fathers_family,"dest": "relation"},
    # {"trigger": "back","source": state_mothers_family,"dest": "relation"},
    # {"trigger": "back","source": state_sons_family,"dest": "relation"},
    # {"trigger": "back","source": state_daughters_family,"dest": "relation"},
]