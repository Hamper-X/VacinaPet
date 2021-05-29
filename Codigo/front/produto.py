import tkinter as tk
from requests import post,get
from PIL import Image, ImageTk
from tkinter import PhotoImage, Tk, ttk

LARGEFONT =("Italic", 32)

class vetPet(tk.Tk):
    # Global
    token=''
    tokentxt=""
    tokenjson=''
    tokenReg=''
    tokenRegtxt=""
    tokenpet=''
    tokenpettxt=""
     
    # __init__ funcao para claase Tkinter
    def __init__(self, *args, **kwargs):
        
        # __init__ funcao para classe Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # Criando Container
        container = tk.Frame(self,width=1000,height=600) 
        container.grid_propagate(False)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # Inicializando Frames para um array vazio
        self.frames = {}
  
        # Iterando por uma tupla que consiste em diferente layouts
        for F in (Menu, Login, Cadastrar, MenuUsuario, CadastroPet, BuscarPet, BuscarClinica, Relatorio, MostrarPets):
            frame = F(container, self)
            
            # inicializando os frames para cada objeto
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(Menu)
  
    # Exibir o frame passado como parametro
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.winfo_toplevel().geometry("")


  
# Menu
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        # Inicializando Frame com configuracoes contidas em vetPet
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

        # Botoes com acao a realizar caso selecionados
        button1 = tk.Button(self, text="Login", font= LARGEFONT, relief="solid",background="white", command=lambda : controller.show_frame(Login))
        button2 = tk.Button(self, text="Cadastrar", font= LARGEFONT, relief="solid",background="white",command =lambda : controller.show_frame(Cadastrar))

        # Colocando os botoes no Frame
        button1.place(x=500, y=250,anchor="center")
        button2.place(x=500, y=375,anchor="center")
         
  
          
  
  
# Login
class Login(tk.Frame):
    def __init__(self, parent, controller):
        # Inicializando Frame com configuracoes contidas em vetPet
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


        # Botoes com acao a realizar caso selecionados
        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(Menu),font=("Italic", 14), relief="solid",background="white")
        btn_prosseguir = tk.Button(self,width=10,text="Prosseguir",command=lambda:controller.show_frame(MenuUsuario),font=("Italic", 14), relief="solid",background="white")
        btn_enviar = tk.Button(self, width = 10, text="Login",command = lambda:self.ent_verification(ent_email,ent_senha), font=("Italic", 14), relief="solid",bg='white')


        # Colocando os botoes no Frame
        btn_voltar.place(x=25,y=25)
        btn_prosseguir.place(x=440,y=350)
        btn_enviar.place(x=500, y=450,anchor="center")


        # Criando label para identificar as caixas de entrada
        lbl_email = tk.Label(self, width = 20, text="email:", font=("Italic", 16))
        lbl_senha = tk.Label(self, width = 20, text="senha:", font=("Italic", 16))

        # Criando caixas de entrada
        ent_email = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_senha = tk.Entry(self, width = 40, relief="solid",bg='white')
        
        # Colocando labels e entrys no Frame
        lbl_email.place(x=500, y=225,anchor="center")
        ent_email.place(x=500, y=250,anchor="center")
        lbl_senha.place(x=500, y=275,anchor="center")
        ent_senha.place(x=500, y=300,anchor="center")



    # Funcao de verificacao de entradas
    def ent_verification(self,email,senha):
        # Criando uma lista com dados
        data = []
       
        # Passando dados para string e adicionando a lista
        data.append(str(email.get()))
        data.append(str(senha.get()))
        
        # Criando objeto chamado cad no qual abre uma janela e depois de concluido exige que usaurio conclua
        cad=tk.Tk()

        # Testes para cada entrada
        if data[0] == "" or data[0]==" ":
            lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, seu email não foi inserido.", font=("Italic", 13))
            btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 10), relief="solid",bg='white')
            lbl_Alert.pack()
            btn_enviar.pack()

        else: 
            if data[1] == "" or data[1]==" ":
                lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, sua senha não foi inserida.", font=("Italic", 13))
                btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 10), relief="solid",bg='white')
                lbl_Alert.pack()
                btn_enviar.pack()
            else:
                vetPet.token = post("http://127.0.0.1:5000/auth",json={"username": data[0],"password": data[1]})
                vetPet.tokentxt=vetPet.token.text
                vetPet.tokenjson=vetPet.token.json()
                print(vetPet.tokentxt)
                print(vetPet.token)
                print(vetPet.tokenjson["access_token"])
                # pet=get("http://127.0.0.1:5000/api/pet",headers={"Authorization":"JWT {}".format(token.json()["access_token"])})
                # print(pet.text)
                lbl_Alert = tk.Label(cad, width = 50, text="Tudo Certo, Confirme para Prosseguir", font=("Italic", 13))
                btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 10), relief="solid",bg='white')
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
            vetPet.tokenReg=post("http://127.0.0.1:5000/api/cliente",json={"nome": data[0],"email": data[1],"senha":data[2]})
            vetPet.tokenRegtxt=vetPet.tokenReg.text
            print(vetPet.tokenRegtxt)
            lbl_Alert = tk.Label(cad, width = 50, text="Cadastro realizado!", font=("Italic", 14))    


        space = tk.Canvas(cad, width = 40, height=10)
        btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 14), relief="solid",bg='white')
        lbl_Alert.pack()
        space.pack()
        btn_enviar.pack()



class MenuUsuario(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        #Abrindo Imagem
        photo = Image.open("backgroundMenu.jpg")
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

        self.icone1 = PhotoImage(file="iconeAdd.png")
        self.pi1 = self.icone1.subsample(1, 1)
        self.icone2 = PhotoImage(file="iconePesquisaPet.png")
        self.pi2 = self.icone2.subsample(1, 1)
        self.icone3 = PhotoImage(file="iconeClinica.png")
        self.pi3 = self.icone3.subsample(1,1)
        self.icone4 = PhotoImage(file="iconeRelatorio.png")
        self.pi4 = self.icone4.subsample(1,1)
        self.icone5 = PhotoImage(file="iconeLista.png")
        self.pi5 = self.icone5.subsample(1,1)


        btn_CadPet = tk.Button(self,image=self.pi1,width=215, text="Cadastro Animal", command = lambda:controller.show_frame(CadastroPet), font=("Italic", 20), relief="solid",bg='white',compound="top")
        btn_BuscarPet = tk.Button(self, image=self.pi2,width=215, text="Buscar Pet",command = lambda:controller.show_frame(BuscarPet), font=("Italic", 20), relief="solid",bg='white',compound="top")
        btn_BuscarClinica = tk.Button(self, image=self.pi3,width=215, text="Buscar Clinica",command = lambda:controller.show_frame(BuscarClinica), font=("Italic", 20), relief="solid",bg='white',compound="top")
        btn_Relatorio = tk.Button(self, image=self.pi4,width=215, text="Relatório",command = lambda:controller.show_frame(Relatorio), font=("Italic", 20), relief="solid",bg='white',compound="top")
        btn_MostrarPets = tk.Button(self, image=self.pi5,width=215, text="Lista Animais",command = lambda:controller.show_frame(MostrarPets), font=("Italic", 20), relief="solid",bg='white',compound="top")

        btn_CadPet.place(x=275,y=100)
        btn_BuscarPet.place(x=525,y=100)
        btn_BuscarClinica.place(x=275,y=250)
        btn_MostrarPets.place(x=525, y=250)
        btn_Relatorio.place(x=400, y=400)
        


class CadastroPet(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(MenuUsuario),font=("Italic", 14), relief="solid",background="white")
        btn_voltar.place(x=25,y=25)

        lbl_nome = tk.Label(self, width = 30, text="Nome:", font=("Italic", 16))
        lbl_especie = tk.Label(self, width = 30, text="Espécie:", font=("Italic", 16))
        lbl_peso = tk.Label(self, width = 30, text="Peso:", font=("Italic", 16))
        lbl_sexo = tk.Label(self, width = 30, text="Sexo:", font=("Italic", 16))
        lbl_porte = tk.Label(self, width = 30, text="Porte:", font=("Italic", 16))
        lbl_nascimento = tk.Label(self, width = 30, text="Nascimento:", font=("Italic", 16))
        lbl_raca = tk.Label(self, width = 30, text="Raça:", font=("Italic", 16))

        ent_nome = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_especie = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_peso = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_sexo = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_porte = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_nascimento = tk.Entry(self, width = 40, relief="solid",bg='white')
        ent_raca = tk.Entry(self, width = 40, relief="solid",bg='white')
        
        cad = tk.Button(self, width=15, text="Cadastrar", command = lambda:self.cadastra(ent_nome, ent_especie, ent_peso, ent_sexo,ent_porte,ent_nascimento,ent_raca), font=("Italic", 16))

        lbl_nome.pack()
        ent_nome.pack()
        lbl_especie.pack()
        ent_especie.pack()
        lbl_peso.pack()
        ent_peso.pack()
        lbl_sexo.pack()
        ent_sexo.pack()
        lbl_porte.pack()
        ent_porte.pack()
        lbl_nascimento.pack()
        ent_nascimento.pack()
        lbl_raca.pack()
        ent_raca.pack()
        cad.pack()


    def cadastra(self, nome, especie, peso, sexo, porte, nascimento, raca):
        pass
        # data = [] 
        # data.append(str(nome.get()))
        # data.append(str(especie()))
        # data.append(str(peso.get()))
        # data.append(str(sexo.get()))
        # data.append(str(porte.get()))
        # data.append(str(nascimento.get()))
        # data.append(str(raca.get()))
        # resp = False

        # if data[0] == "" or data[0]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, seu nome não foi inserido.", font=("Italic", 13))
        #     resp = True
        # elif data[1] == "" or data[1]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, especie não foi inserida.", font=("Italic", 13))
        #     resp = True
        # elif data[2] == "" or data[2]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, peso não foi inserido.", font=("Italic", 13))
        #     resp = True
        # elif data[3] == "" or data[3]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, sexo não foi inserido.", font=("Italic", 13))
        #     resp = True
        # elif data[4] == "" or data[4]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, porte não foi inserido.", font=("Italic", 13))
        #     resp = True
        # elif data[5] == "" or data[5]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, data de nascimento não foi inserida.", font=("Italic", 13))
        #     resp = True
        # elif data[6] == "" or data[6]==" ":
        #     lbl_Alert = tk.Label(self, width = 50, text="Ocorreu um imprevisto, raça não foi inserida.", font=("Italic", 13))
        #     resp = True
        # elif resp==False: 
        #     tokenReg=post("http://127.0.0.1:5000/api/pet",json={"nome": data[0],"especie": data[1],"peso":data[2], "sexo":data[3], "porte":data[4],"nascimento":data[5],"raca":data[6],"cliente_id":NAOTENHO})
        #     print(tokenReg.text)
        #     lbl_Alert = tk.Label(self, width = 50, text="Cadastro realizado!", font=("Italic", 14))    


        # space = tk.Canvas(self, width = 40, height=10)
        # btn_enviar = tk.Button(self, width = 6, text="OK",command=cad.destroy, font=("Italic", 14), relief="solid",bg='white')
        # lbl_Alert.pack()
        # space.pack()
        # btn_enviar.pack()


class BuscarPet(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        #Abrindo Imagem
        photo = Image.open("backgroundMenu.jpg")
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


        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(MenuUsuario),font=("Italic", 14), relief="solid",background="white")
        lbl_busca = tk.Label(self, width = 40, text="Nome do Animal", font=("Italic", 20))
        ent_busca = tk.Entry(self, width = 40, relief="solid",bg='white')

        btn_voltar.place(x=25,y=25)
        lbl_busca.place(x=185,y=100)
        ent_busca.place(x=375,y=200)

        
        pesquisa = tk.Button(self, width=15, text="Pesquisar", command = lambda:self.pesquisa(ent_busca), font=("Italic", 16),relief="solid",background="white")
        pesquisa.place(x=400,y=400)
        
        if():
            vetPet.tokenpet=get("http://127.0.0.1:5000/api/pet",headers={"Authorization":"JWT {}".format(vetPet.tokenjson)})
            vetPet.tokenpettxt=vetPet.tokenpet.text
            print(vetPet.tokenpettxt)
        




    def pesquisa(self, nome):
        #data = []
        #data.append(str(nome.get()))
        #resp = False

        #if data[0] == "" or data[0]==" ":
        #   lbl_Alert = tk.Label(cad, width = 50, text="Ocorreu um imprevisto, seu nome não foi inserido.", font=("Italic", 13))
        #   resp = True 
        # elif resp==False: 
        #     tokenReg=post("http://127.0.0.1:5000/api/pet",json={"nome": data[0]})
        #     print(tokenReg.text)
        #     lbl_Alert = tk.Label(cad, width = 50, text="Cadastro realizado!", font=("Italic", 14))    


        # space = tk.Canvas(cad, width = 40, height=10)
        # btn_enviar = tk.Button(cad, width = 6, text="OK",command=cad.destroy, font=("Italic", 14), relief="solid",bg='white')
        # lbl_Alert.pack()
        # space.pack()
        # btn_enviar.pack()
           
        pass
        
#class DadosPet(tk.Frame)

class BuscarClinica(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)  

        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(MenuUsuario),font=("Italic", 14), relief="solid",background="white")
        btn_voltar.place(x=25,y=25)
        pass

class Relatorio(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(MenuUsuario),font=("Italic", 14), relief="solid",background="white")
        btn_voltar.place(x=25,y=25)
        pass

class MostrarPets(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        btn_voltar = tk.Button(self,width=10,text="Voltar",command=lambda:controller.show_frame(MenuUsuario),font=("Italic", 14), relief="solid",background="white")
        btn_voltar.place(x=25,y=25)
        pass




# Driver Code
app = vetPet()
app.mainloop()