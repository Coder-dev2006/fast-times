def son_hisobla():
    sonlar = []
    while True:
        son = input("Istalgancha son kiriting "
                    "\nMen ularni ko'paytmasini hisoblab beraman "
                    "\nSon kiritib bo'lgach, 'stop' buyrug'ini bering: ")
        if son.lower() == "stop":
            break
        try:
            sonlar.append(float(son))
        except ValueError:
            print("Iltimos, faqat son kiriting yoki 'stop' deb yozing!")

    # ko‘paytmani hisoblash
    kupaytma = 1
    for s in sonlar:
        kupaytma *= s

    print(f"Kiritilgan sonlar: {sonlar}")
    print(f"Sonlar ko‘paytmasi: {kupaytma}")


son_hisobla()



