import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]] !="":
            for index in combo:
                buttons[index].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            reset_game()
    check_draw()

def check_draw():
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_game()

def but_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        buttons[index].config(fg="blue" if current_player == "X" else "red")
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player, winner
    current_player = "X"
    winner = False
    for button in buttons:
        button.config(text="", bg="lightgray", fg="black")  # Set new background color here
    label.config(text=f"Player {current_player}'s turn")

def on_enter(e):
    e.widget['background'] = 'lightblue'

def on_leave(e):
    e.widget['background'] = 'lightgray'  # Set new background color here

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("Helvetica", 20), width=6, height=3, 
                     bg="lightgray",  # Set initial background color here
                     command=lambda i=i: but_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 16))
label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
