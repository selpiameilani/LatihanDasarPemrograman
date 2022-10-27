#tugas 6

print(" ============ program grade nilai ============")
input("nama mahasiswa: ")
nilai  = int(input("masukan nilai  : "))
if (nilai >= 90 and nilai <= 100):
    grade = "A"
    predikat = "dengan pujian"
elif (nilai  >= 80 and nilai  < 90 ):
    grade = "B"
    predikat = "sangat memuaskan"
elif (nilai  >= 70 and nilai  < 79):
    grade = "C"
    predikat = "memuaskan"
elif (nilai  >= 60 and nilai < 69):
    grade = "D"
    predikat = "tidak memuaskan"
elif (nilai >= 0 and nilai  < 59):
    grade = "E"
    predikat = "tidak lulus"
else :
    print ("error")

print ("grade anda :", grade)
print ( "nilai: ", nilai)
print ( "predikat: ", predikat)
print (type (nilai))

