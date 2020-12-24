import sqlite3,tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from datetime import datetime
class program:
    def ekle(s):
        def kaydet(s):
            if inputisim.get() and inputsinif.get():
                tarih=datetime.now().strftime("%m/%d/%y, %H:%M:%S")            
                s.komut.execute("INSERT INTO bilgiler VALUES(NULL,?,?,?)",(inputisim.get(),inputsinif.get(),tarih))
                s.db.commit()
                s.komut.execute("SELECT * FROM bilgiler ORDER BY id ASC LIMIT 1")
                row=s.komut.fetchall()
                s.tablo.insert("",0,text=row[0][0],values=(inputisim.get(),inputsinif.get(),tarih))
                tkinter.messagebox.showinfo("Başarılı","Veritabanına kaydedildi!")
                ekle.destroy()
            else:
                tkinter.messagebox.showerror("Hata","Alanlar doldurulmadan geçilemez")
        def iptal():
            ekle.destroy()

        if s.dbpath:
            ekle=Tk()
            ekle.title("Ürün ekleme ekranı")
            Label(ekle,text="Ürün İsmi:").grid(row=0,column=0,padx=10,pady=10)
            inputisim=Entry(ekle)
            inputisim.grid(row=0,column=1,padx=10,pady=10)
            Label(ekle,text="Ürün Sınıfı:").grid(row=1,column=0,padx=10,pady=10)
            inputsinif=Entry(ekle)
            inputsinif.grid(row=1,column=1,padx=10,pady=10)
            Button(ekle,text="İptal",bg="red",fg="white",command=iptal).grid(row=2,column=0,padx=5,pady=5)
            Button(ekle,text="Kaydet",bg="green",fg="white",command=lambda:kaydet(s)).grid(row=2,column=1,padx=5,pady=5)
        else:
            tkinter.messagebox.showerror("Hata","Veritabanı Seçilmedi")
    def listele(s):
        if s.dbpath:
            s.tablo.delete(*s.tablo.get_children())
            for row in s.komut.execute("SELECT * FROM bilgiler ORDER BY id ASC"):
                s.ids.append(row[0])
                s.tablo.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        else:
            tkinter.messagebox.showerror("Hata","Veritabanı Seçilmedi")
    def sil(s):
        if s.dbpath:
            try:
                selected=s.tablo.focus()
                selectedid=s.tablo.item(selected)["text"]
                s.komut.execute("DELETE FROM bilgiler WHERE id=?",(selectedid,))
                s.db.commit()
                s.tablo.delete(selected)
                tkinter.messagebox.showinfo("Başarılı","Seçili satır veritabanından silindi")
            except:
                tkinter.messagebox.showerror("Hata","Satır Seçilmedi")
        else:
            tkinter.messagebox.showerror("Hata","Veritabanı Seçilmedi")

    def guncelle(s):
        def kaydet(s):
            if inputisim.get() and inputsinif.get():
                s.komut.execute("UPDATE bilgiler SET ürün = ?,sınıf=? WHERE id=?",(inputisim.get(),inputsinif.get(),s.tablo.item(selected)["text"]))
                s.db.commit()
                s.tablo.insert("",0,text=s.tablo.item(selected)["text"],values=(inputisim.get(),inputsinif.get(),s.tablo.item(selected)["values"][2]))
                s.tablo.delete(selected)
                tkinter.messagebox.showinfo("Başarılı","Kayıt güncellendi")
                edit.destroy()
            else:
                tkinter.messagebox.showerror("Hata","Alanlar doldurulmadan geçilemez")
        def iptal():
            edit.destroy()
            
        if s.dbpath:
            try:
                selected=s.tablo.focus()
                edit=Tk()
                edit.title("Ürün güncelleme ekranı")
                Label(edit,text="Ürün İsmi:").grid(row=0,column=0,pady=10,padx=10)
                Label(edit,text="Ürün Sınıfı:").grid(row=1,column=0,pady=10,padx=10)
                inputisim=Entry(edit)
                inputsinif=Entry(edit)
                inputisim.grid(row=0,column=1,pady=10,padx=10);inputisim.insert(0,s.tablo.item(selected)["values"][0])
                inputsinif.grid(row=1,column=1,pady=10,padx=10);inputsinif.insert(0,s.tablo.item(selected)["values"][1])
                Button(edit,text="İptal",bg="red",fg="white",command=iptal).grid(row=2,column=0,padx=5,pady=5)
                Button(edit,text="Kaydet",bg="green",fg="white",command=lambda:kaydet(s)).grid(row=2,column=1,padx=5,pady=5)
            except:
                tkinter.messagebox.showerror("Hata","Satır seçilmedi")
                edit.destroy()
            
        else:
            tkinter.messagebox.showerror("Hata","Veritabanı Seçilmedi")

    def sec(s):
        s.dbpath=filedialog.askopenfilename(initialdir="/",title="Veritabanı seçiniz",
                                          filetypes=(("Veritabanı dosyası","*.db"),("Tüm dosyalar","*.*")))
        if ".db" in s.dbpath:
            s.dosyayolu.configure(text=s.dbpath)
            s.db=sqlite3.connect(s.dbpath)
            s.komut=s.db.cursor()
            s.komut.execute("CREATE TABLE IF NOT EXISTS bilgiler (id INTEGER PRIMARY KEY AUTOINCREMENT ,ürün TEXT NOT NULL, sınıf TEXT NOT NULL, tarih TEXT NOT NULL)")
            s.db.commit()
        else:
            s.dbpath=""

    def yeni(s):
        s.dbpath=filedialog.asksaveasfilename(parent=s.main,initialdir="/",title="Veritabanını kuracağınız klasörü seçin:",defaultextension=".db")
        if s.dbpath == None:
            s.dbpath=""
        else:
            s.dosyayolu.configure(text=s.dbpath)
            s.db=sqlite3.connect(s.dbpath)
            s.komut=s.db.cursor()
            s.komut.execute("CREATE TABLE IF NOT EXISTS bilgiler (id INTEGER PRIMARY KEY AUTOINCREMENT ,ürün TEXT NOT NULL, sınıf TEXT NOT NULL, tarih TEXT NOT NULL)")
            s.db.commit()


    def __init__(self):
        self.dbpath=""
        self.ids=[]
        
        self.main=Tk()
        self.main.title("Veritabanı")
        self.dosyayolu=Label(self.main,text="Veritabanı yolu",relief=SUNKEN,width=70)
        self.dosyayolu.grid(row=0,column=0)
        Button(self.main,text="Veritabanı Seç",command=self.sec).grid(row=0,column=1)
        Button(self.main,text="Yeni Veritabanı",command=self.yeni).grid(row=0,column=2)
        #tabloyu oluşturma
        self.tablo=ttk.Treeview(self.main)
        self.tablo["columns"]=("isim","sinif","tarih")
        self.tablo.column("#0",width=50,minwidth=25)
        self.tablo.column("isim",width=100,minwidth=25)
        self.tablo.column("sinif",width=100,minwidth=25)
        self.tablo.column("tarih",width=150,minwidth=25)
        self.tablo.heading("#0",text="ID")
        self.tablo.heading("isim",text="İsim")
        self.tablo.heading("sinif",text="Sınıf")
        self.tablo.heading("tarih",text="Ekleme Tarihi")
        self.tablo.grid(row=1,column=0,pady=10,rowspan=3)
        #butonlar
        Button(self.main,text="Listele",width=30,height=3,command=self.listele).grid(row=2,column=1,padx=5,pady=5)
        Button(self.main,text="Sil",width=30,height=3,command=self.sil).grid(row=2,column=2,padx=5,pady=5)
        Button(self.main,text="Güncelle",width=30,height=3,command=self.guncelle).grid(row=3,column=1,padx=5,pady=5)
        Button(self.main,text="Yeni Ekle",width=30,height=3,command=self.ekle).grid(row=3,column=2,padx=5,pady=5)
        self.main.mainloop()
  
root=program()
