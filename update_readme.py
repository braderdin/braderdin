import random
from datetime import datetime
import pytz

def generate_dynamic_stats():
    # Tetapkan zon masa Malaysia (Kuala Lumpur)
    tz_my = pytz.timezone('Asia/Kuala_Lumpur')
    masa_sekarang = datetime.now(tz_my).strftime('%d-%m-%Y %I:%M %p')

    # Senarai status/misi rider secara santai & rawak
    misi_hari_ini = [
        "Memburu kabut pagi di sempadan Thailand... 🗺️",
        "Tengah selenggara jentera kesayangan dekat garaj... 🔧",
        "Ngopi sat layan Kopi O Charger pekat... ☕",
        "Tengah pening kepala hadap skrip koding & bug Eleventy... 🧪",
        "Dok usha laluan cross-border seterusnya dekat peta... 🏁",
        "Berehat sambil layan anime One Piece & Bleach... 🌸",
        "Tengah proses footage video 360 layan korner... 📷",
        "Kemas kini storan gambar jentera dekat Imgur... 🚀"
    ]
    
    status_pilihan = random.choice(misi_hari_ini)
    stamina = random.randint(75, 100)
    mood_ride = random.randint(80, 100)

    # Bina bar progress grafik mudah
    def buat_bar(nilai):
        blok = int(nilai / 10)
        return "█" * blok + "░" * (10 - blok)

    content = f"""
> 🗓️ **Kemas Kini Terakhir:** `{masa_sekarang} (Waktu Malaysia)`
>
> 🚩 **Misi Hari Ini:** `{status_pilihan}`

| Statistik Rider | Tahap Status | Bar Grafik |
| :--- | :---: | :--- |
| ☕ **Stamina (Kopi O Charger)** | `{stamina}%` | `[{buat_bar(stamina)}]` |
| 🗺️ **Mood Ride (Lapar Jalan Jauh)** | `{mood_ride}%` | `[{buat_bar(mood_ride)}]` |
"""
    return content

def update_readme():
    stats_baru = generate_dynamic_stats()
    
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Cari kedudukan penanda (comment tags) dalam README
    start_tag = "<!-- START_GARAJ_STATS -->"
    end_tag = "<!-- END_GARAJ_STATS -->"
    
    start_idx = readme_content.find(start_tag) + len(start_tag)
    end_idx = readme_content.find(end_tag)

    if start_idx != -1 and end_idx != -1:
        # Ganti kandungan lama di antara tag dengan statistik baru
        new_readme = readme_content[:start_idx] + "\n" + stats_baru + "\n" + readme_content[end_idx:]
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("README berjaya dikemas kini, bang!")
    else:
        print("Ralat: Penanda tag tidak dijumpai dalam README.md")

if __name__ == "__main__":
    update_readme()