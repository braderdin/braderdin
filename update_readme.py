import random
from datetime import datetime
import pytz

def generate_dynamic_stats():
    tz_my = pytz.timezone('Asia/Kuala_Lumpur')
    waktu_sekarang = datetime.now(tz_my)
    masa_formatted = waktu_sekarang.strftime('%d-%m-%Y %I:%M %p (Waktu Malaysia)')
    
    # Koleksi misi garaj / status rawak hari ini daripada draf abang
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
    
    start_tag = "<!-- START_GARAJ_STATS -->"
    end_tag = "<!-- END_GARAJ_STATS -->"
    
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()

        if start_tag in readme_content and end_tag in readme_content:
            # Teknik Memecah Teks Gaya Pro (Bebas ralat regex)
            bahagian_atas = readme_content.split(start_tag)[0]
            bahagian_bawah = readme_content.split(end_tag)[1]
            
            new_readme = f"{bahagian_atas}{start_tag}\n{stats_baru}\n{end_tag}{bahagian_bawah}"
            
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_readme)
            
            print("✅ README berjaya dikemas kini tanpa ralat!")
        else:
            print("❌ Ralat: Tag penanda tidak dijumpai di dalam fail README.md")
    except Exception as e:
        print(f"❌ Berlaku ralat semasa membaca/menulis fail: {e}")

if __name__ == "__main__":
    update_readme()
