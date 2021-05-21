import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

LARGEFONT =("Italic", 32)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self,width=1000,height=600) 
        container.grid_propagate(False)
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Menu, Login, Cadastrar):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # Menu, Login, Cadastrar respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Menu)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.winfo_toplevel().geometry("")


  
# first window frame Menu
  
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Abrindo Imagem
        photo = Image.open("login.jpg")
        # Arrumando Tamanho
        resize = photo.resize((1030,600), Image.ANTIALIAS)
        # Criando a imagem
        render = ImageTk.PhotoImage(resize)
        # Inserindo a imagem no label
        label = ttk.Label(self, image=render)
        # Setando imagem do label com imagem criada
        label.image = render
        # Colocando label no frame
        label.pack()
        # Centralizando
        label.place(relx=0,rely=0)


        button1 = tk.Button(self, text="Login", font= LARGEFONT, relief="solid",background="white", command=lambda : controller.show_frame(Login))
        button2 = tk.Button(self, text="Cadastrar", font= LARGEFONT, relief="solid",background="white",command =lambda : controller.show_frame(Cadastrar))

        button1.place(x=500, y=250,anchor="center")
        button2.place(x=500, y=375,anchor="center")
         
  
          
  
  
# second window frame Login
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photo = Image.open("login.jpg")
        # Arrumando Tamanho
        resize = photo.resize((1030,600), Image.ANTIALIAS)
        # Criando a imagem
        render = ImageTk.PhotoImage(resize)
        # Inserindo a imagem no label
        label = ttk.Label(self, image=render)
        # Setando imagem do label com imagem criada
        label.image = render
        # Colocando label no frame
        label.pack()
        # Centralizando
        label.place(relx=0,rely=0)

        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(Menu),font=("Italic", 14), relief="solid",background="white")
        btn_voltar.place(x=25,y=25)

        lbl_email = tk.Label(self, width = 20, text="email:", font=("Italic", 16))
        lbl_senha = tk.Label(self, width = 20, text="senha:", font=("Italic", 16))


        ent_email = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_senha = tk.Entry(self, width = 40, relief="solid",bg='white')
        
        space = tk.Canvas(self, width = 40, height=10)
        btn_enviar = tk.Button(self, width = 10, text="Login",command = lambda:self.ent_verification(ent_email,ent_senha), font=("Italic", 14), relief="solid",bg='white')


        lbl_email.place(x=500, y=225,anchor="center")
        ent_email.place(x=500, y=250,anchor="center")
        lbl_senha.place(x=500, y=275,anchor="center")
        ent_senha.place(x=500, y=300,anchor="center")

        btn_enviar.place(x=500, y=450,anchor="center")

    def ent_verification(self,email,senha):
        data = []
        data.append(str(email.get()))
        data.append(str(senha.get()))
        resp = False

        cad=tk.Tk()

        if data[0] == "" or data[0]==" ":
            lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, seu email não foi inserido.", font=("Italic", 13))
            btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 10), relief="solid",bg='white')
            resp = True
            lbl_Alert.pack()
            btn_enviar.pack()

        else: 
            if data[1] == "" or data[1]==" ":
                lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, sua senha não foi inserida.", font=("Italic", 13))
                btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 10), relief="solid",bg='white')
                resp = True
                lbl_Alert.pack()
                btn_enviar.pack()
            else:
                lbl_Alert = tk.Label(cad, width = 50, text="Tudo Certo, Confirme para Prosseguir", font=("Italic", 13))
                btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 10), relief="solid",bg='white')
                resp = True
                lbl_Alert.pack()
                btn_enviar.pack()


  
  
  
  
# third window frame Cadastrar
class Cadastrar(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        photo = Image.open("login.jpg")
        # Arrumando Tamanho
        resize = photo.resize((1030,600), Image.ANTIALIAS)
        # Criando a imagem
        render = ImageTk.PhotoImage(resize)
        # Inserindo a imagem no label
        label = ttk.Label(self, image=render)
        # Setando imagem do label com imagem criada
        label.image = render
        # Colocando label no frame
        label.pack()
        # Centralizando
        label.place(relx=0,rely=0)

        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(Menu),font=("Italic", 14), relief="solid",background="white")
        btn_voltar.place(x=25,y=25)

        lbl_nome = tk.Label(self, width = 20, text="Nome:", font=("Italic", 16))
        lbl_email = tk.Label(self, width = 20, text="email:", font=("Italic", 16))
        lbl_senha = tk.Label(self, width = 20, text="senha:", font=("Italic", 16))

        ent_nome = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_email = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_senha = tk.Entry(self, width = 40, relief="solid",bg='white')
        
        btn_enviar = tk.Button(self, width = 10, text="Cadastre-se",command = lambda:self.ent_verification(self,ent_nome,ent_email,ent_senha), font=("Italic", 14), relief="solid",bg='white')

        lbl_nome.place(x=500, y=150,anchor="center")
        ent_nome.place(x=500, y=175,anchor="center")
        lbl_email.place(x=500, y=200,anchor="center")
        ent_email.place(x=500, y=225,anchor="center")
        lbl_senha.place(x=500, y=250,anchor="center")
        ent_senha.place(x=500, y=275,anchor="center")
        
        btn_enviar.place(x=500, y=450,anchor="center")
    
    def ent_verification(self,cadastro,nome,email,senha):
        data = []
        data.append(str(nome.get()))
        data.append(str(email.get()))
        data.append(str(senha.get()))
        resp = False


        cad = tk.Tk()
        cad.wm_attributes("-topmost", True)
        cad.title("Cadastro")
        cad.geometry("395x120")



        if data[0] == "" or data[0]==" ":
            lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, seu nome não foi inserido.", font=("Italic", 13))
            resp = True
        elif data[1] == "" or data[1]==" ":
            lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, seu email não foi inserido.", font=("Italic", 13))
            resp = True
        elif data[2] == "" or data[2]==" ":
            lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, sua senha não foi inserida.", font=("Italic", 13))
            resp = True
        elif resp==False: 
            lbl_Alert = tk.Label(cad, width = 50, text="Cadastro realizado!", font=("Italic", 14))    


        space = tk.Canvas(cad, width = 40, height=10)
        btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 14), relief="solid",bg='white')
        lbl_Alert.pack()
        space.pack()
        btn_enviar.pack()
  
  
# Driver Code
app = tkinterApp()
app.mainloop()