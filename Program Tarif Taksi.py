#Program [Kalkulasi Tarif Taksi]
#HAFIDZ PUTRA RACHMAN - 21120120140096
#Teknkik Komputer Universitas Diponegoro

#=====================================================================================================

#Import platform development GUI untuk Python (tKinter)
from tkinter import *
from tkinter import messagebox

#Definisi untuk fungsi tombol reset (nama, jarak dan penumpang akan dihapus)
def reset_entry():
    nama_tf.delete(0, 'end')
    jarak_tf.delete(0, 'end')
    penumpang_tf.delete(0, 'end')

#=====================================================================================================
#Defininisi penghitungan biaya tarif (biayaTarif) 
def hitung_biayaTarif():
    km = int(jarak_tf.get())
    orang = int(penumpang_tf.get())*1.5
    biayaTarif = (km*1000)*orang
    biayaTarif = round(biayaTarif, 2)
    biaya_tarif(biayaTarif)

    #Penjelasan Kalkulasi:

        #km = Jarak yang dimasukkan kepada text box 'Jarak Tempuh (KM)'
        #orang = Jumlah penumpang * 1.5 ~ Jadi setiap penumpang akan dikalikan bernilai 1.5
        #biayaTarif = (km*1000)*orang ~ Nilai 'km' akan dikalikan 1000 dimana hasil itu akan dikalikan dengan nilai 'orang'.
#=====================================================================================================

#Definisi ucapan submit terimakasih
def ucapan():
    n = 0
    for n in range(6):
        print("Terimakasih dan selamat jalan!", (n))
    n += 1

#=====================================================================================================
#Heading yang akan muncul pada layar GUI
Label(text="Program Kalkulasi Tarif Taksi", font="ar 16 bold").grid(row=0, column=3)

#=====================================================================================================
#Layar textbox yang akan ditampilkan kepada user untuk memberitahukan hasil kalkulasi biaya tarif dengan mata uang Rupiah.
#Setiap hasil biaya tarif akan digolongkan tergantung besarnya biaya tarif yang tergantung nilai jarak dan jumlah penumpang.
def biaya_tarif(biayaTarif):
    if biayaTarif < 10000:
        messagebox.showinfo('Hasil Perhitungan',
                            f'Biaya tarif perjalanan = Rp. {biayaTarif} Golongan Paket Kecil.')
    elif (biayaTarif > 10000) and (biayaTarif < 50000):
        messagebox.showinfo('Hasil Perhitungan',
                            f'Biaya tarif perjalanan = Rp. {biayaTarif} Golongan Paket Sedang.')
    elif (biayaTarif > 50000) and (biayaTarif < 100000):
        messagebox.showinfo('Hasil Perhitungan',
                            f'Biaya tarif perjalanan = Rp. {biayaTarif} Golongan Paket Besar.')
    elif (biayaTarif > 100000):
        messagebox.showinfo('Hasil Perhitungan',
                            f'Biaya tarif perjalanan = Rp. {biayaTarif} Golongan Paket Sangat Besar.')

#=====================================================================================================
# Dimensi, judul dan configurasi warna background program ini
app = Tk()
app.geometry('450x600')
app.title('Program Kalkulasi Tarif Taksi')
app.config(bg='#D7CA00')

var = IntVar()
frame = Frame(app, padx=10, pady=10, bg='#D7CA00')
frame.pack(expand=True)

#=====================================================================================================
# Kondisi Perjalanan, bisa dipilah salah satu (Siang atau Malam)
gen_lb = Label(frame, text='Kondisi Perjalanan : ', bg='#D7CA00')
gen_lb.grid(row=1, column=1)
frame2 = Frame(frame)
frame2.grid(row=1, column=2, pady=5)

siang_rb = Radiobutton(frame2, text='Siang', variable=var, value=1, bg='#D7CA00')
siang_rb.pack(side=LEFT)

malam_rb = Radiobutton(frame2, text='Malam',
                        variable=var, value=2, bg='#D7CA00')
malam_rb.pack(side=RIGHT)

#=====================================================================================================
# Text Box yang dapat diisi mengenai Nama Pengemudi Taksi tersebut
nama_lb = Label(frame, text="Nama Pengemudi : ", bg='#D7CA00')
nama_lb.grid(row=2, column=1)
nama_tf = Entry(frame, bg='#fdfdfd')
nama_tf.grid(row=2, column=2, pady=5)

# Text Box yang dapat diisi mengenai Jarak yang akan ditempuh pada perjalanan
jarak_lb = Label(frame, text="Jarak Tempuh (KM) : ", bg='#D7CA00')
jarak_lb.grid(row=3, column=1)
jarak_tf = Entry(frame, bg='#fdfdfd')
jarak_tf.grid(row=3, column=2, pady=5)

# Text Box yang dapat diisi mengenai Jumlah Penumpang
penumpang_lb = Label(frame, text="Jumlah Penumpang : ", bg='#D7CA00')
penumpang_lb.grid(row=4, column=1)
penumpang_tf = Entry(frame, bg='#fdfdfd')
penumpang_tf.grid(row=4, column=2, pady=5)

#=====================================================================================================
# Frame untuk button
frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)


# Button Kalkulasi (Untuk memproses data yang telah dimasukkan dan menghasilkan hasil kalkulasi data)
hitung_btn = Button(frame3, text='Kalkulasi', command=hitung_biayaTarif,
                    bg='#0000FF', fg='white')
hitung_btn.pack(side=RIGHT)

# Button Keluar (Untuk mentutup Program)
keluar_btn = Button(frame3, text='Keluar',
                    command=lambda: app.destroy(), bg='#FF0000', fg='white')
keluar_btn.pack(side=LEFT)

# Button Reset (Untuk menghapus dta yang telah dimasukkan dan mengkembalikan program ke kondisi semula)
reset_btn = Button(frame3, text='Reset', command=reset_entry,
                   bg='#00FF00')
reset_btn.pack(side=LEFT)

# Button terimakasih (Mengucapkan terimakasih kepada siapapun user-nya)
terimakasih_btn = Button(frame, text='Terimakasih',
                  command=ucapan, bg='#000000', fg='white')
terimakasih_btn.grid(row=7, columnspan=3, pady=10)

#=====================================================================================================
# Frame untuk pesan paragraph dibawah
frame4 = Frame(frame)
frame4.grid(row=6, columnspan=3, pady=1)
frame4.config(bg='#D7CA00')

# Pesan dari pemilik perusahaan yang mengkelola kendaraan taksi ini.
tabel1_lb = Label(frame4, text='Selamat datang di perusahaan asosiasi Yellow-Taxi Undip! ', bg='#D7CA00')
tabel1_lb.pack(side=TOP)
tabel2_lb = Label(frame4, text=' Silakan masukkan rincian mengenai perjalanan Anda', bg='#D7CA00')
tabel2_lb.pack(side=TOP)
tabel3_lb = Label(frame4, text='dan penumpang untuk menghitung perkiraan biaya tarif.', bg='#D7CA00')
tabel3_lb.pack(side=TOP)
tabel4_lb = Label(frame4, text='Terima kasih atas kepercayaan Anda pada layanan kami!', bg='#D7CA00')
tabel4_lb.pack(side=TOP)

#=====================================================================================================
# Mainloop program
app.mainloop()
#=====================================================================================================

#Sekian...
