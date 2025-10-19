import customtkinter as ctk
import tkinter as tk

root=ctk.CTk()
root.geometry('1300x600')
root.resizable(True, True)
root.title("Unit Converter")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

main_frame=ctk.CTkFrame (root,width=1300, height=600)
main_frame.pack(padx=10,pady=10)
main_frame.grid_columnconfigure((0,1,2,3,4,5),weight=1)
main_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)

display= ctk.CTkFrame(main_frame,fg_color="cyan", width=1260, height=200)
display.grid(column=0, columnspan=6, row=1, rowspan=3, padx=10, pady=(5,10))

option_panel=ctk.CTkFrame(main_frame, fg_color='black',width=1260,height=30)
option_panel.grid(column=0, columnspan=6, row=0, padx=10, pady=(10,5))


root.mainloop()