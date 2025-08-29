from tkinter import *
import threading
from solver import solver


root= Tk()
root.title("SUDOKU SOLVER")
root.geometry("526x700")
root.configure(bg="#dc92eb")
root.resizable(False,False)

label = Label(root,text="Sudoku Solver",font=("Arial",34,"bold"),bg="#dc92eb")
label.place(x=0,y=10, width=526)

label1 = Label(root,text="",fg="#ff0011",bg="#8cc4e9",font=("TkDefaultFont",14,"bold"),relief=GROOVE)
label1.place(x=0,y=92,width=526)

cells={}

def ValidateNumber(P):
    out = (P.isdigit() or P=="") and len(P)<2
    return out

reg = root.register(ValidateNumber)

def drawGrid():
    frame=Frame(root)
    frame.place(x=42, y=151,width=441,height=441)
    font=("TkTextFont",14,"bold")

    for i in range(9):
        for j in range(9):
            entry=Entry(frame,bg="#f6c5c5",fg="#000000",font=font,borderwidth=3,
                        highlightbackground="#F200FF",highlightthickness=2,relief=RIDGE,
                        justify="center",validate="key",validatecommand=(reg,"%P"))
            entry.place(x=i*49,y=j*49,width=48,height=48)
            cells[(j+2,i+1)]=entry
                      
    for b in range(3,9,3):
        y=b*49
        Frame(frame,bg="#23A8F5",height=3,width=441).place(x=0,y=y-1)

    for b in range(3,9,3):
        x=b*49
        Frame(frame,bg="#23A8F5",width=3,height=441).place(x=x-1,y=0)


def clearValues():
    label1.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")


def getValues():
    board = []
    label1.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            rows.append(int(val) if val != "" else 0)
        board.append(rows)

    # run solver in background to avoid freezing UI
    threading.Thread(target=lambda: _solve_worker(board), daemon=True).start()


def _solve_worker(board):
    try:
        sol = solver(board)
    except Exception as e:
        import traceback
        traceback.print_exc()
        root.after(0, lambda: label1.configure(text="Solver error (see console)"))
        return
    

        
    if sol != "no":
        def show_solution():
            for r in range(2, 11):
                for c in range(1, 10):
                    cells[(r, c)].delete(0, "end")
                    cells[(r, c)].insert(0, sol[r - 2][c - 1])
            label1.configure(text="Sudoku Solved")
        root.after(0, show_solution)
    else:
        root.after(0, lambda: label1.configure(text="No solution exists for this sudoku"))



btn = Button(root, command=getValues, text="Solve",font="TkDefaultFont 14 bold",width=10,relief=RAISED,bg="#ffea00")
btn.place(x=100,y=620)

btn = Button(root, command=clearValues, text="Clear",font="TkDefaultFont 14 bold",width=10,relief=RAISED,bg="#ffea00")
btn.place(x=300,y=620)

drawGrid()
root.mainloop()