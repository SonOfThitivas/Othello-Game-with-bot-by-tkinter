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

from random import choice, randint

class Bot:
    def __init__(self, bot_level=None, bot_level_1=None, bot_level_2=None, is_pva=False, is_ava=False):
        self.bot_level = bot_level
        self.bot_level_1 = bot_level_1
        self.bot_level_2 = bot_level_2
        self.is_ava = is_ava
        self.is_pva = is_pva

    """ check bot level and call function """
    def bot_play(self, buttons, frame_board, red_dot, opposite_disk, turn_color):
        if self.is_ava:
            if self.bot_level_1 != None and self.bot_level_2 != None:
                if turn_color == "white":
                    if self.bot_level_1 == "easy":
                        self.easy_bot(buttons, frame_board, red_dot, opposite_disk)
                    elif self.bot_level_1 == "normal":
                        self.normal_bot(buttons, frame_board, red_dot)
                    elif   self.bot_level_1 == "hard":
                        self.hard_bot(buttons, frame_board, red_dot, opposite_disk)     
                else:
                    if self.bot_level_2 == "easy":
                        self.easy_bot(buttons, frame_board, red_dot, opposite_disk)
                    elif self.bot_level_2 == "normal":
                        self.normal_bot(buttons, frame_board, red_dot)
                    elif   self.bot_level_2 == "hard":
                        self.hard_bot(buttons, frame_board, red_dot, opposite_disk)     
                        
            else:
                self.hard_bot(buttons, frame_board, red_dot, opposite_disk)       
                
        elif self.is_pva:    
            if self.bot_level == "easy":
                self.easy_bot(buttons, frame_board, red_dot, opposite_disk)
            elif self.bot_level == "normal":
                self.normal_bot(buttons, frame_board, red_dot)
            elif self.bot_level == "hard":
                self.hard_bot(buttons, frame_board, red_dot, opposite_disk)
    
    """ easy bot function 
    Bot's goal - choose a button than can get point at most.
    """
    def easy_bot(self, buttons, frame_board, red_dot, opposite_disk):        
        collector = [] # to collect row and column
        point_list = [] # to collect only point
        for btn in frame_board.winfo_children(): # loop to take buttons in frame_board with method winfo_children
            if btn["image"] == red_dot:
                # find row, column
                for row in range(8):
                    if btn in buttons[row]:
                        col = buttons[row].index(btn)
                        break
                point = 0
                # below
                point += self.check_below(row, col, buttons, opposite_disk)
                # above
                point += self.check_above(row, col, buttons, opposite_disk)
                # right
                point += self.check_right(row, col, buttons, opposite_disk)
                # left
                point += self.check_left(row, col, buttons, opposite_disk)
                # below right
                point += self.check_below_right(row, col, buttons, opposite_disk)
                # below left
                point += self.check_below_left(row, col, buttons, opposite_disk)
                # above right
                point += self.check_above_right(row, col, buttons, opposite_disk)
                # above left
                point += self.check_above_left(row, col, buttons, opposite_disk)
                """ collector's index is the same as point_list's index"""
                collector.append((row,col))
                point_list.append(point)
                
        """ Take the most point, find index, find row and column, bot presses the button """
        point = max(point_list)
        count = point_list.count(point)
        if count > 1: # if there are the same point moree than 1 position.
            while True: # random the button
                index = randint(0, len(point_list) - 1)
                if point_list[index] == point:
                    break
        else:
            index = point_list.index(point) # find index of point directly
        
        # index of the position of point is the same
        most_point = collector[index]
        row = most_point[0]
        col = most_point[1]
        
        buttons[row][col].event_generate("<Button-1>")
        buttons[row][col].event_generate("<ButtonRelease-1>")
            
    
    def normal_bot(self, buttons, frame_board, red_dot):
        """ normal bot function 
        Bot's goal - random the minimum and maximum row and column.
        """
        # row and col collectoe are the same index
        row_collector = [] # to collect row
        col_collector = [] # to collect column
        for btn in frame_board.winfo_children(): # loop to take buttons in frame_board with method winfo_children
            if btn["image"] == red_dot:
                # find row, column
                for row in range(8):
                    if btn in buttons[row]:
                        col = buttons[row].index(btn)
                        break
                row_collector.append(row)
                col_collector.append(col)   
        """ 
        find the minimum and maximum of row and column.
        random
        take index to press the button that position
        """
        # if len(row_collector) == 0 or len(col_collector) == 0: # If there is nothing
        #     return 0 # stop
        min_row = min(row_collector)
        max_row = max(row_collector)
        min_col = min(col_collector)
        max_col = max(col_collector)
        rand = choice([min_row, max_row, min_col, max_col])
        
        # find a pair of row and column
        if rand == min_row:
            row = min_row
            index = row_collector.index(row)
            col = col_collector[index]
        elif rand == max_row:
            row = max_row
            index = row_collector.index(row)
            col = col_collector[index]
        elif rand == min_col:
            col = min_col
            index = col_collector.index(col)
            row = row_collector[index]
        elif rand == max_col:
            col = max_col
            index = col_collector.index(col)
            row = row_collector[index]
        # press the button
        buttons[row][col].event_generate("<Button-1>")
        buttons[row][col].event_generate("<ButtonRelease-1>")
    
    """  hard bot function 
    Bot's goal - want to capture the edges and the cornors. If it doesn't do, it will take the most point.
    """
    def hard_bot(self, buttons, frame_board, red_dot , opposite_disk):
        pos_point = []
        point_list = []
        flag = False
        for btn in frame_board.winfo_children(): # loop to take buttons in frame_board with method winfo_children
            if btn["image"] == red_dot: 
                # find row, column
                for row in range(8):
                    if btn in buttons[row]:
                        col = buttons[row].index(btn)
                        """ attempt to do not take opposite go to the corner """
                        if ((row == 1) and ((col == 0 or col == 1 or col == 6 or col == 7))) or ((row == 6) and ((col == 0 or col == 1 or col == 6 or col == 7))) or ((col == 1) and ((row == 0 or row == 1 or row == 6 or row == 7))) or ((col == 6) and ((row == 0 or row == 1 or row == 6 or row == 7))):
                            pos_point.append((row,col))
                            point_list.append(0)
                            break
                            """ if it's at the cornors """
                        elif (row == 0 and col == 0) or (row == 0 and col == 7) or (row == 7 and col == 0) or (row == 7 and col == 7): # at some cornors
                            buttons[row][col].event_generate("<Button-1>")
                            buttons[row][col].event_generate("<ButtonRelease-1>")
                            return 0    
                        else:                
                            point = 0
                            # below
                            point += self.check_below(row, col, buttons, opposite_disk)
                            # above 
                            point += self.check_above(row, col, buttons, opposite_disk)
                            # right
                            point += self.check_right(row, col, buttons, opposite_disk)
                            # left
                            point += self.check_left(row, col, buttons, opposite_disk)
                            # below right
                            point += self.check_below_right(row, col, buttons, opposite_disk)
                            # below left
                            point += self.check_below_left(row, col, buttons, opposite_disk)
                            # above right
                            point += self.check_above_right(row, col, buttons, opposite_disk)
                            # above left
                            point += self.check_above_left(row, col, buttons, opposite_disk)
                            """ pos_point's index is the same as point_list's index"""
                            pos_point.append((row, col))
                            point_list.append(point)
                            break
                        

        """ Take the most point, find index, find row and column, bot presses the button """
        point = max(point_list)
        count = point_list.count(point)
        if count > 1: # if there are the same point moree than 1 position.
            while True: # random the button
                index = randint(0, len(point_list) - 1)
                if point_list[index] == point:
                    break
        else:
            index = point_list.index(point) # find index of point directly
        
        # index of the position of point is the same
        most_point_pos = pos_point[index]
        row = most_point_pos[0]
        col = most_point_pos[1]
        
        buttons[row][col].event_generate("<Button-1>")
        buttons[row][col].event_generate("<ButtonRelease-1>")
    
    """
    These functions below are the function that checks and take points
    """
    def check_below(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        for row_below in range(row+1, 8): # loop to the next buttons
            if buttons[row_below][col]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            else:
                break # stop the loop
        
        return point # return point
        
    def check_above(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        for row_above in range(row-1, -1, -1): # loop to the next buttons
            if buttons[row_above][col]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            else:
                break # stop the loop
        
        return point # return point   

    def check_right(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        for col_right in range(col+1, 8): # loop to the next buttons
            if buttons[row][col_right]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            else:
                break # stop the loop
        
        return point # return point   

    def check_left(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        for col_left in range(col-1, -1, -1):
            if buttons[row][col_left]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            else:
                break # stop the loop
        
        return point # return point  

    def check_below_right(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        while True:
            row += 1
            col += 1
            if not(row > -1 and row < 8) or not(col > -1 and col < 8): # beware if it's out of range 
                break # stop the loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            break # stop the loop
        
        return point # return point  

    def check_below_left(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        while True:
            row += 1
            col -= 1
            if not(row > -1 and row < 8) or not(col > -1 and col < 8): # beware if it's out of range
                break # stop the loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            break # stop the loop
        
        return point # return point  

    def check_above_right(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        while True:
            row -= 1
            col += 1
            if not(row > -1 and row < 8) or not(col > -1 and col < 8): # beware if it's out of range
                break # stop the loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            break # stop the loop
        
        return point # return point  

    def check_above_left(self, row, col, buttons:list, opposite_disk):
        point = 0
        # start to count point
        while True:
            row -= 1
            col -= 1
            if not(row > -1 and row < 8) or not(col > -1 and col < 8): # beware if it's out of range
                break # stop the loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk
                point += 1 # increase 1 point
                continue # skip to the next loop
            break # stop the loop
        
        return point # return point     
    """
    End
    """