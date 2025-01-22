import random as rd
import os
import clearprogram as clear


if __name__ == "__main__":
    sistem_operasi = os.name
    
    match(sistem_operasi):
        case "posix": os.system("clear")
        case"nt": os.system("cls")
        

    print("==================================================")
    print("====SELAMAT DATANG Di SIMPLE GAME VANUNIVERSITY=== ")
    print("==================================================")

    name = input("masukan nama kamu : ")
    print(f"Hallo {name}, selamat menikmati permainan semoga kamu beruntung!!")

    print('''
    coba tebak ada digoa nomor berapa alien itu bersembunyi
       ------------|_| |_| |_| |_| |_| |_|---------------
                    1   2   3   4   5   6             
    ''')
    
    alien_position = rd.randint(1,6)

    condition = True
    while(condition):
        
        user_opsi = int(input("Coba tebak ada di goa nomor berapa alien bersembunyi [1/2/3/4/5/6]: "))
        print("================================================================================")
        if user_opsi > 6:
            print("opsi tidak valid, silahkan pilih[1/2/3/4/5/6]")
        else:
            while True:
            
                option = input("Apakah kamu yakin alien ada di nomor tersebut[y/n]: ")
                print("================================================================================")

                if option == "Y" or option == "y":
                    if user_opsi == alien_position:
                        print(f"kamu berhasil menebaknya, alien bereda di dalam goa {alien_position}, dan pilihan kamu goa nomor {user_opsi}.")
                    else:
                        print(f"Kamu kurang beruntung {name},pilihan kamu di goa nomor {user_opsi}, ternyata alien ada di goa nomor {alien_position}")
                    break
                elif option == "n" or option == "N":
                    user_opsi = int(input("Coba tebak ada di goa nomor berapa alien bersembunyi [1/2/3/4/5/6]: "))
                else:
                    print("Input tidak valid , silahkan masukan[y/n]")
                
        choose = input("Apakah kamu ingin berhenti bermain game[y/n]: ")
        if choose == "y" or choose == "Y":
            print(f"yahh padahal baru sebentar, baik terimakasih {name} sudah bermain game, semoga hari anda menyenangkan")
            break
        