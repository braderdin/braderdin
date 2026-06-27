import re
import random
from datetime import datetime
import pytz

def generate_dynamic_stats():
    tz_my = pytz.timezone('Asia/Kuala_Lumpur')
    waktu_sekarang = datetime.now(tz_my)
    masa_formatted = waktu_sekarang.strftime('%d-%m-%Y %I:%M %p (Waktu Malaysia)')
    jam = waktu_sekarang.hour

    # Senarai misi rawak umum
    misi_umum = [
        "Merisik laluan kembara konvoi baru... 🗺️",
        "Tengah asah skill color grading CapCut... 🎞️",
        "Berhempas-pulas cuba fahamkan logik skrip Python... 🧪",
        "Menggali sejarah peradaban lama... 📜",
        "Cuci dan kilatkan jentera di garaj... 🏍️",
        "Kemas kini storan aset digital... 🚀"
    ]
    
    # Sentuhan Pro: Misi bertukar mengikut waktu siang/malam
    if 6 <= jam < 18:
        misi_waktu = ["Ngopi sat layan Kopi O Charger pekat... ☕", "Tengah pening layan coding bawah sinaran matahari... ☀️"]
    else:
        misi_waktu = ["Berehat di pit-stop sambil layan anime... 🌸", "Layan ride santai layan angin malam... 🌙"]
        
    misi_hari_ini = misi_umum + misi_waktu
    status_pilihan = random.choice(misi_hari_ini)
    
    stamina = random.randint(70, 100)
    mood_ride = random.randint(85, 100)

    def buat_bar(nilai):
        blok = int(nilai / 10)
        return "█" * blok + "░" * (10 - blok)

    return f"""
> 🗓️ **Kemas Kini Terakhir:** `{masa_formatted}`
>
> 🚩 **Misi Semasa:** `{status_pilihan}`

| 📊 Indikator Profil | Tahap (%) | Bar Grafik |
| :--- | :---: | :--- |
| ☕ **Stamina Fizikal (Caffeine Level)** | `{stamina}%` | `{buat_bar(stamina)}` |
| 🛣️ **Keterujaan Ride (Throttle Therapy)** | `{mood_ride}%` | `{buat_bar(mood_ride)}` |
"""

def update_readme():
    stats_baru = generate_dynamic_stats()
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()

        # MEMBAIKI REGEX PATTERN YANG KOSONG SEBELUM INI
        pattern = r'()(.*?)()'
        if re.search(pattern, readme_content, flags=re.IGNORECASE | re.DOTALL):
            new_readme = re.sub(pattern, rf'\g<1>\n{stats_baru}\n\g<3>', readme_content, flags=re.IGNORECASE | re.DOTALL)
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_readme)
            print("✅ README berjaya dikemas kini dengan gaya pro!")
        else:
            print("⚠️ Penanda tidak dijumpai dalam README.md")
    except Exception as e:
        print(f"❌ Ralat: {e}")

if __name__ == "__main__":
    update_readme()