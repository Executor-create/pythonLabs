import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class ChatClient:
  def __init__(self, root):
    self.root = root
    self.root.title("Chat")

    self.BG_GRAY = "#ABB2B9"
    self.BG_COLOR = "#17202A"
    self.TEXT_COLOR = "#EAECEE"

    self.root.grid_rowconfigure(1, weight=1)
    self.root.grid_columnconfigure(0, weight=1)

    self.txt = tk.Text(root, bg=self.BG_COLOR, fg=self.TEXT_COLOR, width=60, font=(32))
    self.txt.grid(row=1, column=0, columnspan=2, sticky="nsew")

    self.e = tk.Entry(root, bg="#2C3E50", fg=self.TEXT_COLOR, width=55)
    self.e.grid(row=2, column=0, sticky="ew")

    self.name_label = tk.Label(root, text="Enter your name", width=20,)
    self.name_label.place(relx=0.5, rely=0.4, anchor="center")

    self.name_field = tk.Entry(root, width=30)
    self.name_field.place(relx=0.5, rely=0.5, anchor="center")

    self.stored_name = tk.StringVar()

    self.send_button = tk.Button(root, text="Send", bg=self.BG_GRAY, command=self.send_message)
    self.send_button.grid(row=2, column=1, sticky="ew")

    self.root.grid_rowconfigure(2, weight=1)

    self.name_field.bind("<Return>", self.send_name)
    self.e.bind("<Return>", self.send_message)

    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_address = ('127.0.0.1', 5555)

    try:
      self.client_socket.connect(self.server_address)
    except socket.error as e:
      print(str(e))

    receive_thread = threading.Thread(target=self.receive_messages)
    receive_thread.start()

  def send_name(self, event=None):
    name = self.name_field.get()
    if name:
      self.stored_name.set(name)
      self.name_label.destroy()
      self.name_field.destroy()
      self.send_message("joined the chat!")

  def send_message(self, event=None):
      message = self.e.get().strip()
      if self.stored_name.get() and message:
          full_message = f"{self.stored_name.get()}: {message}"
          self.txt.insert(tk.END, "\n" + full_message)
          self.e.delete(0, tk.END)
          try:
            self.client_socket.send(full_message.encode('utf-8'))
          except Exception as e:
            print(str(e))

  def receive_messages(self):
    while True:
      try:
        data = self.client_socket.recv(1024)
        if not data:
          break
        message = data.decode('utf-8')
        self.update_chat_area(message)
      except Exception as e:
        print(str(e))
        break

  def update_chat_area(self, message):
    self.txt.insert(tk.END, message + '\n')
    self.txt.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    chat_client = ChatClient(root)
    root.mainloop()
