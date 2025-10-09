import customtkinter as ctk
import tkinter
import unicodeit
root= ctk.CTk()
root.geometry("1000x600")
root.resizable(True,True)
root.title("Scientific Calculator")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#MainFrame

main_frame=ctk.CTkFrame(root, fg_color="black")
main_frame.grid(row=0, column=0,padx=10, pady=10, sticky="nsew")

main_frame.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)
main_frame.grid_columnconfigure((0,1,2,3,4,5,6),weight=1)

#Display Window
display_window=ctk.CTkFrame(main_frame)
display_window.grid(row=1,column=0,rowspan=2, padx=(10,5), sticky="nsew", columnspan=5, pady=(5,0))


#History Window
history_window=ctk.CTkScrollableFrame(main_frame, width=450)
history_window.grid(row=1, column=5,columnspan=2, rowspan=8, padx=5, pady=5, sticky="nsew")

#operations Window
operation_window=ctk.CTkFrame(main_frame, fg_color="black")
operation_window.grid(row=4,column=0, rowspan=4, columnspan=5, padx=(5,10), pady=5, sticky="nsew")
operation_window.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)
operation_window.grid_rowconfigure((0,1,2,3,4,5), weight=1)


#Button Commands
def command_1():
    print("currently under developement !")

def command_2():
    print("currently under developement !")

def command_3():
    print("currently under developement !")

def command_4():
    print("currently under developement !")

def command_5():
    print("currently under developement !")

def command_6():
    print("currently under developement !")

def command_7():
    print("currently under developement !")

def command_8():
    print("currently under developement !")

def command_9():
    print("currently under developement !")

def command_0():
    print("currently under developement !")




#Number Buttons

my_font=("Arial",20,"bold")

button_1=ctk.CTkButton(
    operation_window,
    text="1",
    command=command_1,
    fg_color="grey40",
    font=my_font
)
button_1.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

button_2=ctk.CTkButton(
    operation_window,
    text="2",
    command=command_2,
    fg_color="grey40",
    font=my_font
)
button_2.grid(row=4, column=5, padx=5, pady=5, sticky="nsew")

button_3=ctk.CTkButton(
    operation_window,
    text="3",
    command=command_3,
    fg_color="grey40",
    font=my_font
)
button_3.grid(row=4, column=6, padx=5, pady=5, sticky="nsew")

button_4=ctk.CTkButton(
    operation_window,
    text="4",
    command=command_4,
    fg_color="grey40",
    font=my_font)
button_4.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

button_5=ctk.CTkButton(
    operation_window,
    text="5",
    command=command_5,
    fg_color="grey40",
    font=my_font
)
button_5.grid(row=3, column=5, padx=5, pady=5, sticky="nsew")

button_6=ctk.CTkButton(
    operation_window,
    text="6",
    command=command_6,
    fg_color="grey40",
    font=my_font
)
button_6.grid(row=3, column=6, padx=5, pady=5, sticky="nsew")


button_7=ctk.CTkButton(
    operation_window,
    text="7",
    command=command_7,
    fg_color="grey40",
    font=my_font
)
button_7.grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

button_8=ctk.CTkButton(
    operation_window,
    text="8",
    command=command_8,
    fg_color="grey40",
    font=my_font
)
button_8.grid(row=2, column=5, padx=5, pady=5, sticky="nsew")

button_9=ctk.CTkButton(
    operation_window,
    text="9",
    command=command_9,
    fg_color="grey40",
    font=my_font
)
button_9.grid(row=2, column=6, padx=5, pady=5, sticky="nsew")

button_0=ctk.CTkButton(
    operation_window,
    text="0",
    command=command_0,
    fg_color="grey40",
    font=my_font
)
button_0.grid(row=5, column=5, padx=5, pady=5, sticky="nsew")







### OPERATIONS

#Operational Command
def command_plus():
    print("currently under developement !")

def command_sin():
    print("currently under developement !")

def command_cos():
    print("currently under developement !")

def command_modulus():
    print("currently under developement !")

def command_2nd():
    print("currently under developement !")

#Operation Button

button_2nd=ctk.CTkButton(
    operation_window,
    text="2nd",
    command=command_2nd,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_2nd.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")


button_mr=ctk.CTkButton(
    operation_window,
    text="mr",
    command=command_2nd,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_mr.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")


button_mplus=ctk.CTkButton(
    operation_window,
    text="m+",
    command=command_2nd,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_mplus.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")


button_mc=ctk.CTkButton(
    operation_window,
    text="mc",
    command=command_2nd,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_mc.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

button_e=ctk.CTkButton(
    operation_window,
    text="e",
    command=command_2nd,
    fg_color="gray20",
    font=my_font,
    hover_color="gray12"
)
button_e.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")


button_CE=ctk.CTkButton(
    operation_window,
    text="CE",
    command=command_2nd,
    fg_color="dark blue",
    font=my_font
)
button_CE.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")


button_C=ctk.CTkButton(
    operation_window,
    text="C",
    command=command_2nd,
    fg_color="dark blue",
    font=my_font
)
button_C.grid(row=0, column=6, padx=5, pady=5, sticky="nsew")


button_delete=ctk.CTkButton(
    operation_window,
    text="⌫",
    command=command_2nd,
    fg_color="#B22222",
    font=my_font,
    hover_color="#8B0000"
)
button_delete.grid(row=0, column=7, padx=5, pady=5, sticky="nsew")


button_sin=ctk.CTkButton(
    operation_window,
    text="sin",
    command=command_sin,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_sin.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")


button_cos=ctk.CTkButton(
    operation_window,
    text="cos",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_cos.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")


button_tan=ctk.CTkButton(
    operation_window,
    text="tan",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_tan.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")


button_cot=ctk.CTkButton(
    operation_window,
    text="cot",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_cot.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")


button_leftbracket=ctk.CTkButton(
    operation_window,
    text="(",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_leftbracket.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")


button_rightbracket=ctk.CTkButton(
    operation_window,
    text=")",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_rightbracket.grid(row=1, column=5, padx=5, pady=5, sticky="nsew")


button_percentage=ctk.CTkButton(
    operation_window,
    text="%",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_percentage.grid(row=1, column=6, padx=5, pady=5, sticky="nsew")


button_divide=ctk.CTkButton(
    operation_window,
    text="÷",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_divide.grid(row=1, column=7, padx=5, pady=5, sticky="nsew")


button_xsquare=ctk.CTkButton(
    operation_window,
    text="x\u00b2",
    command=command_cos,
    fg_color="gray20",
    font=my_font, 
    hover_color="gray12"
)
button_xsquare.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")


button_xcube=ctk.CTkButton(
    operation_window,
    text="x\u00b3",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_xcube.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")


button_xToThePowery=ctk.CTkButton(
    operation_window,
    text="x\u02b8",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_xToThePowery.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")


button_eToThePowerx=ctk.CTkButton(
    operation_window,
    text="e\u02e3",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_eToThePowerx.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")


button_multiply=ctk.CTkButton(
    operation_window,
    text="x",
    command=command_cos,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_multiply.grid(row=2, column=7, padx=5, pady=5, sticky="nsew")


button_10powerx=ctk.CTkButton(
    operation_window,
    text="10ˣ",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_10powerx.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")



button_ln=ctk.CTkButton(
    operation_window,
    text="ln",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_ln.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")



button_2powerx=ctk.CTkButton(
    operation_window,
    text="2\u02e3",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_2powerx.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")



button_modulus=ctk.CTkButton(
    operation_window,
    text="|x|",
    command=command_modulus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_modulus.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")



button_plus=ctk.CTkButton(
    operation_window,
    text="+",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_plus.grid(row=4, column=7, padx=5, pady=5, sticky="nsew")


button_deg=ctk.CTkButton(
    operation_window,
    text="Deg",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_deg.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")


button_logbasex=ctk.CTkButton(
    operation_window,
    text="log\u2093",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_logbasex.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")


button_logybasex=ctk.CTkButton(
    operation_window,
    text="log\u2093y",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_logybasex.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")


button_xfactorial=ctk.CTkButton(
    operation_window,
    text="x!",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_xfactorial.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")


button_sign=ctk.CTkButton(
    operation_window,
    text="±",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_sign.grid(row=5, column=4, padx=5, pady=5, sticky="nsew")


button_decimal=ctk.CTkButton(
    operation_window,
    text=".",
    command=command_plus,
    fg_color="grey20",
    font=my_font, 
    hover_color="gray12"
)
button_decimal.grid(row=5, column=6, padx=5, pady=5, sticky="nsew")


button_equals=ctk.CTkButton(
    operation_window,
    text="=",
    command=command_plus,
    font=my_font
)
button_equals.grid(row=5, column=7, padx=5, pady=5, sticky="nsew")



root.mainloop()