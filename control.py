
temperature: float = float(input())

if temperature > 100:
    print("Air berubah menjadi gas.")

elif temperature >= 0 and temperature <= 100:
    print("Air tetap berupa cairan.")

else:
    print("Air berubah menjadi padat.")



isSick: bool = False
temperature: float = float(input())

if temperature >= 38:
    print("Anda mengalami sakit demam.")
    isSick = True

elif temperature > 35 and temperature < 38:
    print("Suhu tubuh Anda normal.")

else:
    print("Anda terjangkit sakit hipotermia.")
    isSick = True

if isSick:
    print("Anda disarankan istirahat atau kunjungi dokter secepatnya.")


feeling = "Letih"

match feeling:
    case "Senang":
        print("Bima Senang")
    case "Letih":
        print("Bima Semangat")
    case _:
        print("Bima Santai")