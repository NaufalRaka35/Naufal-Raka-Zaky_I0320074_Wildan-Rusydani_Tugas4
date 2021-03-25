umur = 21
x = int(input("Berapa Usia Anda :"))
if umur <= x :
    print("Anda cukup umur")
    y = input("Apakah Anda sudah lulus ujian kualifikasi (Y/T) :")
    if y == "Y" :
        print("Anda dapat mendaftar di kursus")
    elif y == "T" :
        print("Anda tidak dapat mendaftar di kursus.")
else :
    print("Anda belum cukup umur")