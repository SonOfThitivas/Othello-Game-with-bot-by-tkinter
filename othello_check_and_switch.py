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

class Calculate:
    """
    ------------------------------------these functions below are the functions that check where the buttons can play------------------------------------------------------
    """
    def check_on_below(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        for row in range(btn_row+1,8): # loop to the next button
            if buttons[row][btn_col]["image"] == base or buttons[row][btn_col]["image"] == red_dot or buttons[row][btn_col]["image"] == player_disk:
                break # stop row loop
            elif buttons[row][btn_col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                for row_to_red_dot in range(row+1,8): # continue the loop to the next button
                    if buttons[row_to_red_dot][btn_col]["image"] == red_dot or buttons[row_to_red_dot][btn_col]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop row_to_red_dot loop
                    elif buttons[row_to_red_dot][btn_col]["image"] == opposite_disk: # ignore opposite disks
                        continue # skip to the next loop
                    elif buttons[row_to_red_dot][btn_col]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[row_to_red_dot][btn_col]["image"] = red_dot # That's mean player can play here.
                        buttons[row_to_red_dot][btn_col].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop row_to_red_dot loop
                break # stop row loop
            
    def check_on_above(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        for row in range(btn_row-1,-1,-1): # loop to the next button
            if buttons[row][btn_col]["image"] == base or buttons[row][btn_col]["image"] == red_dot or buttons[row][btn_col]["image"] == player_disk:
                break # stop row loop
            elif buttons[row][btn_col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                for row_to_red_dot in range(row-1,-1,-1): # continue the loop to the next button
                    if buttons[row_to_red_dot][btn_col]["image"] == red_dot or buttons[row_to_red_dot][btn_col]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop row_to_red_dot loop
                    elif buttons[row_to_red_dot][btn_col]["image"] == opposite_disk: # ignore opposite disks
                        continue # skip to the next loop
                    elif buttons[row_to_red_dot][btn_col]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[row_to_red_dot][btn_col]["image"] = red_dot # That's mean player can play here.
                        buttons[row_to_red_dot][btn_col].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop row_to_red_dot loop
                break # stop row loop
    
    def check_on_right(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        for col in range(btn_col+1,8): # loop to the next button
            if buttons[btn_row][col]["image"] == base or buttons[btn_row][col]["image"] == red_dot or buttons[btn_row][col]["image"] == player_disk:
                break # stop row loop
            elif buttons[btn_row][col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                for col_to_red_dot in range(col+1,8): # continue the loop to the next button
                    if buttons[btn_row][col_to_red_dot]["image"] == red_dot or buttons[btn_row][col_to_red_dot]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop col_to_red_dot loop
                    elif buttons[btn_row][col_to_red_dot]["image"] == opposite_disk: # ignore opposite disks
                        continue # skip to the next loop
                    elif buttons[btn_row][col_to_red_dot]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[btn_row][col_to_red_dot]["image"] = red_dot # That's mean player can play here.
                        buttons[btn_row][col_to_red_dot].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop col_to_red_dot loop
                break # stop row loop
            
    def check_on_left(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        for col in range(btn_col-1,-1,-1): # loop to the next button
            if buttons[btn_row][col]["image"] == base or buttons[btn_row][col]["image"] == red_dot or buttons[btn_row][col]["image"] == player_disk:
                break # stop row loop
            elif buttons[btn_row][col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                for col_to_red_dot in range(col-1,-1,-1): # continue the loop to the next button
                    if buttons[btn_row][col_to_red_dot]["image"] == red_dot or buttons[btn_row][col_to_red_dot]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop col_to_red_dot loop
                    elif buttons[btn_row][col_to_red_dot]["image"] == opposite_disk: # ignore opposite disks
                        continue # skip to the next loop
                    elif buttons[btn_row][col_to_red_dot]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[btn_row][col_to_red_dot]["image"] = red_dot # That's mean player can play here.
                        buttons[btn_row][col_to_red_dot].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop col_to_red_dot loop
                break # stop row loop
            
    def check_on_below_right(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        # row and column variables to loop the next button    
        row = btn_row+1
        col = btn_col+1
        # while loop because there are two variables increase or decrease together 
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something or nothing there, that cannot do anything.
                break # stop while loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                while (row >= 0 and row < 8) and (col >= 0 and col < 8): # continue the loop to the next button
                    if buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop col loop
                    elif buttons[row][col]["image"] == opposite_disk: # ignore opposite disks
                        # increase ofr decrease row and column for the next buttons
                        row += 1
                        col += 1
                        continue # skip to the next loop
                    elif buttons[row][col]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[row][col]["image"] = red_dot # That's mean player can play here.
                        buttons[row][col].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop nested while loop
                break # stop while loop
            
    def check_on_below_left(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        # row and column variables to loop the next button    
        row = btn_row+1
        col = btn_col-1
        # while loop because there are two variables increase or decrease together 
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something or nothing there, that cannot do anything.
                break # stop while loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                while (row >= 0 and row < 8) and (col >= 0 and col < 8): # continue the loop to the next button
                    if buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop col loop
                    elif buttons[row][col]["image"] == opposite_disk: # ignore opposite disks
                        # increase ofr decrease row and column for the next buttons
                        row += 1
                        col -= 1
                        continue # skip to the next loop
                    elif buttons[row][col]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[row][col]["image"] = red_dot # That's mean player can play here.
                        buttons[row][col].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop nested while loop
                break # stop while loop
            
    def check_on_above_right(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        # row and column variables to loop the next button    
        row = btn_row-1
        col = btn_col+1
        # while loop because there are two variables increase or decrease together 
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something or nothing there, that cannot do anything.
                break # stop while loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                while (row >= 0 and row < 8) and (col >= 0 and col < 8): # continue the loop to the next button
                    if buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop col loop
                    elif buttons[row][col]["image"] == opposite_disk: # ignore opposite disks
                        # increase ofr decrease row and column for the next buttons
                        row -= 1
                        col += 1
                        continue # skip to the next loop
                    elif buttons[row][col]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[row][col]["image"] = red_dot # That's mean player can play here.
                        buttons[row][col].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop nested while loop
                break # stop while loop
    
    def check_on_above_left(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons, player_choose):
        # row and column variables to loop the next button    
        row = btn_row-1
        col = btn_col-1
        # while loop because there are two variables increase or decrease together 
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something or nothing there, that cannot do anything.
                break # stop while loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's opposite disk, player probably take that disk
                while (row >= 0 and row < 8) and (col >= 0 and col < 8): # continue the loop to the next button
                    if buttons[row][col]["image"] == red_dot or buttons[row][col]["image"] == player_disk: # if there is other place something, that cannot do anything.
                        break # stop col loop
                    elif buttons[row][col]["image"] == opposite_disk: # ignore opposite disks
                        # increase ofr decrease row and column for the next buttons
                        row -= 1
                        col -= 1
                        continue # skip to the next loop
                    elif buttons[row][col]["image"] == base: # if it's clear to play. There is no any disks or red dots
                        buttons[row][col]["image"] = red_dot # That's mean player can play here.
                        buttons[row][col].bind("<Button-1>", player_choose) # define event when click to call player_choose function
                        break # stop nested while loop
                break # stop while loop
    """
    ---------------------------------------------------------------- End --------------------------------------------------------------------
    """
    
    
    """
    ----------------------------- These functions below are the functions when player click the button. The function will switch the opposite disks to the player disks----------------------------
    """
    # all fuctions that work to switch disks  
    def switch_on_below(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = [] # collect row and column of the buttons that will be switched
        for row in range(btn_row+1,8): # loop to the next buttons
            if buttons[row][btn_col]["image"] == base or buttons[row][btn_col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop
            elif buttons[row][btn_col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((row, btn_col)) # add to the collector
                continue # continue the loop
            elif buttons[row][btn_col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop
                
    def switch_on_above(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = [] # collect row and column of the buttons that will be switched
        for row in range(btn_row-1,-1,-1):
            if buttons[row][btn_col]["image"] == base or buttons[row][btn_col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop
            elif buttons[row][btn_col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((row, btn_col)) # add to the collector
                continue # continue the loop
            elif buttons[row][btn_col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop
        
    def switch_on_right(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = [] # collect row and column of the buttons that will be switched
        for col in range(btn_col+1,8):
            if buttons[btn_row][col]["image"] == base or buttons[btn_row][col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop
            elif buttons[btn_row][col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((btn_row, col)) # add to the collector
                continue # continue the loop
            elif buttons[btn_row][col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop
        
    def switch_on_left(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = [] # collect row and column of the buttons that will be switched
        for col in range(btn_col-1,-1,-1):
            if buttons[btn_row][col]["image"] == base or buttons[btn_row][col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop
            elif buttons[btn_row][col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((btn_row, col)) # add to the collector
                continue # continue the loop
            elif buttons[btn_row][col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop
            
    def switch_on_below_right(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = [] # collect row and column of the buttons that will be switched
        row = btn_row +1 
        col = btn_col +1
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((row, col)) # add to the collector
                # increase ofr decrease row and column for the next buttons
                row += 1
                col += 1
                continue # continue the loop
            elif buttons[row][col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop
            
    def switch_on_below_left(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = []
        row = btn_row+1
        col = btn_col-1
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop
            elif buttons[row][col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((row, col)) # add to the collector
                # increase ofr decrease row and column for the next buttons
                row += 1
                col -= 1
                continue # continue the loop
            elif buttons[row][col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop 

    def switch_on_above_right(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = []
        row = btn_row-1
        col = btn_col+1
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range:
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop 
            elif buttons[row][col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((row, col)) # add to the collector
                # increase ofr decrease row and column for the next buttons
                row -= 1
                col += 1
                continue # continue the loop
            elif buttons[row][col]["image"] == player_disk:
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop 
            
    def switch_on_above_left(self, btn_row, btn_col, base, red_dot, player_disk, opposite_disk, buttons):
        collector = []
        row = btn_row-1
        col = btn_col-1
        while (row >= 0 and row < 8) and (col >= 0 and col < 8): # beware if row or column are out of range:
            if buttons[row][col]["image"] == base or buttons[row][col]["image"] == red_dot: # if it's base or red dot, it cannot continue a function
                break # stop the loop 
            elif buttons[row][col]["image"] == opposite_disk: # if it's the opposite disk, funciton will collect row and column of the opposite disk.
                collector.append((row, col)) # add to the collector
                # increase ofr decrease row and column for the next buttons
                row -= 1
                col -= 1
                continue # continue the loop
            elif buttons[row][col]["image"] == player_disk: # if it's player disk, it means the end.
                for r,c in collector: # the loop for switch all the opposite disks that are collected to the player disk.
                    buttons[r][c]["image"] = player_disk # switch
                break # stop the loop 
    """
    -------------------------------------------------------------------- End ------------------------------------------------------------
    """