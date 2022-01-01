from transitions.extensions import GraphMachine

from utils import send_text_message



state_system = ["begin", "menu", "relation"]


#   father's family
state_fathers_family = ["爸爸", "祖父/祖母（爺爺/奶奶）", "叔父/伯父(叔母/伯母)", "姑姑(姑丈)","堂兄弟姊妹", "（姑）表兄弟姊妹",
                        "曾祖父/曾祖母", "曾外祖父/曾外祖母", "叔祖父/伯祖父（叔祖母/伯祖母）","姑祖母/姑祖父", "舅祖父/舅祖母",
                        "姨祖母/姨祖父", "(姑)表叔/伯父/(姑)表姑母", "(舅)表叔/伯父/(舅)表姑母"]
transition_fathers_family = [
        {"trigger": "advance","source": "relation","dest": "爸爸"},
        {"trigger": "advance","source": "爸爸","dest": "祖父/祖母（爺爺/奶奶）"},
        {"trigger": "advance","source": "爸爸","dest": "曾祖父母"},
        {"trigger": "advance","source": "爸爸","dest": "叔父/伯父(叔母/伯母)"},
        {"trigger": "advance","source": "爸爸","dest": "曾外祖父母"},
        {"trigger": "advance","source": "爸爸","dest": "姑姑(姑丈)"},
        {"trigger": "advance","source": "爸爸","dest": "堂兄弟姊妹"},
        {"trigger": "advance","source": "爸爸","dest": "（姑）表兄弟姊妹"},
        {"trigger": "advance","source": "爸爸","dest": "曾祖父/曾祖母"},
        {"trigger": "advance","source": "爸爸","dest": "曾外祖父/曾外祖母"}, 
        {"trigger": "advance","source": "爸爸","dest": "叔祖父/伯祖父（叔祖母/伯祖母）"}, 
        {"trigger": "advance","source": "爸爸","dest": "姑祖母/姑祖父"}, 
        {"trigger": "advance","source": "爸爸","dest": "舅祖父/舅祖母"}, 
        {"trigger": "advance","source": "爸爸","dest": "姨祖母/姨祖父"}, 
        {"trigger": "advance","source": "爸爸","dest": "(姑)表叔/伯父/(姑)表姑母"}, 
        {"trigger": "advance","source": "爸爸","dest": "(舅)表叔/伯父/(舅)表姑母"},  
]

#   mother's family
state_mothers_family = ["媽媽", "外祖父/外祖母", "舅父（舅母）", "姨母（姨父）", "(舅)表兄弟姊妹",
                        "姨兄弟姊妹", "外曾祖父/外曾祖母","外曾外祖父/外曾外祖母","叔外祖父/伯外祖父", "叔外祖母/伯外祖母",
                        "姑外祖母/姑外祖父", "舅外祖父/舅外祖母", "姨外祖母/姨外祖父", "(姑)表舅父/(姑)表姨母"]

transition_mothers_family = [
    {"trigger": "advance","source": "relation","dest": "媽媽"},]

#   son's family
state_sons_family = ["兒子", "媳婦", "孫子/孫女", "孫媳婦", "孫女婿",
                     "曾孫/曾孫女", "曾外孫/曾外孫女", "男媳姻兄弟姐妹","男媳姻男/男媳姻女", "男媳姻婦/男媳姻婿",
                     "男媳姻孫男/女", "男媳姻外孫男/女", "親家公/親家母"]
transition_sons_family = [
    {"trigger": "advance","source": "relation","dest": "兒子"},
]

#   daughter's family
state_daughter_family = ["女兒", "媳婦", "外孫/外孫女", "外孫媳婦", "外孫女婿",
                         "外曾孫/外曾孫女", "外曾外孫/外曾外孫女", "女媳姻兄弟/女媳姻姊妹", "女媳姻男/女媳姻女","女媳姻婦/女媳姻婿"
                         "女媳姻孫/女媳姻孫女", "女媳姻外孫/女媳姻外孫女", "親家公/親家母"]
transition_daughter_family = [
    {"trigger": "advance","source": "relation","dest": "女兒"},
]


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
