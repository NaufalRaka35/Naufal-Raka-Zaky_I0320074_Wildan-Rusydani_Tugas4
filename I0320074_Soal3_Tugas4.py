#  beban bagasi maksimal
bebanmaks_lbs = 50
bebanmaks_kg = bebanmaks_lbs * 0.453592
beban110 = 110
beban49 = 49

seleksipertama = bebanmaks_kg > beban110
print(seleksipertama)

seleksikedua = bebanmaks_kg > beban49
print(seleksikedua)