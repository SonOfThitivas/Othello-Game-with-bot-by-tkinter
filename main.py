"""
วิชา Programming Fudamental
รหัสวิชา 010123102
Mini Project: Othello

จัดทำโดย
1) นายกานต์ สุขสมกิจ 6601012620011
2) นายภูวิศ ลือดารา 6601012610113

สาขาวิชา วิศวกรรมคอมพิวเตอร์
ภาควิชา วิศวกรรมไฟฟ้าและคอมพิวเตอร์
คณะ วิศวกรรมศาสตร์
มหาวิทยาลัยเทคโนโลยีพระจอมเกล้า พระนครเหนือ
"""

from tkinter import Label, Button, Tk
import othello

class StartUp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Othello Game")
        self.mode = ""
        self.level_bot = ""
        self.first_bot_turn = ""
        self.level_bot_1 = ""
        self.level_bot_2 = ""
        self.time_select = 1

        self.create_widgets()
        
    def create_widgets(self):
        Label(self.window, text="!!! OTHELLO GAME !!!", font=("Calibri", 36), fg="green").pack()
        Label(self.window, text="เลือกโหมดในการเล่น", font=("Calibri", 24)).pack()
        Button(self.window, text="Player vs Player", font=("Calibri", 24), fg="white", bg="red", command=lambda:self.user_choose("pvp")).pack(pady=5)
        Button(self.window, text="Player vs AI", font=("Calibri", 24), fg="white", bg="blue", command=lambda:self.user_choose("pva")).pack(pady=5)
        Button(self.window, text="AI vs AI", font=("Calibri", 24), fg="white", bg="green", command=lambda:self.user_choose("ava")).pack(pady=5)
        
    def user_choose(self, mode):
        self.mode = mode
        if mode == "pva":
            self.bot_window = Tk()
            self.bot_window.title("Bot Level")
            Label(self.bot_window, text="เลือกระดับความยาก", font=("Calibri", 36)).pack(pady=10)
            Button(self.bot_window, text="Easy", font=("Calibri", 24), fg="white", bg="green", command=self.easy).pack(pady=5)
            Button(self.bot_window, text="Normal", font=("Calibri", 24), fg="black", bg="yellow", command=self.normal).pack(pady=5)
            Button(self.bot_window, text="Hard", font=("Calibri", 24), fg="white", bg="red", command=self.hard).pack(pady=5)
            self.bot_window.mainloop()
        
        elif mode == "ava":
            self.bot_window = Tk()
            self.bot_window.title("Bot")
            Label(self.bot_window, text="เลือกบอท", font=("Calibri", 36)).pack(pady=10)
            Button(self.bot_window, text="Karn's AI vs Puwit's AI", font=("Calibri", 24), bg="#FF66FF", command=self.puwit_karn_bot_wn).pack(pady=5, padx=5)
            Button(self.bot_window, text="Level vs Level", font=("Calibri", 24), bg="light blue", command=self.select_bot_level_wn).pack(pady=5)
            self.bot_window.mainloop()
            
        else:
            self.window.destroy()
    
    def easy(self, i=None):
        if i == None:
            self.level_bot = "easy"
            self.bot_window.destroy()   
            self.window.destroy()
        elif i == 1:
            self.level_bot_1 = "easy"
            self.time_select += 1
            self.lb.config(text="เลือกระดับความยากของบอทตัวแรก Player 2 (black)")
        elif i == 2:
            self.level_bot_2 = "easy"
            self.bot_window.destroy()   
            self.level_bot_wn.destroy()
            self.window.destroy()
            
    def normal(self, i=None):
        if i == None:
            self.level_bot = "normal"
            self.bot_window.destroy()
            self.window.destroy()
        elif i == 1:
            self.level_bot_1 = "normal"
            self.time_select += 1
            self.lb.config(text="เลือกระดับความยากของบอทตัวแรก Player 2 (black)")
        elif i == 2:
            self.level_bot_2 = "normal"
            self.bot_window.destroy()   
            self.level_bot_wn.destroy()
            self.window.destroy()
            
    def hard(self, i=None):
        if i == None:
            self.level_bot = "hard"    
            self.bot_window.destroy()
            self.window.destroy()
        elif i == 1:
            self.level_bot_1 = "hard"
            self.time_select += 1
            self.lb.config(text="เลือกระดับความยากของบอทตัวแรก Player 2 (black)")
        elif i == 2:
            self.level_bot_2 = "hard"
            self.bot_window.destroy()   
            self.level_bot_wn.destroy()
            self.window.destroy()
            
        
    def first_pick(self, who_bot=None):
        if who_bot != None:
            self.first_bot_turn = who_bot 
            self.wn.destroy()  
            self.bot_window.destroy()
            self.window.destroy()
        else:
            pass
    
    def puwit_karn_bot_wn(self):
        self.wn = Tk()
        self.wn.title("Bot select")
        Label(self.wn, text="เลือกบอทตัวแรก Player 1 (white)", font=("Calibri", 36)).pack(pady=10)
        Button(self.wn, text="Karn's AI", font=("Calibri", 24), bg="#FF66FF", command=lambda:self.first_pick("Karn's AI")).pack(pady=5)
        Button(self.wn, text="Puwit's AI", font=("Calibri", 24), bg="light blue", command=lambda:self.first_pick("Puwit's AI")).pack(pady=5)
        self.wn.mainloop() 
        
    def select_bot_level_wn(self):
        self.level_bot_wn = Tk()
        self.level_bot_wn.title("Bot level")
        self.lb = Label(self.level_bot_wn, text="เลือกระดับความยากของบอทตัวแรก Player 1 (white)", font=("Calibri", 36))
        self.lb.pack(pady=10)
        Button(self.level_bot_wn, text="Easy", font=("Calibri", 24), fg="white", bg="green", command=lambda:self.easy(self.time_select)).pack(pady=5)
        Button(self.level_bot_wn, text="Normal", font=("Calibri", 24), fg="black", bg="yellow", command=lambda:self.normal(self.time_select)).pack(pady=5)
        Button(self.level_bot_wn, text="Hard", font=("Calibri", 24), fg="white", bg="red", command=lambda:self.hard(self.time_select)).pack(pady=5)
        self.level_bot_wn.mainloop()
    
    def start_window(self):
        self.window.mainloop()

if __name__ == "__main__":
    while True:
        start_up = StartUp()
        start_up.start_window()
        mode = start_up.mode
        bot_level = start_up.level_bot
        first_bot_turn = start_up.first_bot_turn
        level_bot_1 = start_up.level_bot_1
        level_bot_2 = start_up.level_bot_2
        
        if mode == "pvp":
            game = othello.Othello_board()
            game.start_game()

        elif mode == "pva" and bot_level != "":
            game = othello.Othello_board(is_pva=True, bot_level=bot_level)
            game.start_game()
            
        elif mode == "ava" and first_bot_turn != "":
            game = othello.Othello_board(first_bot_turn=first_bot_turn, is_ava=True)
            game.start_game()
        
        elif mode == "ava" and level_bot_1 != "" and level_bot_2 != "":
            game = othello.Othello_board(bot_level_1=level_bot_1, bot_level_2=level_bot_2, is_ava=True)
            game.start_game()
            
        break