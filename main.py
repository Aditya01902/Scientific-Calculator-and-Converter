import customtkinter as ctk

root= ctk.CTk()
root.geometry("1000x600")
root.resizable(True,True)
root.title("Scientific Calculator")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#MainFrame

main_frame=ctk.CTkFrame(root)
main_frame.grid(row=0, column=0,padx=10, pady=10, sticky="nsew")

main_frame.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
main_frame.grid_columnconfigure((0,1,2),weight=1)

#Display Window
display_window=ctk.CTkFrame(main_frame)
display_window.grid(row=1,column=0,rowspan=2, padx=5, sticky="nsew", columnspan=2, pady=(5,0))


#History Window
history_window=ctk.CTkFrame(main_frame)
history_window.grid(row=1, column=2, rowspan=8, padx=5, pady=5, sticky="nsew")

#operations Window
operation_window=ctk.CTkFrame(main_frame)
operation_window.grid(row=3,column=0, rowspan=5, columnspan=2, padx=5, pady=5, sticky="nsew")
root.mainloop()