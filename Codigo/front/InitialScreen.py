from tkinter import *
from PIL import Image, ImageTk



# CODE |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class InitialScreen:
    def __init__(self,root,title,geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
    
    def setInitialOptions(self):

        photo = Image.open("vacpet.png")
        resize = photo.resize((1130,720), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resize)
        label = Label(self.root, image=render)
        #photo = Image.open("vacpet.png")
        #render = ImageTk.PhotoImage(photo)
        #label = Label(self.root, image=render)
        label.image = render
        #label.pack(fill=BOTH, expand=1)
        label.pack()
        label.place(relx=0,rely=0)

        center_frame = Frame(self.root,relief = "solid", background="white",bg='white')   # Criando Frame
        center_frame.pack() # Adicionando o frame ao root
        center_frame.place(relx=0.5, rely=0.5, anchor="c")

        btn_Login = Button(center_frame, width = 15, text="Login", command=self.login, font=("Italic", 32), relief="solid",bg='white')
        btn_Register = Button(center_frame, width=15, text="Register",command = self.login, font=("Italic", 32), relief="solid",bg='white')
        #lbl_ForgotPassword = Label(center_frame, text="I forgot the password", font=("Italic", 16))
        #espaco = Label(center_frame,pady=15,background="white")
        espaco = Label(center_frame,pady=15,bg='white')
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
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Define a transparent color
#root.wm_attributes("-transparentcolor", 'grey')
st = InitialScreen( root, "guei", "1095x720")
st.setInitialOptions()
st.start()

