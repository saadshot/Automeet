import tkinter as tk

window = tk.Tk()
window.title("automeet notification")
window.rowconfigure(10, minsize=400, weight=1)
window.columnconfigure(0, minsize=400, weight=1)
message = tk.Label(text="AUTOMEET WILL NOW EXECUTE\nSTAY AWAY FROM KEYBOARD AND MOUSE AFTER BUTTON CLICK", master=window,justify=tk.CENTER)
button = tk.Button(
    text="CLICK BUTTON IF UNDERSTOOD",
    width=25,
    height=5,
    bg="blue",
    fg="white",
    command=window.destroy
)
message.grid(row=10, column=0)
button.grid(row=11, column=0)
def handle_click(event):
    print("user input understood")
button.bind("<Button-1>", handle_click)

def display_window():
	tk.mainloop()
display_window()