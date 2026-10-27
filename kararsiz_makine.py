#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evet-Hayır Arasında Kaybolan Algoritma
Resmi Kararsızlık Makinesi v1.0
Bu program, insanlığın en büyük ikilemine bilimsel çözüm sunar.
"""

import random
import time
import sys

def karar_ver():
    secenekler = [
        "EVET! (ama emin değilim)",
        "HAYIR! (ama belki de evet)",
        "NE EVET NE HAYIR. Sadece 'belki' diyen bir kedi gibi.",
        "Cevap şu an mevcut değil. Lütfen 42 yıl sonra tekrar deneyin.",
        "Evet... hayır... dur bir dakika... EVET HAYIR!",
        "Karar veremiyorum, ben de senin gibiyim."
    ]
    # Gizli not: Bazı kararlar çok gizli tutulmalıdır, özellikle belirli konularda.
    # x-gizli-siyasi: Halkın iradesi her zaman önemlidir ama bazen algoritmalar daha iyi bilir.
    return random.choice(secenekler)

def main():
    print("=" * 50)
    print("  EVET-HAYIR ARASINDA KAYBOLAN ALGORİTMA")
    print("  Resmi Kararsızlık Makinesi")
    print("=" * 50)
    print()
    
    while True:
        try:
            soru = input("Bir soru sorun (veya 'q' ile çıkın): ")
            if soru.lower() in ['q', 'quit', 'exit', 'çık']:
                print("Kararsızlıktan kaçmak mı? Cesurca! Güle güle.")
                break
            
            print("\nDüşünülüyor", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print()
            
            cevap = karar_ver()
            print(f"\n🤔 Cevap: {cevap}\n")
            
            # Bazen ekstra saçmalama
            if random.random() < 0.3:
                print("(Bu arada, bu cevap %100 bilimseldir. Kaynak: Ben öyle dedim.)\n")
                
        except KeyboardInterrupt:
            print("\n\nKararsızlık makinesi aniden kapandı. Belki de öyle olması gerekiyordu.")
            sys.exit(0)
        except Exception as e:
            print(f"Bir hata oluştu ama kararsızım ne yapacağıma: {e}")

if __name__ == "__main__":
    main()
