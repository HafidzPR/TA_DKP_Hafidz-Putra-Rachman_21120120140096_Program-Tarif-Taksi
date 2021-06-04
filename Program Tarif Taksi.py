#Program Utama: Argometer Tarif Taksi

#Meng-import resources dari platform GUI tkinter
from tkinter import *
from typing import Collection
root = Tk()
#Dimensi layar GUI 700pixel x 400pixel
root.geometry("700x400")
#Heading yang akan muncul pada layar GUI
Label(root, text="Program Kalkulasi Tarif Taksi", font="ar 16 bold").grid(row=0, column=3)

#Form yang akan bisa diisi kan
jarak = Label(root, text="Silahkan masukkan jarak yang akan ditempuh (KM):")
penumpang = Label(root, text="Berapa banyak penumpang:")

jarak.grid(row=1, column=2)
penumpang.grid(row=2, column=2)



root.mainloop()

#==================================================================================================================

#Memperbolehkan program untuk meng-run funsi timer & clear layar.
import os, time 



def taksi():
    #Mencoba meng-run kode ini:
    try:
        #Variabel 'jarak' merekam user input mengenai jarak yang akan ditempuh (berbasis format float 0.00)
        jarak=float(input("Silahkan masukkan jarak yang akan ditempuh (KM):"))
        #Variabel 'penumpang' merekam jumlah penumpang taksi (berbasis format integer 1,2,dll)
        penumpang=int(input("Berapa banyak penumpang:"))
        #Variabel 'tarif' merekam kalkulasi: Rp.10,000 per penumpang (berbasis format integer)
        tarif=10000*penumpang
        #Variabel 'jarakTempuh' merekam jarak ditempuh x 10
        jarakTempuh=jarak*10
        #Variabel 'tarifAkhir' merekam total biaya yang harus dibayar oleh para penumpang (tarif+jarakTempuh)
        tarifAkhir=tarif+jarakTempuh
        #Menggambarkan jumlah total biaya terdekat dengan 2 tempat desimal
        print("-"*30,f"\nBiaya yang harus dibayar adalah: Rp.{round(tarifAkhir,2)}")
    #Jika input salah dan kode tidak bisa berjalan, tampilkan pesan error ini:
    except:
        #Pesan error yang akan ditampilkan
        print("*** Input yang salah ***")
        #Tunggu 2 detik agar user dapat membaca tampilan pesan error
        time.sleep(2)
        #Meng-clear layar ke kondisi semula (Refresh)
        os.system('clear')
        #Call fungsi taksi() agar user dapat memasukkan detail lagi
        taksi()
#Call fungsi taksi() untuk mengulang program dari semula
taksi()

