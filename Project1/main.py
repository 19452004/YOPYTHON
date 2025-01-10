import os 
import Operasi
import Suhu
import csv
import convert_money


if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    def calculator_console():
        while(True):
            print("pilih opsi yang tersedia")
            print(f"1. penjumlahan")
            print(f"2. pengurangan")
            print(f"3. perkalian")
            print(f"4. pembagian")
            
            choose = input("silahkan pilih (1,2,3,4): ")
            
            match choose:
                case "1": Operasi.tambah_func() 
                case "2": Operasi.kurang_func()
                case "3": Operasi.kali_func()
                case "4": Operasi.bagi_func()
                
            is_done = input("apakah sudah selesai dengan program menghitung (y/n)? ")
            if is_done == "y" or is_done == "Y":
                break
            
    def ConvertCelcius_console():
        while(True):
            print("pilih opsi yang tersedia")
            print(f"1. Fahrenheit")
            print(f"2. Kelvin")
            print(f"3. Reamur")
            
            choose = input("silahkan pilih (1,2,3): ")
            
            
            if choose == "1" or choose == "2" or choose == "3":
                match choose:
                    case "1": Suhu.Fahrenheit_func()
                    case "2": Suhu.kelvin_func()
                    case "3": Suhu.reamur_func()
            else:
                print("masukan pilihan yang benar (1,2,3)")
                break 
            is_done = input("Apakah sudah  selesai mengonversi (y/n)? ")
            if is_done == "y" or is_done == "Y":
                break
            
    def ConvertUang_console():
        convert_money.main_convert()
                
    
    def main_menu():
        option = True
        while(option):
            print(30*"=")
            print("SELAMAT DATA DI APLIKASI KAMI")
            print(30*"=")
            print(f"1. SIMPLE CALCULATOR")
            print(f"2. CONVERT SUHU")
            print(f"3. CONVERT MATA UANG")
            print(f"4. EXIT!!")
            opsi_user = int(input("Masukan pilhan menu diatas(1/2/3): "))
            match(opsi_user):
                case 1:
                     calculator_console()
                case 2:
                    ConvertCelcius_console()
                case 3:
                    ConvertUang_console()
                case 4:
                    break
                
        option != False

        print("Program selesai, Terimakasih banyak telah menggunakan program kami")
        
  
        
    def Register():
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")
        
        dataAkun = []
        
        with open('dataAkun.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=",")
            for row in csv_reader:
                dataAkun.append({'username' : row[0], 'password' : row[1]})
        
        username_ada = False
        
        for akun in dataAkun:
            if username == akun['username']:
                print("Username sudah digunakan, coba ganti")
                username_ada = True
                break
           
        if username_ada == False:
            databaru = {'username': username, 'password': password}
            with open('dataAkun.csv', 'a', newline='') as file:
                writter = csv.DictWriter(file, fieldnames = databaru.keys())
                writter.writerow(databaru)
            print("Register berhasil silahkan login <3 ")
               
    def Login():
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")
        
        dataAkun = []
        with open('dataAkun.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter = ",")
            for row in csv_reader:
                dataAkun.append({'username': row[0], 'password': row[1]})
                
        datalogin = []
        for i in dataAkun :
            if username== i['username'] and password ==i['password']:
                datalogin.append(i)
                print(20*"=")
                print("Berhasil login")
                main_menu()
                
        for i in dataAkun:
            if username != i['username']:
                print(25*"=")
                print("username salah/tidak ada")
                break
                
        for i in dataAkun:
            if password != i['password']:
                print(25*"=")
                print("password salah")
                break
            
        if len(datalogin) == 0:
            print(25*"=")
            print("Akun tidak ditemukan")
            print(25*"=")
        
    
    opsi1 = True
    while(opsi1):

        print(f"1. REGISTER")
        print(f"2. LOGIN")
        print(f"3. EXIT!!!")
        pilihan = int(input("pilih login/regist(1/2/3): "))
        match(pilihan):
            case 1:
                Register()
            case 2:
                Login()
            case 3:
                break
            
    opsi1 != False
    print("SELESAI, TERIMAKASIH!")
          