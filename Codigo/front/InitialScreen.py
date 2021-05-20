from tkinter import *
from PIL import Image, ImageTk



# CODE |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class InitialScreen:
    def __init__(self,root,title,geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
    
    def setInitialOptions(self):

        # Descomentar somente quando a luana souber como pegar a imagem no windows
        """photo = Image.open(r"\vacpet.png")
        resize = photo.resize((1130,720), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resize)
        label = Label(self.root, image=render)
        #photo = Image.open("vacpet.png")
        #render = ImageTk.PhotoImage(photo)
        #label = Label(self.root, image=render)
        label.image = render
        #label.pack(fill=BOTH, expand=1)
        label.pack()
        label.place(relx=0,rely=0)"""

        center_frame = Frame(self.root,relief = "solid", background="white",bg='white')   # Criando Frame
        center_frame.pack() # Adicionando o frame ao root
        center_frame.place(relx=0.5, rely=0.5, anchor="c")

        btn_Login = Button(center_frame, width = 15, text="Login", command=self.login, font=("Italic", 32), relief="solid",bg='white')
        btn_Register = Button(center_frame, width=15, text="Register",command = self.register, font=("Italic", 32), relief="solid",bg='white')
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
    
    
    
    def register(self):
        cadastro = Tk()
        cadastro.wm_attributes("-topmost", True)
        cadastro.title("Cadastro")
        cadastro.geometry("395x220")

        lbl_nome = Label(cadastro, width = 30, text="Nome:", font=("Italic", 16))
        lbl_email = Label(cadastro, width = 30, text="email:", font=("Italic", 16))
        lbl_senha = Label(cadastro, width = 30, text="senha:", font=("Italic", 16))

        ent_nome = Entry(cadastro, width = 40, relief="solid",bg='white')
        ent_email = Entry(cadastro, width = 40, relief="solid",bg='white')
        ent_senha = Entry(cadastro, width = 40, relief="solid",bg='white')
        
        space = Canvas(cadastro, width = 40, height=10)
        btn_enviar = Button(cadastro, width = 6, text="Cadastre-se",command = lambda:self.ent_verification(cadastro,ent_nome,ent_email,ent_senha), font=("Italic", 14), relief="solid",bg='white')

        lbl_nome.pack()
        ent_nome.pack()
        lbl_email.pack()
        ent_email.pack()
        lbl_senha.pack()
        ent_senha.pack()
        
        space.pack()
        btn_enviar.pack()
        st.start()
    
    def ent_verification(self,cadastro,nome,email,senha):
        data = []
        data.append(str(nome.get()))
        data.append(str(email.get()))
        data.append(str(senha.get()))
        resp = FALSE


        cad = Tk()
        cad.wm_attributes("-topmost", True)
        cad.title("Cadastro")
        cad.geometry("395x120")



        if data[0] == "" or data[0]==" ":
            lbl_Alert = Label(cad, width = 30, text="ERRO! A aba de nome deve ser preenchida.", font=("Italic", 12))
            resp = TRUE
        if data[1] == "" or data[1]==" ":
            lbl_Alert = Label(cad, width = 30, text="ERRO! A aba de email deve ser preenchida.", font=("Italic", 12))
            resp = TRUE
        if data[2] == "" or data[2]==" ":
            lbl_Alert = Label(cad, width = 30, text="ERRO! A aba de senha deve ser preenchida.", font=("Italic", 12))
            resp = TRUE
        if resp==FALSE: 
            lbl_Alert = Label(cad, width = 30, text="Cadastro realizado!", font=("Italic", 14))    


        space = Canvas(cad, width = 40, height=10)
        btn_enviar = Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 14), relief="solid",bg='white')
        lbl_Alert.pack()
        space.pack()
        btn_enviar.pack()
        st.start()
            
    
    def start(self):
        self.root.mainloop()    # Iniciar screen



root = Tk()
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Define a transparent color
#root.wm_attributes("-transparentcolor", 'grey')
st = InitialScreen( root, "Vacina Pet .Corp", "1095x720")
st.setInitialOptions()
st.start()

