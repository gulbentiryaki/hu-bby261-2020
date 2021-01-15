from tkinter import *
import random
root = Tk();
root.title("Perudo");
root.geometry("400x400");

txt=StringVar();
txt.set("MERHABA YABANCI, YOKSA YALANCIMI DEMELIYDIM !! \n SIRA SENDE HADI BAHSI BASLAT !! ")
#Bütün zarlari oyun alanina attim
oyuncu1=[random.randrange(1,7),random.randrange(1,7),random.randrange(1,7)]
oyuncu2=[random.randrange(1,7),random.randrange(1,7),random.randrange(1,7)]
#Bütün zarlarin ekranda gostermek icin string array olusturdum
oyuncu1t=[StringVar(),StringVar(),StringVar()]
oyuncu2t=[StringVar(),StringVar(),StringVar()]
#oyuncu zarlarinin ekranda gosterilecek sekilde atamalari
oyuncu1t[0].set("?"),oyuncu1t[1].set("?"),oyuncu1t[2].set("?")
oyuncu2t[0].set(oyuncu2[0]),oyuncu2t[1].set(oyuncu2[1]),oyuncu2t[2].set(oyuncu2[2])

#bildirim yazisi
Label(root,bg="#b7a47b", textvariable = txt).pack(side = TOP);

#zarlarin gorsel olarak gosterilmesi
canvas = Canvas(root)

#rakibinzarlari
canvas.create_rectangle(80, 10, 150, 60, outline="#fb0", fill="#a28f35")
label = Label(root, textvariable=oyuncu1t[0],bg="#a28f35")
label.place(x=120, y=60)

canvas.create_rectangle(160, 10, 230, 60, outline="#fb0", fill="#a28f35")
label = Label(root, textvariable=oyuncu1t[1],bg="#a28f35")
label.place(x=200, y=60)

canvas.create_rectangle(240, 10, 310, 60, outline="#fb0", fill="#a28f35")
label = Label(root, textvariable=oyuncu1t[2],bg="#a28f35")
label.place(x=280, y=60)


#benimzarlarim
canvas.create_rectangle(80, 200, 150, 250, outline="#fb0", fill="#356ba2")
label = Label(root, textvariable=oyuncu2t[0],bg="#356ba2")
label.place(x=120, y=250)

canvas.create_rectangle(160, 200, 230, 250, outline="#fb0", fill="#356ba2")
label = Label(root, textvariable=oyuncu2t[1],bg="#356ba2")
label.place(x=200, y=250)

canvas.create_rectangle(240, 200, 310, 250, outline="#fb0", fill="#356ba2")
label = Label(root, textvariable=oyuncu2t[2],bg="#356ba2")
label.place(x=280, y=250)

canvas.pack()


#benim bahis tahminlerimi almak için
tane=StringVar();
taneT=StringVar();
label = Label(root, text="kac tane?").place(x=50, y=300)
Entry(root, width = 5, textvariable = taneT).place(x=120, y=300)

zar=StringVar();
zarT=StringVar();
label = Label(root, text="hangi zar?").place(x=180, y=300)
Entry(root, width = 5, textvariable = zarT).place(x=250, y=300)

def arttir():

  tane.set(taneT.get())
  zar.set(zarT.get())

  #ekrandaki kutulari temizlemek için
  taneT.set("")
  zarT.set("")
  botBahis()
def yalanci():
  if bAdeti() + kAdeti() >= int(tane.get()) :
    txt.set("RAKIBINIZ TAM BIR POKERFACE KAYBETTINIZ !\n")
  else :
    txt.set("YALANINI YAKALADINIZ, BAHSI KAZANDINIZ !\n")
  elleriGoster()


#botadeti
def bAdeti():
  SbottakiAdeti=0
  if str(oyuncu1[0])==zar.get() :
    SbottakiAdeti=SbottakiAdeti+1
  if str(oyuncu1[1])==zar.get() :
    SbottakiAdeti=SbottakiAdeti+1
  if str(oyuncu1[2])==zar.get() :
    SbottakiAdeti=SbottakiAdeti+1
  return SbottakiAdeti;
#kullaniciadeti
def kAdeti():
  SkullaniciAdeti=0
  if str(oyuncu2[0])==zar.get() :
    SkullaniciAdeti=SkullaniciAdeti+1
  if str(oyuncu2[1])==zar.get() :
    SkullaniciAdeti=SkullaniciAdeti+1
  if str(oyuncu2[2])==zar.get() :
    SkullaniciAdeti=SkullaniciAdeti+1
  return SkullaniciAdeti;

def botBahis():
  # bot 1 gelirse dogru 0 gelirse yalan soyleyecek
  bot =random.randrange(0,2)
  SbottakiAdeti = bAdeti()
  if bot==1:
    if SbottakiAdeti > int(tane.get()):
      tane.set(SbottakiAdeti)
      txt.set("BAHIS ARTTIRILDI !!  " + tane.get() + " TANE " + zar.get() + "\n")  # botun bahis tahmini
    elif int(zar.get()) != 6:
      bahis=FALSE
      for i in range(int(zar.get()) +1,7):
        bottakiAdeti=0
        if oyuncu1[0]==i :
          bottakiAdeti=bottakiAdeti+1
        if oyuncu1[1]==i :  
          bottakiAdeti=bottakiAdeti+1
        if oyuncu1[2]==i :  
          bottakiAdeti=bottakiAdeti+1
        if bottakiAdeti >= int(tane.get()) :
          tane.set(bottakiAdeti)
          zar.set(i)
          txt.set("BAHIS ARTTIRILDI !!  "+ tane.get() + " TANE " + zar.get()+"\n")  #botun bahis tahmini
          bahis=TRUE
          break
      if bahis==FALSE:
        #yalan soyle
        tane.set(random.randrange(int(tane.get()),7))
        zar.set(random.randrange(int(zar.get()),7))
        txt.set("BAHIS ARTTIRILDI !!  "+ tane.get() + " TANE " + zar.get()+"\n")
  else :
    #yalan soyle
    tane.set(random.randrange(int(tane.get()),7))
    zar.set(random.randrange(int(zar.get()),7))
    txt.set("BAHIS ARTTIRILDI !!  "+ tane.get() + " TANE " + zar.get()+"\n")

def elleriGoster():
  oyuncu1t[0].set(oyuncu1[0]),oyuncu1t[1].set(oyuncu1[1]),oyuncu1t[2].set(oyuncu1[2])

Button(root, text="Bahis arttir!", command=arttir).place(x=250, y=350)
Button(root, text="Aramizda Yalanci Var!", command=yalanci).place(x=50, y=350)





root.mainloop();