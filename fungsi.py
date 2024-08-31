panjangRuang: float = float(input())
lebarRuang: float = float(input())
tinggiRuang: float = float(input())


def hitungCat(panjangRuang: float, lebarRuang: float, tinggiRuang: float) -> float:
    kelilingRuang = 2 * (panjangRuang + lebarRuang)
    jumlahLiter: float = kelilingRuang * tinggiRuang / 12
    return jumlahLiter


jumlahLiter: float = hitungCat(panjangRuang, lebarRuang, tinggiRuang)
print(f"Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter.")






#####################################

landArea: float = float(input())
width: float = float(input())
length: float = float(input())


def checkArea(landArea: float, width: float, length: float) -> bool:
    buildingArea: float = width * length

    if buildingArea > landArea:
        return False
    else:
        return True


check: bool = checkArea(landArea, width, length)
if check:
    print("Rumah dapat dibangun berdasarkan ketiga nilai tersebut.")
else:
    print("Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut.")


"""
TODO:
 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel permission.
     1.1. Beri informasi bahwa masukan hanya boleh mengizinkan nilai 1 untuk True atau 0 untuk False.
 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data string dan simpan pada variabel city.
 3. Buatlah prosedur bernama checkPermission yang memiliki parameter permission dan city.
     3.1. Gunakan pengondisian untuk memeriksa permission.
          3.1.1. Apabila bernilai False, cetak teks "Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap."
          3.1.2. Apabila bernilai True, cetak teks "Anda dapat membangun rumah di kota {city}."
     3.2. Jalankan prosedur untuk memeriksa berkas
"""

# Tulis kode Anda di bawah ini
permission: int = int(input("nilai 1 untuk True atau 0 untuk False."))
city: str = str(input())


def checkPermission(permission: int, city: str):
    if permission == 1:
        print(f"Anda dapat membangun rumah di kota {city}.")
    elif permission == 0:
        print(f"Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap.")

checkPermission(permission, city)