# beberapa jumlah konversi celcius, farenheit, reamur


#  Konversi Celsius
# 1. Konversi Celsius ke Fahrenheit
def celcius_to_farenheit(celcius) :
    farenheit = (celcius * 1.8) + 32
    return farenheit
# 2. Konversi Celsius ke Reaamur
def  celcius_to_reaamur(celcius) : 
    reamur = (celcius * 0.8 )
    return reamur
# 3. Konversi Celsius ke Kelvin
def  celsius_to_kelvin(celcius) :
    kelvin = celcius + 273
    return kelvin

#  Konversi Farenheit
# 1. Konversi Fahrenheit ke Celcius
def farenheit_to_celsius(farenheit):
    celcius  = 0.5 * ( farenheit - 32) 
    return celcius
# 2. Konversi Fahrenheit ke Reamur
def farenheit_to_reaamur(farenheit) :
    reamur = 0.4 * ( farenheit - 32) 
    return reamur
# 3. Konversi Fahrenheit ke Kelvin
def  farenheit_to_kelvin(farenheit) :
    kelvin = 0.5 * ( farenheit - 32) + 273
    return kelvin

# Konversi Reamur
# 1. Konversi Reamur ke Celcius
def  reamur_to_celsius(reamur) :
    celcius = (1.25 * reamur)
    return celcius
# 2. Konversi Reamur ke Fahrenheit
def reamur_to_fahrenheit(reamur) :
    fahrenheit= ((9/5)* reamur) + 32
    return fahrenheit
# 3. Konversi Reamur ke Kelvin
def reamur_to_kelvin(reamur) :
    kelvin = 5/4 * reamur + 273
    return kelvin

# Konversi Kelvin
# 1. Konversi Kelvin ke Celcius
def kelvin_to_celsius(kelvin) :
    celsius = kelvin -  273
    return celsius
# 2. Konversi Kelvin ke Reamur
def kelvin_to_reamur(kelvin):
    reamur = 4/5 * (kelvin - 273)
    return reamur
# 3. Konversi Kelvin ke Farenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = 9/5 * (kelvin - 273) + 32
    return fahrenheit


# celcius = float(input("masukan angka celcius: "))
# hasilKonversi = celcius_to_reaamur(celcius)
# print(f"Hasil dari konversi Celcius ke Reamur adalah %0.2f" % hasilKonversi )


# Program Utama
while True :
    print("\n")
    print("========================================")
    print("||              Menu Utama           ||")
    print("========================================")
    print("||   1. Perhitungan Celcius          ||")
    print("||   2. Perhitungan Reamur           ||")
    print("||   3. Perhitungan Farenheit        ||")
    print("||   4. Perhitungan Kelvin           ||")
    print("||   5. Keluar Sistem                ||")
    print("========================================")
    choose = input("Masukan pilihan anda: ")
    if choose.isdigit():
        choose = int(choose)
        if choose == 1:
            valid_celcius = False
            while not valid_celcius:
                celcius = input("Masukan Nilai Celcius: ")
                if celcius.isdigit():
                    celcius = float(celcius)
                    valid_celcius = True
                    while True :
                        print("===========================================")
                        print("||        Perhitungan Celcius            ||")
                        print("===========================================")
                        print("||   1. Perhitungan Celcius ke Reamur    ||")
                        print("||   2. Perhitungan Celcius ke Farenheit ||")
                        print("||   3. Perhitungan Celcius ke Kelvin    ||")
                        print("||   4. Kembali                          ||")
                        print("===========================================")
                        choise = input("Masukan Perhitungan yang diinginkan: ")
                        if choise.isdigit():
                            choise = int(choise)
                            if choise == 1:
                                convert_celcius_to_reamur = celcius_to_reaamur(celcius)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Celcius ke Reamur adalah", convert_celcius_to_reamur ,"R")
                                print("---------------------------------------------------------------")
                            elif choise == 2 :
                                convert_celcius_to_farenheit = celcius_to_farenheit(celcius)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Celcius ke Farenheit adalah", convert_celcius_to_farenheit ,"F")
                                print("---------------------------------------------------------------")
                            elif choise == 3:
                                convert_celcius_to_kelvin = celsius_to_kelvin(celcius)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Celcius ke Kelvin adalah", convert_celcius_to_kelvin ,"K")
                                print("---------------------------------------------------------------")
                            elif choise == 4 :
                                break
                            else :
                                print("Pilihlah sesuai pilihan yang ada !!")

                        elif choise.strip() == "":
                            print("Tidak boleh kosong, harus memilih !!")
                        else :
                            print("Hanya bisa memasukkan nomor yang tertera !!")
                elif celcius.strip() == "":
                    print("Nilai Celcius tidak boleh kosong")
                else :
                    print("Hanya bisa memasukkan angka, coba lagi!!")
        elif choose == 2 :
            valid_reamur = False
            while not valid_reamur:
                reamur = input("Masukan Nilai Reamur: ")
                if reamur.isdigit():
                    reamur = float(reamur)
                    valid_reamur = True
                    while True :
                        print("===========================================")
                        print("||        Perhitungan Reamur             ||")
                        print("===========================================")
                        print("||   1. Perhitungan Reamur ke Celcius    ||")
                        print("||   2. Perhitungan Reamur ke Farenheit ||")
                        print("||   3. Perhitungan Reamur ke Kelvin    ||")
                        print("||   4. Kembali                          ||")
                        print("===========================================")
                        choise = input("Masukan Perhitungan yang diinginkan: ")
                        if choise.isdigit():
                            choise = int(choise)
                            if choise == 1:
                                convert_reamur_to_celcius = reamur_to_celsius(reamur)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Reamur ke Celcius adalah", convert_reamur_to_celcius ,"C")
                                print("---------------------------------------------------------------")
                            elif choise == 2 :
                                convert_reamur_to_farenheit = reamur_to_fahrenheit(reamur)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Reamur ke Farenheit adalah", convert_reamur_to_farenheit ,"F")
                                print("---------------------------------------------------------------")
                            elif choise == 3:
                                convert_reamur_to_kelvin = reamur_to_kelvin(reamur)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Reamur ke Kelvin adalah", convert_reamur_to_kelvin ,"K")
                                print("---------------------------------------------------------------")
                            elif choise == 4 :
                                break
                            else :
                                print("Pilihlah sesuai pilihan yang ada !!")
                        elif choise.strip() == "":
                            print("Tidak boleh kosong, harus memilih !!")
                        else :
                            print("Hanya bisa memasukkan nomor yang tertera !!")
                elif reamur.strip() == "":
                    print("Nilai Reamur tidak boleh kosong")
                else :
                    print("Hanya bisa memasukkan angka, coba lagi!!")
        elif choose == 3 :
            valid_farenheit = False
            while not valid_farenheit:
                farenheit = input("Masukan Nilai Farenheit: ")
                if farenheit.isdigit():
                    farenheit = float(farenheit)
                    valid_farenheit = True
                    while True :
                        print("===========================================")
                        print("||        Perhitungan Farenheit           ||")
                        print("===========================================")
                        print("||   1. Perhitungan Farenheit ke Reamur   ||")
                        print("||   2. Perhitungan Farenheit ke Celcius  ||")
                        print("||   3. Perhitungan Farenheit ke Kelvin   ||")
                        print("||   4. Kembali                           ||")
                        print("===========================================")
                        choise = input("Masukan Perhitungan yang diinginkan: ")
                        if choise.isdigit():
                            choise = int(choise)
                            if choise == 1:
                                convert_farenheit_to_reamur = farenheit_to_reaamur(farenheit)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Farenheit ke Reamur adalah", convert_farenheit_to_reamur ,"R")
                                print("---------------------------------------------------------------")
                            elif choise == 2 :
                                convert_farenheit_to_celcius = farenheit_to_celsius(farenheit)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Farenheit ke Celcius adalah", convert_farenheit_to_celcius ,"C")
                                print("---------------------------------------------------------------")
                            elif choise == 3:
                                convert_farenheit_to_kelvin = farenheit_to_kelvin(farenheit)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Farenheit ke Kelvin adalah", convert_farenheit_to_kelvin ,"K")
                                print("---------------------------------------------------------------")
                            elif choise == 4 :
                                break
                            else :
                                print("Pilihlah sesuai pilihan yang ada !!")
                        elif choise.strip() == "":
                            print("Tidak boleh kosong, harus memilih !!")
                        else :
                            print("Hanya bisa memasukkan nomor yang tertera !!")
                elif farenheit.strip() == "":
                    print("Nilai Farenheit tidak boleh kosong")
                else :
                    print("Hanya bisa memasukkan angka, coba lagi!!")
        elif choose == 4 :
            valid_kelvin = False
            while not valid_kelvin:
                kelvin = input("Masukan Nilai Kelvin: ")
                if kelvin.isdigit():
                    kelvin = float(kelvin)
                    valid_kelvin = True
                    while True :
                        print("===========================================")
                        print("||        Perhitungan Kelvin             ||")
                        print("===========================================")
                        print("||   1. Perhitungan Kelvin ke Reamur     ||")
                        print("||   2. Perhitungan Kelvin ke Farenheit  ||")
                        print("||   3. Perhitungan Kelvin ke Celcius    ||")
                        print("||   4. Kembali                          ||")
                        print("===========================================")
                        choise = input("Masukan Perhitungan yang diinginkan: ")
                        if choise.isdigit():
                            choise = int(choise)
                            if choise == 1:
                                convert_kelvin_to_reamur = kelvin_to_reamur(kelvin)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Kelvin ke Reamur adalah", convert_kelvin_to_reamur ,"R")
                                print("---------------------------------------------------------------")
                            elif choise == 2 :
                                convert_kelvin_to_farenheit = kelvin_to_fahrenheit(kelvin)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Kelvin ke Farenheit adalah", convert_kelvin_to_farenheit ,"F")
                                print("---------------------------------------------------------------")
                            elif choise == 3:
                                convert_kelvin_to_celcius = kelvin_to_celsius(kelvin)
                                print("---------------------------------------------------------------")
                                print("Hasil dari konversi Suhu Kelvin ke Celcius adalah", convert_kelvin_to_celcius ,"C")
                                print("---------------------------------------------------------------")
                            elif choise == 4 :
                                break
                            else :
                                print("Pilihlah sesuai pilihan yang ada !!")
                        elif choise.strip() == "":
                            print("Tidak boleh kosong, harus memilih !!")
                        else :
                            print("Hanya bisa memasukkan nomor yang tertera !!")
                elif kelvin.strip() == "":
                    print("Nilai Kelvin tidak boleh kosong")
                else :
                    print("Hanya bisa memasukkan angka, coba lagi!!")
        elif choose == 5 :
            print("\n")
            print("=========================================================")
            print("Terima kasih telah menggunakan Sistem Sederhana kami 😊")
            print("=========================================================")
            print("\n")
            break
        else :
            print("Pilihlah sesuai pilihan yang ada !!")
    elif choose.strip() == "":
        print("Pilihan tidak boleh kosong !!")
    else :
        print("Hanya bisa menginputkan sebuah angka !!")








