from tkinter import *


# CODE |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class InitialScreen:
    def __init__(self,root,title,geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
    
    def setInitialOptions(self):
        center_frame = Frame(self.root, width = 300, height = 720,background = "red")   # Criando Frame 
        center_frame.pack(side = BOTTOM) # Adicionando o frame ao root

        btn_Login = Button(center_frame,width = 150, height = 10, text = "Login",command = self.login)
        btn_Register = Button(center_frame,width = 150, height = 10, text = "Register",command = self.login)
        lbl_ForgotPassword = Label(center_frame, text = "I forgot the password",width = 150, height = 10)

        btn_Login.pack()
        btn_Register.pack()
        lbl_ForgotPassword.pack()

    
    def login(self):
        pass
    def forgotPass(self):
        print("Se fudeo")

    def start(self):
        self.root.mainloop()    # Iniciar screen



root = Tk()
st = InitialScreen( root, "guei", "1080x720")
st.setInitialOptions()
st.start()
