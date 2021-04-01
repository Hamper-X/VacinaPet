from tkinter import *


# CODE |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class InitialScreen:
    def __init__(self,root,title,geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
    
    def setInitialOptions(self):
        center_frame = Frame(self.root,relief = "solid")   # Criando Frame
        center_frame.pack() # Adicionando o frame ao root
        center_frame.place(relx=0.5, rely=0.5, anchor="c")

        btn_Login = Button(center_frame, width = 15, text="Login", command=self.login, font=("Italic", 32), relief="solid")
        btn_Register = Button(center_frame, width=15, text="Register",command = self.login, font=("Italic", 32), relief="solid")
        #lbl_ForgotPassword = Label(center_frame, text="I forgot the password", font=("Italic", 16))
        espaco = Label(center_frame,pady=15)

        # btn_quit = Button(center_frame, text = "Quit",command=self.root.destroy, font=("Italic",12))
        btn_Login.pack()
        espaco.pack()
        btn_Register.pack()
        #lbl_ForgotPassword.pack()
        # btn_quit.pack(ipadx = 100)

    
    def login(self):
        pass
    def forgotPass(self):
        pass
    def start(self):
        self.root.mainloop()    # Iniciar screen



root = Tk()
st = InitialScreen( root, "guei", "1080x720")
st.setInitialOptions()
st.start()








































