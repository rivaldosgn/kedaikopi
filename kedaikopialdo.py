class MenuKopi:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def get_nama(self):
        return self._nama

    def get_harga(self):
        return self._harga


class AnandaCoffe:
    def __init__(self):
        self._menu = [
            MenuKopi("ES Kopi Susu", 11000),
            MenuKopi("ES Kopi Coklat", 12000),
            MenuKopi("ES Kopi Hitam", 11000),
            MenuKopi("Ice Americano", 14000)
        ]

    def tampilkan_menu(self):
        print("==============================")
        print("Ananda Coffe")
        print("List Menu Minuman Kopi")
        print("==============================")
        for i, item in enumerate(self._menu):
            print(f"{chr(65 + i)}. {item.get_nama()} : Rp {item.get_harga()}")
        print("==============================")

    def pesan_kopi(self):
        pesan = input("Masukkan list abjad menu kopi = ")
        jumlah_pesan = int(input("Masukkan jumlah pesanan = "))

        if pesan.lower() in ["a", "b", "c", "d"]:
            menu_pilihan = self._menu[ord(pesan.lower()) - 97]
            harga = menu_pilihan.get_harga() * jumlah_pesan
            ppn = int(harga * 0.1)

            if jumlah_pesan >= 5:
                diskon = int(harga * 0.2)
                total_harga = harga - diskon + ppn
            else:
                diskon = 0
                total_harga = harga + ppn

            print("--------------------------")
            print("Ananda Coffe")
            print("--------------------------")
            print("Menu :", menu_pilihan.get_nama())
            print("Jumlah Pesan :", jumlah_pesan)
            print("Harga :", harga)
            print("Diskon :", diskon)
            print("PPN :", ppn)
            print("--------------------------")
            print("Jumlah Bayar :", total_harga)
            print("--------------------------")
        else:
            print("Menu tidak tersedia.")

    def jalankan_program(self):
        pilihan = "y"
        while pilihan.lower() == "y":
            self.tampilkan_menu()
            self.pesan_kopi()
            pilihan = input("Apakah Anda ingin order kembali? (Y/N) = ")


kopi = AnandaCoffe()
kopi.jalankan_program()
