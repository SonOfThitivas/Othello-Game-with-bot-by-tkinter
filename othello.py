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

from tkinter import Label, Tk, Frame, PhotoImage, Button, Scrollbar, Text, StringVar, IntVar
from othello_check_and_switch import * # contain game calculate funciton
import bot_karn, bot_puwit # import bot class
import time, os, sys 
from pathlib import Path # for universal path ref: พงษ์จันทร์ จันทร์แจ่ม

class Othello_board:
    def __init__(self, bot_level=None, bot_level_1=None, bot_level_2=None, first_bot_turn=None, is_pva=False, is_ava=False):  
        print("initalize")
        # initialize bot
        self.is_ava = is_ava
        self.is_pva = is_pva
        self.first_bot_turn = first_bot_turn
        self.bot_level = bot_level
        self.bot_level_1 = bot_level_1
        self.bot_level_2 = bot_level_2
        self.bot_karn = bot_karn.Bot(bot_level=self.bot_level, bot_level_1=self.bot_level_1, bot_level_2=self.bot_level_2, is_pva=self.is_pva, is_ava=self.is_ava)
        self.bot_puwit = bot_puwit.Bot()
        
        # call calculate class
        self.caluclate = Calculate()
        
        # call tkinter class
        self.window = Tk()
        self.window.title("Othello Game")
        
        self.window.config(bg="#FAB8FF") # background color
        self.buttons = [[None for r in range(8)] for c in range(8)]
        
        # refer to image files
        """
        PhotoImage seem like it takes image variables to string follow the order.
        If you print(self.base), it is "pyimage1".
        The other variables are the same follow the order.
        If you configure button attribute to image, you have to use variable.
        But, if you use it for condition, you have to use string to refer the image.
        """
        self.base = PhotoImage(file=Path("image")/"base.png") # pyimage1"
        self.white_disk = PhotoImage(file=Path("image")/"white_disk.png") # "pyimage2"
        self.black_disk = PhotoImage(file=Path("image")/"black_disk.png") # "pyimage3"
        self.red_dot = PhotoImage(file=Path("image")/"red_dot.png") # "pyimage4"
        # variables
        self.turn_color = "white" # start with white turn
        self.player = {"white":"player 1", "black":"player 2"} # color of that turn to player
        self.player_disk = {"black":"pyimage3", "white":"pyimage2"} # color refer to image
        self.switch_color = {"white":"black", "black":"white"} # to switch color
        self.turn_color_display = StringVar(value="white") # display color of player
        self.player_display = StringVar(value="player 1") # display on the game 
        self.turn_count = 0 # how many time do players play
        self.level_color = {"easy":"green", "normal":"#FEFFD1", "hard":"red"}
        self.is_continue_play = False
        self.is_game_over = False
        # time
        self.time_running = 0 # time count then convert to hour:minute:second
        self.time_display = StringVar(value="00:00:00") # display time as hour:minute:second
        # disks
        self.black_disk_count = IntVar(value=0)
        self.white_disk_count = IntVar(value=0)
        
        # function called
        self.create_widgets() # create widgets
        self.time_ticking() # start time counting
        self.init_game_start() # initialize first disks place
        self.window.after(500, self.turn_check_to_red_dot) # game start
        
    def create_widgets(self):
        # background color
        self.frame_left = Frame(self.window, bg="#FAB8FF")
        self.frame_right = Frame(self.window, bg="#FAB8FF")
        
        # frame right
        self.bot_frame_display = Frame(self.frame_right, bg="#FAB8FF")
        
        if self.is_ava:
            if self.first_bot_turn == "Karn's AI":
                Label(self.bot_frame_display, text="AI player 1: Karn's AI", font=("Calibri", 24), bg="#FAB8FF", fg="#860E86").grid(row=0, column=0, padx=1, pady=5)
                Label(self.bot_frame_display, text="|", font=("Calibri", 24), bg="#FAB8FF", fg="#9F3A00").grid(row=0, column=1, padx=1, pady=5)
                Label(self.bot_frame_display, text="AI player 2: Puwit's AI", font=("Calibri", 24), bg="#FAB8FF", fg="blue").grid(row=0, column=2, padx=1, pady=5)
            elif self.first_bot_turn == "Puwit's AI":
                Label(self.bot_frame_display, text="AI player 1: Puwit's AI", font=("Calibri", 24), bg="#FAB8FF", fg="blue").grid(row=0, column=0, padx=1, pady=5)
                Label(self.bot_frame_display, text="|", font=("Calibri", 24), bg="#FAB8FF", fg="#9F3A00").grid(row=0, column=1, padx=1, pady=5)
                Label(self.bot_frame_display, text="AI player 2: Karn's AI", font=("Calibri", 24), bg="#FAB8FF", fg="#860E86").grid(row=0, column=2, padx=1, pady=5)
            elif self.bot_level_1 != None and self.bot_level_2 != None:     
                Label(self.bot_frame_display, text=f"AI player 1: {self.bot_level_1}", font=("Calibri", 24), bg="#FAB8FF", fg=self.level_color[self.bot_level_1]).grid(row=0, column=0, padx=1, pady=5)
                Label(self.bot_frame_display, text="|", font=("Calibri", 24), bg="#FAB8FF", fg="#9F3A00").grid(row=0, column=1, padx=1, pady=5)
                Label(self.bot_frame_display, text=f"AI player 2: {self.bot_level_2}", font=("Calibri", 24), bg="#FAB8FF", fg=self.level_color[self.bot_level_2]).grid(row=0, column=2, padx=1, pady=5)
            
        elif self.is_pva:
            Label(self.bot_frame_display, text=f"AI's level: {self.bot_level}", font=("Calibri", 24), bg="#FAB8FF", fg=self.level_color[self.bot_level]).pack(padx=5, pady=5)
            
        self.bot_frame_display.pack()
        Label(self.frame_right, text="ตำแหน่งที่ได้เล่นแล้ว", font=("Calibri", 24), bg="#FAB8FF").pack()
        self.frame_history = Frame(self.frame_right)
        self.scroll_bar = Scrollbar(self.frame_history) # ref: https://www.askpython.com/python-modules/tkinter/tkinter-text-widget-tkintscrollbar
        self.scroll_bar.pack(side="right", fill='y') # ref: https://www.geeksforgeeks.org/scrollable-frames-in-tkinter/
        self.history_area = Text(self.frame_history, font=("Calibri", 16), width=30, height=20, state="disabled", padx=5, pady=5, yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.history_area.yview)
        self.history_area.pack()
        self.frame_history.pack()
        
        # frame left
        self.frame_upper = Frame(self.frame_left)
        self.frame_middle = Frame(self.frame_left)
        self.frame_lower = Frame(self.frame_left)
        
        # upper frame
        # turn display
        self.frame_turn = Frame(self.frame_upper, highlightthickness=2, highlightbackground=self.turn_color)
        Label(self.frame_turn, text="Turn:", font=("Calibri", 24)).grid(row=0, column=0)
        Label(self.frame_turn, textvariable=self.player_display, font=("Calibri", 24), width=7).grid(row=0, column=1)
        Label(self.frame_turn, textvariable=self.turn_color_display, font=("Calibri", 24), width=7).grid(row=0, column=2)
        
        # time display
        self.frame_time = Frame(self.frame_upper, highlightthickness=2, highlightbackground="red")
        Label(self.frame_time, text="Time: ", font=("Calibri", 24)).grid(row=0, column=0)
        Label(self.frame_time, textvariable=self.time_display, font=("Calibri", 24)).grid(row=0, column=1)
        
        # count disks in the board
        self.frame_disk = Frame(self.frame_upper, highlightthickness=2, highlightbackground="green")
        Label(self.frame_disk, text="White:", font=("Calibri", 24)).grid(row=0, column=0)
        Label(self.frame_disk, textvariable=self.white_disk_count, font=("Calibri", 24), width=3).grid(row=0, column=1)
        Label(self.frame_disk, text="Black:", font=("Calibri", 24)).grid(row=0,column=2)
        Label(self.frame_disk, textvariable=self.black_disk_count, font=("Calibri", 24), width=3).grid(row=0, column=3)
        
        # gird frame
        self.frame_turn.grid(row=0,column=0, padx=5, pady=5)
        self.frame_time.grid(row=0,column=1,padx=10, pady=5)
        self.frame_disk.grid(row=0,column=2, padx=5, pady=5)
        
        # middle frame
        self.frame_row = Frame(self.frame_middle)
        self.frame_col = Frame(self.frame_middle)
        self.frame_board = Frame(self.frame_middle)
        # adding Label column A - H
        char = 65 # A, H = 72
        for col in range(8):
             Label(self.frame_col, text=str(chr(char)), font=("Calibri", 24)).grid(row=0, column=col, padx=16)
             char += 1
             
        # adding Label row 1-8
        for rw in range(8):
            Label(self.frame_row, text=str(rw+1), font=("Calibri", 24)).grid(row=rw, column=0, pady=5)
        
        # button widgets adding
        for rw in range(8):
            for cl in range(8): 
                self.buttons[rw][cl] = Button(self.frame_board, image=self.base)
                self.buttons[rw][cl].grid(row=rw, column=cl)
        # now there are buttons
        
        # grid frame
        self.frame_col.grid(row=0, column=1)
        self.frame_row.grid(row=1, column=0, padx=5)
        self.frame_board.grid(row=1, column=1)
        
        # background color
        for widget in self.frame_left.winfo_children():
            widget.configure(background="#FAB8FF")
            for frame in widget.winfo_children():
                frame.configure(background="#FAB8FF")
                for little_frame in frame.winfo_children():
                    little_frame.configure(background="#FAB8FF")
                    
        # lower frame
        self.new_game_btn = Button(self.frame_lower, text="New game", font=("Calibri", 24), bg="#FAFF99", command=self.new_game_func)
        self.re_start_btn  =Button(self.frame_lower, text="Restart", font=("Calibri", 24), bg="#8FFF84", command=self.restart_func)
        self.new_game_btn.grid(row=0,column=0, padx=5, pady=5)
        self.re_start_btn.grid(row=0,column=1, padx=5, pady=5)
        if self.is_ava:
            self.re_start_btn.configure(state="disabled") # wait until game over
        
        # pack frame
        self.frame_upper.pack(ipadx=5, ipady=5)
        self.frame_middle.pack(pady=10, ipadx=5, ipady=5)
        self.frame_lower.pack(ipadx=5, ipady=5)
        
        # grid frame left right
        self.frame_left.grid(row=0, column=0, pady=5)
        self.frame_right.grid(row=0, column=1, pady=5)
                
    def init_game_start(self):
        base = "pyimage1" # green base
        red_dot = "pyimage4" # red point
        self.buttons[3][3].configure(image=self.black_disk)
        self.buttons[4][4].configure(image=self.black_disk)
        self.buttons[3][4].configure(image=self.white_disk)
        self.buttons[4][3].configure(image=self.white_disk)
        self.clear_red_dot_count_disk_unbind(red_dot, base) # count disks
        
    def time_ticking(self): # ref: https://www.studytonight.com/python-howtos/how-to-convert-seconds-to-hours-minutes-and-seconds-in-python
        converted = time.strftime("%H:%M:%S", time.gmtime(self.time_running)) # convert seconds to hour:minute:second
        self.time_display.set(converted) # change time display
        self.time_running += 1
        self.after_code = self.window.after(1000, self.time_ticking) # after 1 second repeat this function
        
    def turn_check_to_red_dot(self):
        base = "pyimage1" # green base
        red_dot = "pyimage4" # red point
        player_disk = self.player_disk[self.turn_color] # refer to player disk image code
        opposite_disk = self.player_disk[self.switch_color[self.turn_color]] # refer to opposite disk image code
        red_dot_count = 0
        base_count = 0
        
        # call all button widgets
        for btn in self.frame_board.winfo_children():
            # if it is player disk
            if btn["image"] == player_disk: 
                # find row and column
                for row in range(8):
                    if btn in self.buttons[row]:
                        col = self.buttons[row].index(btn)
                        break
                # check to tell player where there can play
                self.caluclate.check_on_below(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_above(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_right(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_left(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_below_right(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_below_left(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_above_right(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)
                self.caluclate.check_on_above_left(row, col, base, red_dot, player_disk, opposite_disk, self.buttons, self.player_choose)

        # stop time if game over ref: https://stackoverflow.com/questions/9776718/how-do-i-stop-tkinter-after-function, https://stackoverflow.com/questions/25702094/tkinter-after-cancel-in-python
        for btn in self.frame_board.winfo_children():
            if btn["image"] == red_dot:
                red_dot_count += 1
            if btn["image"] == base:
                base_count += 1

        # game over check
        if red_dot_count == 0: 
            if self.is_continue_play or base_count == 0: # Did it switch and 
                self.is_game_over = True
                self.re_start_btn.configure(state="normal")
                self.window.after_cancel(self.after_code)
                self.win_conclusion()
                return 0 # stop function on belo
            elif base_count != 0:
                self.is_continue_play = True
                # switch player's turn
                self.turn_color = self.switch_color[self.turn_color] # switch player turn
                self.turn_color_display.set(self.turn_color) # display next player turn
                self.player_display.set(self.player[self.turn_color])
                self.frame_turn.config(highlightbackground=self.turn_color) # change color bordor
                self.turn_check_to_red_dot()   
                return 0 # stop function on below   
        else:
            self.is_continue_play = False
        
        print(self.turn_count, self.turn_color)
        if (self.is_pva and self.turn_color == "black") or self.is_ava and not(self.is_game_over): # bot plays
            self.bot_play()
        
        # self.is_continue_play = False
        
    def player_choose(self, event=None):
        self.turn_count += 1 # +1 turn play
        base = "pyimage1"
        red_dot = "pyimage4"
        col_to_char = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'} # take column position to alphabet
        player_disk = self.player_disk[self.turn_color] # take color to disk
        opposite_disk = self.player_disk[self.switch_color[self.turn_color]] # take color to disk
        
        button_clicked = event.widget # refer to a button that was pressed
        button_clicked.configure(image=player_disk) # check that button to player disk

        # find row and column of the button
        for row in range(8):
            if button_clicked in self.buttons[row]:
                col = self.buttons[row].index(button_clicked)
                break
        # call function to switch opposite disks
        self.caluclate.switch_on_below(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_above(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_right(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_left(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_below_right(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_below_left(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_above_right(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        self.caluclate.switch_on_above_left(row, col, base, red_dot, player_disk, opposite_disk, self.buttons)
        
        # unbind every buttons, turn red point to green base, count amout black/white disk
        self.clear_red_dot_count_disk_unbind(red_dot, base)
        
        # position display
        self.history_area.configure(state="normal")
        self.history_area.insert("end",f"ตาที่:{self.turn_count} {self.player[self.turn_color]}: row:{row+1}, column:{col_to_char[col]}\n")
        self.history_area.configure(state="disabled")
        self.history_area.see("end") # focus on the latest history ref: https://stackoverflow.com/questions/30669015/autoscroll-of-text-ascrollbar-in-python-text-box
        
        # switch player's turn
        self.turn_color = self.switch_color[self.turn_color] # switch player turn
        self.turn_color_display.set(self.turn_color) # display next player turn
        self.player_display.set(self.player[self.turn_color])
        self.frame_turn.config(highlightbackground=self.turn_color) # change color bordor

        if (self.is_pva and self.turn_color == "black") or self.is_ava: # if player plays with bot and it black color
            self.window.after(500, self.turn_check_to_red_dot)
        else:
            self.turn_check_to_red_dot() # recall function
    
    def clear_red_dot_count_disk_unbind(self, red_dot, base):
        # unbind every buttons, turn red point to green base, count amout black/white disk
        black_disks = 0
        white_disks = 0
        for btn in self.frame_board.winfo_children(): # loop all buttons
            btn.unbind("<Button-1>")
            if btn["image"] == red_dot:
                btn["image"] = base
            # counting black/white disks
            if btn["image"] == self.player_disk["black"]:
                black_disks += 1
                self.black_disk_count.set(black_disks)
            elif btn["image"] == self.player_disk["white"]:
                white_disks += 1
                self.white_disk_count.set(white_disks)
        
                
    def new_game_func(self): # ref: https://stackoverflow.com/questions/41655618/restart-program-tkinter
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    def restart_func(self): # ref: พงษ์จันทร์ จันทร์แจ่ม
        self.window.after_cancel(self.after_code)
        # reset important variable
        self.turn_color = "white" # start with white turn
        self.frame_turn.configure(highlightbackground=self.turn_color)
        self.turn_color_display.set("white") # display white turn
        self.player_display.set("player 1") # displaye player 1
        self.turn_count = 0 # reset time that played
        self.is_continue_play = False
        self.is_game_over = False
        if self.is_ava:
            self.re_start_btn.configure(state="disabled")
        # deletee all history that played
        self.history_area.configure(state="normal")
        self.history_area.delete("1.0","end") 
        self.history_area.configure(state="disabled")
        # time
        self.time_running = 0 # reset time
        self.time_display.set("00:00:00") # reset time display
        # disks
        self.black_disk_count.set(0) # reset all black disks count
        self.white_disk_count.set(0) # reset all white disks     count
        # clear buttons
        for row in range(8):
            for col in range(8):
                self.buttons[row][col].configure(image=self.base, state="normal") # clear all disks and red dots
        
        # recall function
        self.time_ticking() # start time counting
        self.init_game_start() # initialize first disks place
        self.window.after(500, self.turn_check_to_red_dot) # game start
        
    def win_conclusion(self): # game over
        win_col_wn = Tk() # new window
        win_col_wn.title("Conclusion")
        # get all disks count
        black_disk = self.black_disk_count.get()
        white_disk = self.white_disk_count.get()
        # check who wins
        if black_disk > white_disk:
            winner = "The winner is Player 2"
        elif white_disk > black_disk:
            winner = "The winner is Player 1"
        else:
            winner = "Draw"
            
        frame_upper = Frame(win_col_wn)
        frame_lower = Frame(win_col_wn)
        
        # upper frame
        Label(frame_upper, text="!!! GAME OVER !!!", font=("Calibri", 36), fg="green").pack()
        Label(frame_upper, text=winner, font=("Calibri", 36)).pack()
        
        # lower frame
        Label(frame_lower, text="White(player 1):", font=("Calibri", 24)).grid(row=0,column=0,padx=5,pady=5)
        Label(frame_lower, text=str(white_disk), font=("Calibri", 24)).grid(row=0,column=1,padx=5,pady=5)
        Label(frame_lower, text="Black(player 2):", font=("Calibri", 24)).grid(row=0,column=2,padx=5,pady=5)
        Label(frame_lower, text=str(black_disk), font=("Calibri", 24)).grid(row=0,column=3,padx=5,pady=5)
        Label(frame_lower, text="Time:", font=("Calibri", 24)).grid(row=1,column=1,pady=5)
        Label(frame_lower, text=self.time_display.get(), font=("Calibri", 24)).grid(row=1,column=2,pady=5)
        
        # pack
        frame_upper.pack()
        frame_lower.pack()
        Button(win_col_wn, text="Close", font=("Calibri", 24), fg="white", bg="blue", command=win_col_wn.destroy).pack(pady=5)
    
    def bot_play(self): # ref: https://stackoverflow.com/questions/23839982/is-there-a-way-to-press-a-button-without-touching-it-on-tkinter-python
        red_dot = "pyimage4" # red dot image for condition
        opposite_disk = self.player_disk[self.switch_color[self.turn_color]]
        
        if self.first_bot_turn == "Puwit's AI":
            if self.turn_color == "white":
                self.bot_puwit.bot_play(self.buttons, self.frame_board, red_dot)
            else:
                self.bot_karn.bot_play(self.buttons, self.frame_board, red_dot, opposite_disk, self.turn_color)

        elif self.first_bot_turn == "Karn's AI":
            if self.turn_color == "white":
                self.bot_karn.bot_play(self.buttons, self.frame_board, red_dot, opposite_disk, self.turn_color)
            else:
                self.bot_puwit.bot_play(self.buttons, self.frame_board, red_dot)
        else:
            self.bot_karn.bot_play(self.buttons, self.frame_board, red_dot, opposite_disk, self.turn_color)
      
    def start_game(self): 
        self.window.mainloop()