from tkinter import *
from tkinter import messagebox
from random import choice

#Mise en place et personnalisation de la fenetre
window = Tk()
window.geometry("1080x725")
window.config(background="black")
window.title("FIRST GAME")

#creation titre/infos
image_bienvenue = PhotoImage(file="image_bienvenue.png").subsample(1, 2)
titre=Label(window,text="BIENVENUE",padx=400,pady=30,font=('Courrier',30),image=image_bienvenue,compound='center',bg="black",fg="white")
titre.pack()


#creation de l'espace jeu et du carre
image_voleur = PhotoImage(file="steal.png").subsample(23)
canvas = Canvas(window, width=500, height=500, bg="black")
rectangle = canvas.create_image(12,15,image=image_voleur)
#rectangle = canvas.create_rectangle(0,0,25,25,fill="green")
canvas.pack(expand=YES,side="left")


#creation du menu
Menu_principal= Canvas(window, width=500, height=500,background="black",bd=5)
Menu_principal.pack(expand=YES,side="right")

title_menu=Label(Menu_principal,text="MENU",width=65,bg="black",fg="green")
title_menu.place(x=27,y=10)

title_menu2=Label(Menu_principal,text="MENU",width=65,bg="black",fg="green")
title_menu2.place(x=27,y=481)

XP=Label(Menu_principal,text="XP :",bg="black",fg="green",font=('Arial',40))
XP.place(x=80,y=250)
XP_nb=Label(Menu_principal,text="0",bg="black",fg="yellow",font=('Arial',40))
XP_nb.place(x=280,y=250)

lvl=Label(Menu_principal,text="LVL :",bg="black",fg="green",font=('Arial',40))
lvl.place(x=80,y=350)
lvl_nb=Label(Menu_principal,text="0",bg="black",fg="yellow",font=('Arial',40))
lvl_nb.place(x=280,y=350)

infos=Label(Menu_principal,bg="black",fg="yellow",font=('Time',8,'bold italic'),text="INFOS :\n\n -TU EST UN VOLEUR EN QUÊTE D’ARGENT, AIDE LE A EN DÉROBER LE PLUS POSSIBLE .\n\n-TU GAGNE DES XP QUAND TU TROUVES DES « MONEY-BAGS » (SAC D’ARGENT).\n\n-TU PERD DES XP EN TE FRACASSANT LA TÊTE SUR LES REBORDS DE LA COUR.\n\n-LES SEULES TOUCHES ACCEPTÉES SONT    ↑     ↓     ←      →  .\n\n- TU GAGNES EN NIVEAU TOUT LES 50 POINTS D’XP OBTENUS .\n")
infos.place(x=15,y=50)

#initialisation de certain parametre
x = 0
y = 0
compteur = 0
list_touche = ["Start"]


#les touche sont mise au fur et a mesure dans une liste
def keysym(event):
    global list_touche

    if event.keysym == "Left":
        list_touche.append("Left")

    elif event.keysym == "Right":
        list_touche.append("Right")

    elif event.keysym == "Up":
        list_touche.append("Up")

    elif event.keysym == "Down":
        list_touche.append("Down")

    else:
        messagebox.showinfo("Error", "Touche non-valide veuillez utlise seulement ces touches(↑,↓,→,←)")



position_x = 0
position_y = 0
x_point = 1
y_point = 1
image_argent = PhotoImage(file="money-bag.png").subsample(23)

#Ici on fait bouger le rectangle par rapport a la derniere touche ecrite dans la liste de touche ci dessus
#et si les point du rectangle sont les meme que ceux du rond on appele la fonction random_point_change pour changer de place le rond

def move_rect():
    global x, y, list_touche, position_x, position_y

    Direction = list_touche[-1]

    if Direction == "Right":
        if position_x < 470:
            canvas.move(rectangle, 25, y)
            position_x += 25
        else:
            modifie_xp_malus()

    elif Direction == "Left":
        if position_x > 0:
            canvas.move(rectangle, -25, y)
            position_x -= 25
        else:
            modifie_xp_malus()

    elif Direction == "Up":
        if position_y > 0:
            canvas.move(rectangle, x, -25)
            position_y -= 25
        else:
            modifie_xp_malus()

    elif Direction == "Down":
        if position_y < 470:
            canvas.move(rectangle, x, 25)
            position_y += 25
        else:
            modifie_xp_malus()

    if str(position_x) == str(x_point) and str(position_y) == str(y_point):
        random_point_change()
        modifie_xp_bonus()

    if nb_players<50:
        window.after(120, move_rect)
        lvl_nb['text']= "0"
        lvl_nb['fg']="yellow"
    elif nb_players<100:
        window.after(80, move_rect)
        lvl_nb['text'] = "1"
        lvl_nb['fg'] = "#d36d75"
    elif nb_players<150:
        window.after(60, move_rect)
        lvl_nb['text'] = "2"
        lvl_nb['fg'] = "#df4e56"
    elif nb_players<200:
        window.after(30, move_rect)
        lvl_nb['text'] = "3"
        lvl_nb['fg'] = "#e71837"
    else:
        window.after(20, move_rect)
        lvl_nb['text'] = "4"
        lvl_nb['fg'] = "#cbe7e9"


#Ici on creer un rond avec des coordonne issus d'un fichier (0 a 400 par tranche de 25)
def random_point():
    global x_point, y_point,nb,canvas2,image_argent

    fill = open("position.txt", "r")
    nb=fill.read().strip().split("\n")

    x_point = choice(nb)
    y_point = choice(nb)

    fill.close()
    #print(x_point, y_point)

    canvas2 = Canvas(canvas, width=25, height=25, bg="black", highlightbackground="black")
    canvas2.create_image(14, 12, image=image_argent)
    # canvas2.create_oval(0, 0, 25, 25, fill="red")
    canvas2.place(x=x_point, y=y_point)


#Ici la fonction qui va changer de place le rond quand le rectangle et le rond se "touche"
def random_point_change():
        global x_point,y_point
        fill = open("position.txt", "r")
        nb = fill.read().strip().split("\n")
        fill.close()
        x_point = choice(nb)
        y_point = choice(nb)
        #print(x_point, y_point)

        canvas2.place(x=x_point, y=y_point)

nb_players=0

def modifie_xp_bonus():
    global nb_players
    nb_players+=10
    XP_nb['text']=str(nb_players)
    XP_nb['fg']="green"
    canvas['highlightbackground'] = "white"

def modifie_xp_malus():
    global nb_players
    if nb_players>-50:
        nb_players-=10
        XP_nb['text']=str(nb_players)
        XP_nb['fg'] = "red"
        canvas['highlightbackground'] = "red"


random_point()
move_rect()
window.bind('<KeyPress>', keysym)

window.mainloop()
