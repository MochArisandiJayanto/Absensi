# -------------------- IMPORT LIBRARY ---------------------
import os, time, datetime,pandas

# -------------------- MENU UTAMA ---------------------
def menu_1():
    print("="*85)
    print("|\t\t❖   SELAMAT DATANG DI PERUSAHAAN ARSELLY TANI  ❖\t\t    |")
    print("="*85)
    print("-"*35, "Menu Option  ☰", "-"*34)
    print("|"," "*81,"|")
    print("|\t 1. Admin\t\t 2. Pegawai\t\t 3. Hentikan Program\t    |")
    print("|"," "*81,"|")
    print("="*85)
    print()
    
# -------------------- MENU ADMIN ---------------------
def menu_2():
    while True:
        print("="*85)
        print("|\t\t\t\tADMIN ACCES MAIN MENU ✎\t\t\t\t    |")
        print("="*85)
        print("|\t\t\t1. Daftar Karyawan\t\t\t\t\t    |")
        print("|\t\t\t2. Penambahan Karyawan\t\t\t\t\t    |")
        print("|\t\t\t3. Penghapusan Daftar Karyawan (RESIGN)\t\t\t    |")
        print("|\t\t\t4. Update Status Karyawan\t\t\t\t    |")
        print("|\t\t\t5. Daftar Absensi\t\t\t\t\t    |")
        print("|\t\t\t6. Exit\t\t\t\t\t\t\t    |")
        print("="*85)
        print()
        ques_2 = input("Pilih Options : ")
        if ques_2 == "1":
            os.system("cls")
            daftar_pegawai()
            input("\t\t\t>> Tekan 'Enter' untuk kembali ke menu <<")
            print()
            print("\t\t\t  #==================================#")
            print("\t\t\t  |     Kembali ke menu......  ⟳     |")
            print("\t\t\t  #==================================#")
            time.sleep(3)
            os.system("cls")
        elif ques_2 == "2":
            os.system("cls")
            rekrut()
            os.system("cls")
        elif ques_2 == "3":
            os.system("cls")
            delete()
        elif ques_2 == "4":
            os.system("cls")
            update_data()
        elif ques_2 == "5":
            os.system("cls")
            presensi_pegawai()
            input("\t\t\t>> Tekan 'Enter' untuk kembali ke menu <<")
            print()
            print("\t\t\t  #==================================#")
            print("\t\t\t  |     Kembali ke menu......  ⟳     |")
            print("\t\t\t  #==================================#")
            time.sleep(3)
            os.system("cls")
        elif ques_2 == "6":
            os.system("cls")
            input("\t\t\t    >> Tekan Enter untuk exit <<")
            print("\t   #=============================================================#")
            print("\t   |                                                             |")
            print("\t   |   Anda akan keluar dari menu ini.... mohon bersabar..!! ⟳   |")
            print("\t   |                                                             |")
            print("\t   #=============================================================#")
            time.sleep(3)
            os.system("cls")
            break
        
# -------------------- LOGIN ADMIN ---------------------
def login_admin():
    print("="*85)
    print("|\t\t\t\t  MASUKAN USER & PASSWORD \t\t\t    |")
    print("="*85,"\n")
    log_ques = input("➤   Masukkan Username : ")
    pas_ques = input("➤   Masukkan Password : ")
    if log_ques == "admin" and pas_ques == "admin":
        os.system("cls")
        print("\t\t#========================#")
        print("\t\t|  SELAMAT DATANG ADMIN  |")
        print("\t\t#========================#")
        print()
        input("\t  Tekan 'Enter' untuk lanjut ke menu >> ")
        print("Sebentar lagi anda akan diarahkan ke 'ADMIN ACCES MAIN MENU'...")
        time.sleep(4)
        os.system("cls")
        menu_2()
    else:
        os.system("cls")
        print("\t\t#========================================#")
        print("\t\t|            User tidak valid            |")
        print("\t\t#========================================#")
        time.sleep(2)
        os.system("cls")
        
# -------------------- LOGIN PEGAWAI ---------------------
def login_pegawai():
    print("="*85)
    print("|\t\t\t\t  ABSENSI MASUK KERJA \t\t\t\t    |")
    print("="*85,"\n")
    print("Identitas Pegawai :\n")
    log_choice = input("➤   Masukkan Nama Lengkap Pegawai : ")
    for i in range(len(daftar_karyawan)):
        if log_choice == daftar_karyawan.loc[i]["nama"]:
            print("Hari Kerja :\n☞. Senin\n☞. Selasa\n☞. Rabu\n☞. Kamis\n☞. Jum'at\n")
            choice = input("➤   Pilih Hari : ")
            choice_2 = input("➤   Jam Masuk Kerja : ")
            tanggal = datetime.date.today()
            input("Tekan Enter untuk melakukan Absensi >> ")
            absensi.loc[-1] = (log_choice, choice, choice_2, tanggal.strftime("%d/%m/%Y"))
            print("#===============================================================================================================================================#")
            print("|                                                                                                                                               |")
            print("|                           Absensi kerja anda akan kami catat untuk hari ini.... Silahkan menjalani pekerjaan anda....                         |")
            print("|                                                                                                                                               |")
            print("#===============================================================================================================================================#")
            time.sleep(4)
            os.system("cls")
            
            absensi_data(ABSEN_PATH, absensi)

# -------------------- LOGOUT PEGAWAI / PRESENSI KELUAR ---------------------
def presensi_out():
    print("="*85)
    print("|\t\t\t\t  ABSENSI KELUAR KERJA \t\t\t\t    |")
    print("="*85,"\n")
    presensi_pegawai()
    print()
    log_out = int(input("➤   Masukkan Nomor Urut Pegawai : "))
    absensi.drop(log_out, inplace=True)
    print()
    os.system("cls")
    print("•========================================================================================•")
    print("|  Anda telah melakukan absensi pulang.... Semoga harimu menyenangkan.... Terima Kasih.  |")
    print("•========================================================================================•")
    time.sleep(4)
    os.system("cls")
    
    absensi_data(ABSEN_PATH, absensi)
    
# -------------------- MENU PEGAWAI ---------------------
def menu_3():
    print("#","="*81,"#")
    print("|\t\t\t     SILAHKAN LAKUKAN ABSENSI KERJA \t\t\t    |")
    print("#","="*81,"#")
    print("|\t\t                    \t\t                  \t\t    |")
    print("|\t\t    1. Absensi Masuk\t\t 2. Absensi Pulang\t\t    |")
    print("|\t\t                    \t\t                  \t\t    |")
    print("#","="*81,"#")
    print()
    ques_hero = input("➤   Lakukan Presensi >> ")
    if ques_hero == "1":
        os.system('cls')
        login_pegawai()
                 
    elif ques_hero == "2":
        os.system('cls')
        presensi_out()
        
# -------------------- LIST DAFTAR KARYAWAN ---------------------
def daftar_pegawai():
    print("#","="*94,"#")
    print("| %2s | %-30s | %-9s | %-16s | %-25s |"%("NO","NAMA KARYAWAN","UMUR","ASAL KOTA","STATUS KARYAWAN"))
    print("#","="*94,"#")
    for i in range(len(daftar_karyawan)):
        print("| %2s | %-30s | %-9s | %-16s | %-25s |"%(i, daftar_karyawan.iloc[i]['nama'],daftar_karyawan.iloc[i]['umur'],daftar_karyawan.iloc[i]['asal'],daftar_karyawan.iloc[i]['status']))
    print("#","="*94,"#")
    print()
      
# -------------------- LIST DATA ABSENSI KARYAWAN ---------------------   
def presensi_pegawai():
    print("+","="*81,"+")
    print("| %2s | %-30s | %-12s | %-10s | %-15s |"%("NO","NAMA PEGAWAI YANG ABSEN","HARI ABSEN","JAM MASUK","TANGGAL ABSENSI"))
    print("+","="*81,"+")
    for i in range(len(absensi)):
        print("| %2s | %-30s | %-12s | %-10s | %-15s |"%(i, absensi.iloc[i]['log_user'],absensi.iloc[i]['hari'],absensi.iloc[i]['jam'],absensi.iloc[i]['waktu']))
    print("+","="*81,"+")
    
# -------------------- PENAMBAHAN KARYAWAN ---------------------
def rekrut():
    print("="*85)
    print("|\t\t\t\t  RECRUITMENT KARYAWAN \t\t\t\t    |")
    print("="*85,"\n")
    print()
    nama = input("➤   Nama Lengkap : ")
    umur = input("➤   Umur : ")
    asal = input("➤   Asal Kota : ")
    pegawai = input("➤   Status Pekerjaan : ")
    daftar_karyawan.loc[-1] = (nama, umur, asal, pegawai)
    os.system("cls")
    print("\t\t#========================================================#")
    print("\t\t|                                                        |")
    print("\t\t|   Data karyawan dalam tahap proses penambahan .... ⟳   |")
    print("\t\t|                                                        |")
    print("\t\t#========================================================#")
    time.sleep(5)
    os.system("cls")
    print("\t\t#========================================================#")
    print("\t\t|                                                        |")
    print("\t\t|       Data telah berhasil ditambahkan ........ ✔       |")
    print("\t\t|                                                        |")
    print("\t\t#========================================================#")
    time.sleep(2)
    
    rekrut_data(DATA_PATH, daftar_karyawan)


def update_data():
    daftar_pegawai()
    daftar_baru = daftar_karyawan
    print()
    index = int(input("➤   Pilih nomor pegawai yang ingin di upadate status pekerjaanya : "))
    status_new = input("➤   Update status baru pegawai : ")
    ubah_1 = input("➤   Apakah anda yakin ingin mengupdate status tersebut ? [Y/T] :  " )
    if ubah_1 == "Y" or ubah_1.lower() == "y":
        daftar_baru.loc[index] = (daftar_baru.loc[index]["nama"], daftar_baru.loc[index]["umur"], daftar_baru.loc[index]["asal"], status_new)
        os.system("cls")
        print("\t\t#========================================================#")
        print("\t\t|                                                        |")
        print("\t\t|   Data status karyawan dalam proses updating ..... ⟳   |")
        print("\t\t|                                                        |")
        print("\t\t#========================================================#")
        time.sleep(5)
        os.system("cls")
        print("\t\t#========================================================#")
        print("\t\t|                                                        |")
        print("\t\t|         Data telah berhasil diupdate ....... ✔         |")
        print("\t\t|                                                        |")
        print("\t\t#========================================================#")
        time.sleep(2)
        os.system("cls")
        
        rekrut_data(DATA_PATH, daftar_karyawan)
        
    elif ubah_1 == "T" or ubah_1.lower() == "t":  
        os.system("cls")
        print("\t\t#========================================================#")
        print("\t\t|                                                        |")
        print("\t\t|        Data status tidak jadi diubah ........ ✘        |")
        print("\t\t|                                                        |")
        print("\t\t#========================================================#")
        time.sleep(4)
        os.system("cls") 
# -------------------- PENGHAPUSAN KARYAWAN ---------------------
def delete():
    daftar_pegawai()
    ques_1 = int(input("➤   Hapus Karyawan Yang Resign/Tidak Bekerja Lagi : "))
    past = input("➤   Apakah kamu yakin ingin menghapus daftar karyawan tersebut ?? : [Y/T] >> ")
    if past == "Y" or past.lower() == "y":
        daftar_karyawan.drop(ques_1, inplace=True)
        os.system("cls")
        print("\t\t#========================================================#")
        print("\t\t|                                                        |")
        print("\t\t|   Data karyawan dalam tahap proses penghapusan.... ⟳   |")
        print("\t\t|                                                        |")
        print("\t\t#========================================================#")
        time.sleep(5)
        os.system("cls")
        print("\t\t#========================================================#")
        print("\t\t|                                                        |")
        print("\t\t|         Data telah berhasil dihapus ........ ✔         |")
        print("\t\t|                                                        |")
        print("\t\t#========================================================#")
        time.sleep(2)
        os.system("cls")
        
        rekrut_data(DATA_PATH, daftar_karyawan)
        
    elif past =="T" or past.lower() == "t":
        os.system("cls")
        print("\t\t#========================================================#")
        print("\t\t|                                                        |")
        print("\t\t|           Data tidak jadi dihapus ........ ✘           |")
        print("\t\t|                                                        |")
        print("\t\t#========================================================#")
        time.sleep(4)
        os.system("cls")
        
# -------------------- File Handling ---------------------
def muat_daftarpegawai(_path):
    df = pandas.read_csv(_path)
    return df
    
def rekrut_data(_path, _data):
    _data.to_csv(_path, index=False)

def muat_absensi(_path):
    df = pandas.read_csv(_path)
    return df

def absensi_data(_file, _data):
    _data.to_csv(_file, index=False)
        
# -------------------- DATABASE ---------------------
DATA_PATH = "daftar_karyawan.csv"
daftar_karyawan = muat_daftarpegawai(DATA_PATH)

ABSEN_PATH = "absensi.csv"
absensi = muat_absensi(ABSEN_PATH)

# -------------------- ALUR PROGRAM ---------------------
while True:
    menu_1()
    ques = input("➤    Pilih ---------- >> ")
    if ques == "1":
        os.system("cls")
        login_admin()
    elif ques == "2":
        os.system("cls")
        menu_3()
    elif ques == "3":
        break