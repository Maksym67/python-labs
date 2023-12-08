import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

window = tk.Tk()
window.title("Chat")
window.geometry("400x500")

def send_message():
    message = entry.get()
    if message:
        full_message = f"{name}: {message}"
        client.send(full_message.encode())
        chat_display.insert(tk.END, full_message + "\n")
        log_ui_message(full_message)
        entry.delete(0, tk.END)
    else:
        full_message = ""
        client.send(full_message.encode())

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode()
            chat_display.insert(tk.END, message + "\n")
            log_ui_message(message)
        except ConnectionResetError:
            break

def initialize_chat():
    global name
    name = choose_name.get()
    secondary_window.destroy()
    window.deiconify()
    server_thread = threading.Thread(target=receive_message)
    server_thread.start()

def log_ui_message(message):
    with open("ui_log.txt", 'a') as file:
        file.write(message + '\n')

secondary_window = tk.Toplevel(window)
secondary_window.title("Choose name")
secondary_window.geometry('250x70')

choose_name = tk.Entry(secondary_window, width=15)
choose_name.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

confirm_button = tk.Button(secondary_window, text='Confirm', width=8, command=initialize_chat)
confirm_button.grid(row=2, column=6, padx=12, pady=12, sticky="ew")

chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

entry = tk.Entry(window, width=30)
entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

def send_button_press(event):
    send_button.invoke()

send_button = tk.Button(window, text="Send", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

entry.bind('<Return>', send_button_press)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

window.withdraw()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

window.mainloop()