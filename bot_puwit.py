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

from random import randint,choice

class Bot:    
    def bot_play(self, buttons, frame_board, red_dot):
        self.ava_bot_pooh(buttons, frame_board, red_dot)

    def ava_bot_pooh(self, buttons, frame_board,red_dot):
        playable_row=[]
        playable_column=[]
        for btn in frame_board.winfo_children():
            if btn["image"] == red_dot:
                # find row, column
                for row in range(8):
                    if btn in buttons[row]:
                        col = buttons[row].index(btn)
                        playable_row.append(row)
                        playable_column.append(col)  
                        break
                    
        random_playstyle=randint(1,2)
        print("random_playstyle", random_playstyle)
        if random_playstyle == 1:    
            index=randint(0,len(playable_row)-1)
            row=playable_row[index]
            col=playable_column[index]

            buttons[row][col].event_generate("<Button-1>")
            buttons[row][col].event_generate("<ButtonRelease-1>")
        
        else:
            min_row = min(playable_row)
            max_row = max(playable_row)
            min_col = min(playable_column)
            max_col = max(playable_column)
            rand = choice([min_row, max_row, min_col, max_col])
            
            # find a pair of row and column
            if rand == min_row:
                row = min_row
                index = playable_row.index(row)
                col = playable_column[index]
            elif rand == max_row:
                row = max_row
                index = playable_row.index(row)
                col = playable_column[index]
            elif rand == min_col:
                col = min_col
                index = playable_column.index(col)
                row = playable_row[index]
            elif rand == max_col:
                col = max_col
                index = playable_column.index(col)
                row = playable_row[index]
            # press the button
            buttons[row][col].event_generate("<Button-1>")
            buttons[row][col].event_generate("<ButtonRelease-1>")