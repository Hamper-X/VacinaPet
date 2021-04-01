from tkinter import *
from tkinter import ttk
import math

control = 0
control2 = 0
raio = 0
position = [0,0,0,0,0]
lista_retas = []
list_in_out = []
geo_trans2d_x = 0
geo_trans2d_y = 0


# Transformações geometricas  |===================================================================================================================
def geometricsTransformation2D(geo_frame,canvas):
    lbl_x = Label(geo_frame, text="1° -> X  |  2° - Y\nRotação: Primeiro valor\nEscala: Primeiro Valor")
    alter_x = Entry(geo_frame,width = 7)
    alter_y = Entry(geo_frame,width = 7)
    btn_send = Button(geo_frame, text = "Enviar Valores",command = lambda:setGeo(alter_x,alter_y))
    lbl_introduction = Label(geo_frame,text="Geometrics Transformation 2D",foreground = "red",width = 15,height = 2, padx = 40 )
    btn_translation = Button(geo_frame,text= "Translação",width = 15,height = 2, padx = 40,command = lambda: translation(canvas))
    btn_rotation = Button(geo_frame,text= "Rotação",width = 15,height = 2, padx = 40,command = lambda:rotation(canvas))
    btn_escalation = Button(geo_frame,text= "Escala",width = 15,height = 2, padx = 40,command = lambda:escala(canvas))
    btn_reflexion = Button(geo_frame,text= "Reflexão",width = 15,height = 2, padx = 40,command = reflection)

    
    
    lbl_introduction.pack()
    btn_translation.pack()
    btn_rotation.pack()
    btn_escalation.pack()
    btn_reflexion.pack()
    lbl_x.pack()
    
    alter_x.pack()
    alter_y.pack()

    btn_send.pack()
def translation(canvas):
    canvas.delete('all')
    for n in lista_retas:
        canvas.create_line(n[0]+geo_trans2d_x,n[1]+geo_trans2d_y,n[2]+geo_trans2d_x+1,n[3]+geo_trans2d_y+1,fill='red')
def escala (canvas):
    clearCanvas(canvas)
    for n in list_in_out:
        canvas.create_line(n[0],n[1],n[2]*geo_trans2d_x,n[3]*geo_trans2d_y, canvas)
def rotation(canvas):
    canvas.delete('all')
    for n in list_in_out:
        x2 = n[2]*math.cos(geo_trans2d_x) - n[3]*math.sin(geo_trans2d_x)
        y2 = n[2]*math.sin(geo_trans2d_x) + n[3]*math.cos(geo_trans2d_x)
        canvas.create_line(n[0],n[1],x2,y2,fill='red')
def reflection():
    pass

# Rasterização |===================================================================================================================
def rasterization(rest_fram,canvas):
    lbl_introduction = Label(rest_fram,text="================| Rasterization |================",foreground = "red",width = 15,height = 2, padx = 40 )
    btn_straight_DDA = Button(rest_fram,text= "Rasterização de Retas\n com DDA", width = 15,height = 2, padx = 40,command = lambda:straightDDA(position[0],position[1],position[2],position[3],canvas))
    btn_stright_Bresenham = Button(rest_fram,text= "Rasterização de Retas\n com Bresenham",width = 15,height = 2, padx = 40,command = lambda:straightBresenham(position[0],position[1],position[2],position[3],canvas))
    btn_circle_Bresenham = Button(rest_fram,text= "Rasterização de circunferencias\n com Bresenham",width = 15,height = 2, padx = 40,command = lambda:circleBresenham(position[0],position[1],position[4],canvas))
    btn_point = Button(rest_fram,text= "Pontinho :3",width = 15,height = 2, padx = 40,command = lambda:makePoint(position[0],position[1],position[2],position[3],canvas))
    
    lbl_introduction.pack()
    btn_straight_DDA.pack()
    btn_stright_Bresenham.pack()
    btn_circle_Bresenham.pack()
    btn_point.pack()
def abs(value):
    if value < 0:
        value = value * (-1)
    return value
def straightDDA(x1,y1,x2,y2,canvas):
    list_in_out.append(x1)
    list_in_out.append(y1)
    list_in_out.append(x2)
    list_in_out.append(y2)
    passos = 0
    dx = x2-x1
    dy = y2-y1
    if abs(dx)>abs(dy):
        passos = abs(dx)
    else:
        passos = abs(dy)
    x_inc = dx/passos
    y_inc = dy/passos
    x = x1
    y = y1
    k=1
    canvas.create_oval(x,y,x+1,y+1,fill='black')
    lista_dda = [x,y,x+1,y+1]
    lista_retas.append(lista_dda)
    while k < passos:
        x = x + x_inc
        y = y + y_inc
        canvas.create_oval(x,y,x+1,y+1,fill='black')
        lista_dda = [x,y,x+1,y+1]
        lista_retas.append(lista_dda)
        k = k+1   
    return 
def straightBresenham(x1,y1,x2,y2,canvas):
    lista_dda = [x1,y1,x2,y2]
    list_in_out.append(lista_dda)
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    p = (2*dy)-dx
    const1 = 2*dy
    const2 = 2*(dy-dx)
    x = x1
    y = y1
    canvas.create_oval(x,y,x+1,y+1,fill='black')
    while(x<x2):
        x=x+1
        if(p<0):
            p = p + const1
        else:
            p = p + const2
            y = y+1
        canvas.create_oval(x,y,x+1,y+1,fill='black')
def plot_circle_points(xc,x,yc,y,canvas):
    canvas.create_oval(xc+x,yc+y,xc+x+1,yc+y+1,fill='black')
    canvas.create_oval(xc-x,yc+y,xc-x+1,yc+y+1,fill='black')
    canvas.create_oval(xc+x,yc-y,xc+x+1,yc-y+1,fill='black')
    canvas.create_oval(xc-x,yc-y,xc-x+1,yc-y+1,fill='black')
    canvas.create_oval(xc+y,yc+x,xc+y+1,yc+x+1,fill='black')
    canvas.create_oval(xc-y,yc+x,xc-y+1,yc+x+1,fill='black')
    canvas.create_oval(xc+y,yc-x,xc+y+1,yc-x+1,fill='black')
    canvas.create_oval(xc-y,yc-x,xc-y+1,yc-x+1,fill='black')
    
    lista_dda = [xc+x,yc+y,xc+x+1,yc+y+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc-x,yc+y,xc-x+1,yc+y+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc+x,yc-y,xc+x+1,yc-y+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc-x,yc-y,xc-x+1,yc-y+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc+y,yc+x,xc+y+1,yc+x+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc-y,yc+x,xc-y+1,yc+x+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc+y,yc-x,xc+y+1,yc-x+1]
    lista_retas.append(lista_dda)
    lista_dda = [xc-y,yc-x,xc-y+1,yc-x+1]
    lista_retas.append(lista_dda)  
def circleBresenham(xc,yc,raio,canvas):
    x = 0
    y = raio
    p = 3-2*raio
    plot_circle_points(xc,x,yc,y,canvas)
    while x<y:
        if p<0 :
            p = p+ (4*x) + 6
        else:
            p = p + 4*(x-y) + 10
            y = y-1
        x = x +1
        plot_circle_points(xc,x,yc,y,canvas)
def makePoint(x1,y1,x2,y2,canvas):
    lista_dda = [x1,y1,x2,y2]
    list_in_out.append(lista_dda)
    canvas.create_oval(x1,y1,x1+2,y1+2,fill='black')


# Recorte |================================================================================================================
def cutout(cut_frame,canvas):
    lbl_introduction = Label(cut_frame,text="==================| Cutout |==================",foreground = "red",width = 15,height = 2, padx = 40 )
    #btn_circle_Cohen = Button(cut_frame,text= "Recorte Codificado Cohen",width = 15,height = 2, padx = 40,command = algorithms.straightDDA)
    btn_circle_Sutherlan = Button(cut_frame,text= "Recorte Codificado\n Cohen Sutherland",width = 15,height = 2, padx = 40,command = cohenSutherland(position[0],position[1],position[2],position[3],canvas))
    btn_circle_liang = Button(cut_frame,text= "Recorte Parametrico Liang",width = 15,height = 2, padx = 40)#,command = algorithms.cirBresenham)
    btn_circle_Barsky = Button(cut_frame,text= "Recorte Parametrico Barsky",width = 15,height = 2, padx = 40)#,command = algorithms.cirBresenham)
    lbl_introduction.pack()
    #btn_circle_Cohen.pack()
    btn_circle_Sutherlan.pack()
    btn_circle_liang.pack()
    btn_circle_Barsky.pack()
def region_code(x,y):
    codigo =0 

    # esquerda -bit 0
    if x<position[0]:
        codigo = codigo +1
    # direita -bit 1
    if x<position[2]:
        codigo=codigo+2
    # baixo -bit 2
    if y<position[1]:
        codigo = codigo +4 
    # cima -bit 3
    if y>position[3]:
        codigo = codigo + 8
    return codigo
# xmin = 0 ymin = 0 /  xmax = 700 ymax = 530
def cohenSutherland(x1,y1,x2,y2,canvas):
    aceite = False
    feito = False
    while not feito:
        c1 = region_code(x1,y1)
        c2 = region_code(x2,y2)
        if c1==0 and c2==0:
            aceite = True
            feito = True
        else:
            if c1 != 0 and c2 != 0:
                feito = True
            else:
                if c1 != 0:
                    cfora = c1
                else:
                    cfora = c2

                if cfora==0:
                    xint = 0
                    yint = y1 + (y2-y1)*(0-x1)/(x2-x1)
                else:
                    if cfora==1: 
                        xint = 700
                        yint = y1 + (y2-y1)*(700-x1)/(x2-x1)
                    else:
                        if cfora ==2:
                            yint = 0
                            xint = x1 + (x2-x1)*(0-y1)/(y2-y1)
                        else:
                            if cfora ==3:
                                yint = 530
                                xint = x1+(x2-x1)*(530-y1)/(y2-y1)

                if c1 == cfora:
                    x1 = xint
                    y1 = yint
                else:
                    x2 = xint
                    y2 = yint
    if aceite==True:
        canvas.create_line(x1,y1,x2,y2)
 


# FUNCTIONS |==============================================================================================================

# Get Mouse position 
def getMousePosition(event):
    global control
    if control == 0:
        position[0] = int(event.x)
        position[1] = int(event.y)
        control = control + 1
    else:
        position[2] = int(event.x)
        position[3] = int(event.y)
        print(position[0],position[1],position[2],position[3]) 
        control = 0 
# Montagem dos frames
def makeFrams(root):
    glob_frame = Frame(root)                                                    # Fram Global
    glob_frame.pack()
    frame_button = Frame(glob_frame, width = 200, height = 680)      # Frame Botoes
    frame_button.pack(side = LEFT)

    frame_action = Frame(glob_frame, width = 700, height = 680)     # Frame Canvas+opções
    frame_action.pack(side = LEFT)

    frame_canv= Frame(frame_action, width = 700, height = 560, bg= 'black')     # Alocação do Canvas
    frame_canv.pack(side = TOP)
    canvas = showCanvas(frame_canv)
    frame_value= Frame(frame_action, width = 700, height = 150)    # Alocação das opções
    geometricsTransformation2D(frame_button, canvas)
    cutout(frame_button,canvas)
    rasterization(frame_button,canvas)
    makeOptions(frame_value,canvas)
    frame_value.pack()
# 
def makeOptions(op_frame,canvas):
    lbl_inst = Label(op_frame,text="Escreva as coordenadas dos pontos A e B, nos retangulos na forma [x1][y1][x2][y2] ou clique em 2 pontos do canvas(inicial e final). \nDepois, clique no botão 'Enviar Valores'. (Em caso de ponto, sera considerado o primeiro valor).\n Para circunferencias sera considerado x1, e y1 como pontos do centro.Aplique o raio tb.",foreground = "red",width = 100,height = 4)  
    lbl_aX1 = Label(op_frame, text="x1: ")  
    lbl_aY1 = Label(op_frame, text="y1: ")  
    lbl_aX2 = Label(op_frame, text="x2: ")  
    lbl_aY2 = Label(op_frame, text="y2: ")
    lbl_raio = Label(op_frame, text="Raio: ")  
    aX1 = Entry(op_frame,width = 7)
    aY1 = Entry(op_frame,width = 7)
    bX2 = Entry(op_frame,width = 7)
    bY2 = Entry(op_frame,width = 7)
    raio = Entry(op_frame,width = 7)
    
    lbl_inst.pack()
    lbl_aX1.pack(side=LEFT)
    aX1.pack(side=LEFT)
    lbl_aY1.pack(side=LEFT)
    aY1.pack(side=LEFT)
    lbl_aX2.pack(side=LEFT)
    bX2.pack(side=LEFT)
    lbl_aY2.pack(side=LEFT)
    bY2.pack(side=LEFT)
    lbl_raio.pack(side=LEFT)
    raio.pack(side=LEFT)

    btn_send = Button(op_frame, text = "Enviar Valores",command = lambda:setValues(aX1,aY1,bX2,bY2,canvas,raio))
    btn_send.pack(side=LEFT)
    canvas.bind("<Button-1>", getMousePosition)
    
def setValues(aX1,aY1,bX2,bY2,canvas,raio):
    # print(aX1.get(),aY1.get(),bX2.get(),bY2.get())
    rai = int(raio.get())
    x1 = int(aX1.get())
    y1 = int(aY1.get())
    x2 = int(bX2.get())
    y2 = int(bY2.get())
    position[0] = x1
    position[1] = y1
    position[2] = x2
    position[3] = y2
    position[4] = rai

def showCanvas(frame_canv):
    canv = Canvas(frame_canv,width = 700, height = 530, bg='white')
    canv.pack()
    return canv

def setGeo(x,y):
    global geo_trans2d_x
    global geo_trans2d_y
    geo_trans2d_x = int(x.get())
    geo_trans2d_y = int(y.get())

def clearCanvas(canvas):
    canvas.delete('all')

# MAIN |===================================================================================================================
def start():
    root = Tk()
    root.title("Trabalho de CG")
    root.geometry("960x620")
    makeFrams(root)
    

    root.mainloop()


start()
