class TuringMakinesi:
    BLANK = '_'

    def __init__(self, plaka):
        self.bant = list(plaka) + [self.BLANK]
        self.kafa = 0

        self.baslangic = "q_ilk_rakam"
        self.kabul = "q_kabul"
        self.red = "q_red"

        self.durum = self.baslangic
        self.adim = 1

        self.rakamlar = "0123456789"
        self.buyuk_harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"

        self.gecisler = self.gecis_fonksiyonu_olustur()

    def gecis_fonksiyonu_olustur(self):
        gecis = {}

        def red_ekle(durum, semboller):
            for s in semboller:
                gecis[(durum, s)] = (self.red, s, 'R')

        tum_harfler = self.buyuk_harfler + self.kucuk_harfler
        # 1. karakter -> rakam
        for r in self.rakamlar:
            gecis[("q_ilk_rakam", r)] = ("q_ikinci_rakam", r, 'R')
        red_ekle("q_ilk_rakam", tum_harfler + self.BLANK)
        # 2. karakter -> rakam
        for r in self.rakamlar:
            gecis[("q_ikinci_rakam", r)] = ("q_ilk_harf", r, 'R')
        red_ekle("q_ikinci_rakam", tum_harfler + self.BLANK)
        # 3. karakter -> büyük harf
        for h in self.buyuk_harfler:
            gecis[("q_ilk_harf", h)] = ("q_ikinci_harf", h, 'R')
        red_ekle("q_ilk_harf", self.rakamlar + self.kucuk_harfler + self.BLANK)
        # 4. karakter -> büyük harf
        for h in self.buyuk_harfler:
            gecis[("q_ikinci_harf", h)] = ("q_son_rakam_1", h, 'R')
        red_ekle("q_ikinci_harf", self.rakamlar + self.kucuk_harfler + self.BLANK)
        # 5. karakter -> rakam
        for r in self.rakamlar:
            gecis[("q_son_rakam_1", r)] = ("q_son_rakam_2", r, 'R')
        red_ekle("q_son_rakam_1", tum_harfler + self.BLANK)
        # 6. karakter -> rakam
        for r in self.rakamlar:
            gecis[("q_son_rakam_2", r)] = ("q_son_rakam_3", r, 'R')
        red_ekle("q_son_rakam_2", tum_harfler + self.BLANK)
        # 7. karakter -> rakam
        for r in self.rakamlar:
            gecis[("q_son_rakam_3", r)] = ("q_kontrol", r, 'R')
        red_ekle("q_son_rakam_3", tum_harfler + self.BLANK)
        # giriş bitti mi kontrolü
        gecis[("q_kontrol", self.BLANK)] = (self.kabul, self.BLANK, 'S')

        tum_karakterler = (
            self.rakamlar +
            self.buyuk_harfler +
            self.kucuk_harfler
        )
        red_ekle("q_kontrol", tum_karakterler)

        return gecis

    def bant_yazdir(self, okunan, yazilan, yon):
        bant_gorunum = "".join(self.bant)

        print(
            f"Adım: {self.adim:<2} | "
            f"Durum: {self.durum:<18} | "
            f"Okunan: {okunan} | "
            f"Yazılan: {yazilan} | "
            f"Yön: {yon} | "
            f"Bant: {bant_gorunum}"
        )

        print(" " * 79 + " " * self.kafa + "^")

    def calistir(self):
        print("\nTuring Makinesi Başlatıldı")
        print("Girdi:", "".join(self.bant).replace(self.BLANK, ""))
        print("-" * 60)
        while self.durum not in [self.kabul, self.red]:
            if self.kafa >= len(self.bant):
                self.bant.append(self.BLANK)
            okunan = self.bant[self.kafa]
            anahtar = (self.durum, okunan)
            if anahtar in self.gecisler:
                yeni_durum, yazilan, yon = self.gecisler[anahtar]
                self.bant[self.kafa] = yazilan
                self.bant_yazdir(okunan, yazilan, yon)
                self.durum = yeni_durum
               
                if yon == 'R':
                    self.kafa += 1
                elif yon == 'L':
                    self.kafa -= 1
                elif yon == 'S':
                    pass
            else:
                self.bant_yazdir(okunan, okunan, 'S')
                self.durum = self.red
            self.adim += 1
        if self.durum == self.kabul:
            print("\nSONUÇ: KABUL")
        else:
            print("\nSONUÇ: RED")
def main():

    while True:
        plaka = input("\nPlaka giriniz (Çıkmak için q): ")
        if plaka.lower() == 'q':
            print("Program sonlandırıldı.")
            break
        tm = TuringMakinesi(plaka)
        tm.calistir()

if __name__ == "__main__":
    main()
