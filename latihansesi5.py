# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0 

while(True):
    nama_barang = input("masukan nama barang :")
    harga_barang = input("masukan harga barang :")
    persen = input("masukan persen barang")
    barang_terjual = int(input("masukan jumlah barang terjual"))

    harga_keuntungan = int(harga_barang) * int(persen) /100
    harga_jual = int(harga_barang) + harga_keuntungan

    #Menghitung modal
    modal = haga_barang + barang_terjual
    print(nama_barang, 'dijual dengan: ',harga_jual)
    modal_keseluruhan = modal_keseluruhan + modal

    #menghitung laba
    laba = keuntungan_persen * barang_terjual
    #menghitung laba keseluruan 
    laba_keseluruhan = laba_keseluruhan + laba

    print("barang", nama_barang)
    print("harga barang", harga_barang)
    print("keuntungan per barang", keuntungan_persen)
    print("dijual dengan harga", harga_jual)
    print("terjual", barang_terjual)
    print("modal", modal)
    print("laba", laba)

    apakahlanjut = input("apakah ingin input barang lain? Y lanjut : ")
    if(apakahlanjut != "Y"):
        break 

print("..............")
print("modal keseluruhan", modal_keseluruhan)
print("laba keseluruhan", laba_keseluruhan)