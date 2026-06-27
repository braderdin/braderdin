import re
import random
from datetime import datetime
import pytz

def generate_dynamic_stats():
    tz_my = pytz.timezone('Asia/Kuala_Lumpur')
    waktu_sekarang = datetime.now(tz_my)
    masa_formatted = waktu_sekarang.strftime('%d-%m-%Y %I:%M %p (Waktu Malaysia)')
    
    # Koleksi misi garaj / status rawak hari ini daripada fail draf abang
    misi_hari_ini = [
        "Merisik laluan kembara konvoi baru ke utara sempadan... 🗺️",
        "Tengah asah skill color grading CapCut untuk footage kamera... 🎞️",
        "Ngopi sat layan Kopi O Charger pekat... ☕",
        "Berhempas-pulas cuba fahamkan logik skrip Python... 🧪",
        "Menggali sejarah peradaban lama, dari empayar Rom ke Tanah Siam... 📜",
        "Berehat di pit-stop sambil layan lore terbaru One Piece & Bleach... 🌸",
        "Cuci dan kilatkan jentera di garaj sebelum ride hujung minggu... 🏍️",
        "Kemas kini storan aset digital & gambar di Shutterstock... 🚀"
    ]
    
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
    print("🤖 Memulakan proses suntikan profil utama...")
    stats_baru = generate_dynamic_stats()
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()

        # FORMULA REGEX DIBAIKI DENGAN BETUL KEMBALI
        pattern = r'(<!--\s*START_GARAJ_STATS\s*-->)(.*?)(<!--\s*END_GARAJ_STATS\s*-->)'
        if re.search(pattern, readme_content, flags=re.IGNORECASE | re.DOTALL):
            new_readme = re.sub(pattern, rf'\g<1>\n{stats_baru}\n\g<3>', readme_content, flags=re.IGNORECASE | re.DOTALL)
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_readme)
            
            tz_my = pytz.timezone('Asia/Kuala_Lumpur')
            waktu_log = datetime.now(tz_my).strftime('%d-%m-%Y %I:%M %p')
            print(f"✅ README berjaya dikemas kini pada {waktu_log}")
        else:
            print("❌ Ralat: Tag START_GARAJ_STATS tidak dijumpai di dalam fail README.md")
    except Exception as e:
        print(f"❌ Berlaku ralat semasa membaca/menulis fail: {e}")

if __name__ == "__main__":
    update_readme()