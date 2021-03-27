umur = 21
a = int(input("Berapa Usia Anda :"))
if umur <= a :
    print("Anda cukup umur")
    b = input("Apakah Anda sudah lulus ujian kualifikasi (B/T) :")
    if b == "B" :
        print("Anda dapat mendaftar di kursus")
    elif b == "T" :
        print("Anda tidak dapat mendaftar di kursus.")
else :
    print("Anda belum cukup umur")