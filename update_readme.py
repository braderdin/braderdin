import re
import random
from datetime import datetime
import pytz

def generate_dynamic_stats():
    tz_my = pytz.timezone('Asia/Kuala_Lumpur')
    masa_sekarang = datetime.now(tz_my).strftime('%d-%m-%Y %I:%M %p')

    misi_hari_ini = [
        "Merisik laluan kembara konvoi baru... 🗺️",
        "Tengah asah skill color grading CapCut... 🎞️",
        "Ngopi sat layan Kopi O Charger pekat... ☕",
        "Berhempas-pulas cuba fahamkan logik skrip Python... 🧪",
        "Menggali sejarah peradaban lama... 📜",
        "Berehat di pit-stop sambil layan anime... 🌸",
        "Cuci dan kilatkan jentera di garaj... 🏍️",
        "Kemas kini storan aset digital... 🚀"
    ]
    
    status_pilihan = random.choice(misi_hari_ini)
    stamina = random.randint(70, 100)
    mood_ride = random.randint(85, 100)

    def buat_bar(nilai):
        blok = int(nilai / 10)
        return "█" * blok + "░" * (10 - blok)

    return f"""
> 🗓️ **Kemas Kini Terakhir:** `{masa_sekarang}`
> 🚩 **Misi Semasa:** `{status_pilihan}`

| 📊 Indikator Profil | Tahap (%) | Bar Grafik |
| :--- | :---: | :--- |
| ☕ **Stamina Fizikal** | `{stamina}%` | `{buat_bar(stamina)}` |
| 🛣️ **Keterujaan Ride** | `{mood_ride}%` | `{buat_bar(mood_ride)}` |
"""

def update_readme():
    stats_baru = generate_dynamic_stats()
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()

        pattern = r'(<!--\s*START_GARAJ_STATS\s*-->)(.*?)(<!--\s*END_GARAJ_STATS\s*-->)'
        if re.search(pattern, readme_content, flags=re.IGNORECASE | re.DOTALL):
            new_readme = re.sub(pattern, rf'\g<1>\n{stats_baru}\n\g<3>', readme_content, flags=re.IGNORECASE | re.DOTALL)
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_readme)
            print("✅ README berjaya dikemas kini!")
    except Exception as e:
        print(f"❌ Ralat: {e}")

if __name__ == "__main__":
    update_readme()