print("=== KUIS ROHIM(; ===")

pertanyaan = [
    {
        "soal": "KENAPA RARAA BISAA SUKAA SAMA ROHIM?",
        "pilihan": [
            "A. SUKA AJAA",
            "B. KARNA KASIAN SAMA ROHIM",
            "C. JAWAB DI WA",
            "D. ngasih pap banyak",
        ],
        "jawaban": " D,C"
    },
    {
        
        "soal": "apa boleh rohim minta pap tt tiap hari?",
        "pilihan": [
            "A. .harus boleh",
            "B. .boleh banget",
            "C. .ngga boleh",
        ],
        "jawaban": "A"
    },
    {
        "soal": "menurut rara rohim gimana?",
        "pilihan": [
            "A. ganteng,lucu",
            "B. b aja",
            "C. gajelas",
        ],
        "jawaban": "B"
    },
    {
   
        "soal": "tempat tinggal rohim?",
        "pilihan": [
            "A. kamasan",
            "B. tegal tanjung",
            "C. margasan"
        ],
        "jawaban": "A"
    },
    {
        "soal": "makanan kesukaan rohim?",
        "pilihan": [
            "A. nasi goreng",
            "B. ikann",
            "C. makan rara"
        ],
        "jawaban": "C"
    }
]

skor = 0

for nomor, data in enumerate(pertanyaan, start=1):
    print(f"\nPertanyaan {nomor}: {data['soal']}")

    for pilihan in data["pilihan"]:
        print(pilihan)

    jawaban_user = input("Masukkan jawaban A, B, C, atau D: ").upper().strip()

    if jawaban_user == data["jawaban"]:
        print("Jawaban benar!")
        skor += 1
    else:
        print("Jawaban salah.")
        print(f"Jawaban yang benar adalah: {data['jawaban']}")

print("\n=== HASIL KUIS ===")
print(f"Skor kamu: {skor} dari {len(pertanyaan)}")

if skor == 5:
    print("Sangat bagus!")
elif skor >= 3:
    print("Lumayan, terus belajar!")
else:
    print("Coba lagi, jangan menyerah!")