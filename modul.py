stok = [
    {"nama" : "handphone", "jumlah" : 12},
    {"nama" : "tablet", "jumlah" : 10}
    
]
def tambah_data ():
    nama_barang = str(input("masukan nama barang : ")).lower()
    jumlah = int(input("masukan stok barang : "))

    stok_baru = {f"nama": nama_barang, "jumlah" : jumlah }
    stok.append(stok_baru)
    print("\n")
    print("data berhasil ditambahkan")
    print("\n")

def edit_data ():
    index = int(input("masukan data index ke : "))
    nama_baru = str(input("masukan nama barang :"))
    jumlah_baru = int(input("masukan stok :"))

    stok_baru = [("nama",nama_baru),("jumlah",jumlah_baru) ]
    stok[index].update(stok_baru)
    print("\n")
    print("data telah diubah")
    print("\n")

def hapus_data():
    hapus = int(input("hapus data index ke : "))
    stok.pop(hapus)
    print("\n")
    print("data berhasil dihapus")
    print("\n")

def tampil_data():
    print("====daftar barang============")
    for i in stok:
        print(f"{i['nama']} : {i['jumlah']}")
    print("\n")

def cari_data():
    print("========hasil pencarian============")
    items = []
    cari = str(input("data yang akan dicari :")).lower()
    for i in stok :
        if cari in i["nama"] :
            items.append(i)
    if items :
        for item in items :  
            print(f"{item['nama']} : {item['jumlah']}")
    else : 
        print("tidak ada data dengan nama", cari)
    print("\n")

def jumlah_data():
    print("=========jumlah data==========")
    print(f"terdapat {len(stok)} data")
    print("\n")