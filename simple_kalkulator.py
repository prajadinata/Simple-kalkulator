def kalkulator():
    print("---- Kalkulator Sederhana ----")
    print("------------------------------\n")

    try:
        angka_1 = float(input("Masukkan angka pertama: "))
        operator = input("Pilih operasi (+, -, *, /): ")
        angka_2 = float(input("Masukkan angka kedua: "))

        print("\n------------------------------")

        if operator == "+":
            hasil = angka_1 + angka_2
            print(f"Hasilnya adalah: {hasil}")

        elif operator == "-":
            hasil = angka_1 - angka_2
            print(f"Hasilnya adalah: {hasil}")

        elif operator == "*":
            hasil = angka_1 * angka_2
            print(f"Hasilnya adalah: {hasil}")

        elif operator == "/":
            if angka_2 != 0:
                hasil = angka_1 / angka_2
                print(f"Hasilnya adalah: {hasil}")
                print(f"Jika dibulatkan: {round(hasil)}")
            else:
                print("Error: Tidak bisa membagi dengan nol.")

        else:
            print("Operator tidak dikenali. Gunakan hanya +, -, *, atau /.")

    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka dengan benar.")

# Panggil fungsi kalkulator
kalkulator()
