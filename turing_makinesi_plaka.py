class TuringMakinesi:
    def __init__(self, plaka):
        # bant yapısı
        self.bant = list(plaka) + ['_']  # boşluk sembolü
        self.kafa = 0

        # durumlar
        self.durum = 'q0'
        self.kabul = 'q_kabul'
        self.red = 'q_red'

        self.adim = 1

        
        self.rakamlar = "0123456789"
        self.harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # geçiş fonksiyonu
        self.gecisler = self.gecis_fonksiyonu_olustur()

    def gecis_fonksiyonu_olustur(self):
        gecis = {}

        # q0 ilk rakam
        for r in self.rakamlar:
            gecis[('q0', r)] = ('q1', r, 'R')

        # q1 ikinci rakam
        for r in self.rakamlar:
            gecis[('q1', r)] = ('q2', r, 'R')

        # q2 ilk büyük harf
        for h in self.harfler:
            gecis[('q2', h)] = ('q3', h, 'R')

        # q3 ikinci büyük harf
        for h in self.harfler:
            gecis[('q3', h)] = ('q4', h, 'R')

        # q4 ilk rakam
        for r in self.rakamlar:
            gecis[('q4', r)] = ('q5', r, 'R')

        # q5 ikinci rakam
        for r in self.rakamlar:
            gecis[('q5', r)] = ('q6', r, 'R')

        # q6 üçüncü rakam
        for r in self.rakamlar:
            gecis[('q6', r)] = ('q7', r, 'R')

        # q7 yalnızca boşluk gelirse kabul
        gecis[('q7', '_')] = (self.kabul, '_', 'S')

        return gecis

    def bant_yazdir(self, okunan, yazilan, yon):
        bant_gorunum = "".join(self.bant)

        bilgi = (
            f"Adım: {self.adim} | "
            f"Durum: {self.durum} | "
            f"Okunan: {okunan} | "
            f"Yazılan: {yazilan} | "
            f"Hareket: {yon}"
        )

        print(bilgi)
        print("Bant :", bant_gorunum)
        print("       " + " " * self.kafa + "^")
        print("-" * 60)

    def calistir(self):

        print("\nTuring Makinesi Başlatıldı")
        print("Girdi:", "".join(self.bant).replace("_", ""))
        print("-" * 60)

        while self.durum not in [self.kabul, self.red]:

            # bant sonuna çıkılırsa boşluk oku
            if self.kafa >= len(self.bant):
                okunan = '_'
            else:
                okunan = self.bant[self.kafa]

            anahtar = (self.durum, okunan)

            # geçiş varsa
            if anahtar in self.gecisler:

                yeni_durum, yazilan, yon = self.gecisler[anahtar]

                # banda yaz
                self.bant[self.kafa] = yazilan

                # adımı göster
                self.bant_yazdir(okunan, yazilan, yon)

                # durum değiştir
                self.durum = yeni_durum

                # kafa hareketi
                if yon == 'R':
                    self.kafa += 1

                elif yon == 'L':
                    self.kafa -= 1

            else:
                # tanımsız geçiş: RED
                self.bant_yazdir(okunan, okunan, 'S')
                self.durum = self.red

            self.adim += 1

        # sonuç
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