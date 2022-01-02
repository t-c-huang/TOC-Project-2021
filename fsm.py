from transitions.extensions import GraphMachine
from utils import send_text_message
import Template as tpl
import Message as Msg
import state_and_transition as sat

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_menu(self,line_bot_api, event, machine):
        if machine.state == "begin":
            # machine.go_menu()
            tpl.menu(line_bot_api, event)
            return True
        elif machine.state == "dothings":
            msg = event.message.text
            if msg == "回主選單":
                tpl.menu(line_bot_api, event)
                return True
        return False
    def is_going_relation(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "親戚稱謂查詢&紅包收發":
            # machine.go_relation()
            tpl.relation(line_bot_api, event)
            return True
        return False
    
    def is_going_money(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "紅包規劃":
            # machine.go_money()
            tpl.money(self,line_bot_api, event)
            return True
        return False
    
    def is_going_image(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "拜年長輩圖":
            # machine.go_image()
            tpl.image(line_bot_api, event)
            return True
        return False
    
    def is_going_document(self,line_bot_api, event, machine):    
        msg = event.message.text 
        if msg == "Document":
            # machine.go_document()
            tpl.doc(line_bot_api, event)
            return True
        return False
    
    def more_image(self,line_bot_api, event, machine):
        msg = event.message.text 
        if msg == "再三張":
            tpl.image(line_bot_api, event)
            return True
        return False
        
    def is_back_menu(self,line_bot_api, event, machine):
        msg = event.message.text 
        if msg == "回主選單":
            tpl.menu(line_bot_api, event)
            return True
        return False
    
    def is_going_fathers_family(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "爸爸的親戚":
            tpl.fathers_family(line_bot_api, event)
            return True
        return False
    
    def is_going_mothers_family(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "媽媽的親戚":
            tpl.mothers_family(line_bot_api, event)
            return True
        return False
    
    def is_going_f_parents(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "父母":
            tpl.f_parents(line_bot_api, event)
            return True
        return False
    
    def is_going_f_siblings(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "兄弟姊妹":
            tpl.f_sibling(line_bot_api, event)
            return True
        return False
    
    def is_going_f_nephews(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "姪男/女 or 甥男/女":
            tpl.f_nephews(line_bot_api, event)
            return True
        return False

    def is_going_m_parents(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "父母":
            tpl.m_parents(line_bot_api, event)
            return True
        return False
    
    def is_going_m_siblings(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "兄弟姐妹":
            tpl.m_sibling(line_bot_api, event)
            return True
        return False
    
    def is_going_m_nephews(self,line_bot_api, event, machine):
        msg = event.message.text
        if msg == "姪男/女 or 甥男/女":
            tpl.m_nephews(line_bot_api, event)
            return True
        return False

    def is_going_dothings(self,line_bot_api, event, machine):
        msg = event.message.text
        source_states = ["祖父", "祖母", '伯父', '叔父', '姑母', '堂兄弟姐妹', '(姑)表兄弟姐妹', '舅父', '姨母', '外祖父', '外祖母', '(舅)兄弟姐妹', '姨兄弟姐妹']
        if msg in source_states:
            tpl.dothings(line_bot_api, event)
            return True
        return False
    
    # def is_going_to_state1(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state1"

    # def is_going_to_state2(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state2"

    # def on_enter_state1(self, event):
    #     print("I'm entering state1")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state1")
    #     self.go_back()

    # def on_exit_state1(self):
    #     print("Leaving state1")

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")
