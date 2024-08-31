No 2

name = 'Dicoding Indonesia'
print(f"Hello, saya belajar coding di {name}")

No 3

data = ['dress', 'red']
apparel, color = data
print(apparel)
print(color)

no 4

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

no 5

x = { 'name': 'Coding', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"
print(x)

no 11

lulus = True 
print("Dicoding Indonesia") if lulus else print ("Python")

no 14

def luas_persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    return luas

print(luas_persegi_panjang(10,5))

def greeting(nama):
    print(f"Halo {nama}")

greeting("Aco")


no 15
var keyword
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

no 17
atribut instance
class Mobil:
    def __init__(self):
        self.warna = 'Merah'

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)



atribut kelas
class Mobil:
    warna = "Merah"

print(Mobil.warna)