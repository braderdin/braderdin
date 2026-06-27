import urllib.request
import json
from datetime import datetime
import pytz

def ambil_cuaca(nama_tempat, lat, lon):
    # Menggunakan API Cuaca Open-Meteo (Percuma & Bebas Kunci API)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=Asia%2FKuala_Lumpur"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode())
            return res_data['current']
    except Exception as e:
        print(f"❌ Ralat mengambil data cuaca {nama_tempat}: {e}")
        return None

def tukar_kod_cuaca(code):
    # Menukar kod data kepada indikator status rider yang santai
    if code == 0: 
        return "☀️ Cerah Benderang (Ngam sangat pulas throttle layan ride)"
    elif code in [1, 2, 3]: 
        return "⛅ Redup / Berawan (Cuaca redup selesa menunggang)"
    elif code in [45, 48]: 
        return "🌫️ Berkabut Tebal (Pasang lampu hazard, tunggang berhati-hati)"
    elif code in [51, 53, 55, 61, 63, 65]: 
        return "🌧️ Hujan / Renyai (Masa untuk sedia baju hujan atau pitstop ngeteh dulu ☕)"
    elif code in [80, 81, 82, 95, 96, 99]: 
        return "🌩️ Ribut Petir Kencang (Berteduh dulu bang, utamakan keselamatan!)"
    return "🌤️ Cuaca Normal"

def main():
    print("🌦️ Memulakan semakan cuaca laluan kembara...")
    tz_my = pytz.timezone('Asia/Kuala_Lumpur')
    masa_formatted = datetime.now(tz_my).strftime('%d-%m-%Y %I:%M %p (Waktu Malaysia)')
    
    # Ambil data live daripada koordinat geografi sebenar
    cuaca_rawang = ambil_cuaca("Rawang", "3.3211", "101.5779")
    cuaca_hatyai = ambil_cuaca("Hatyai", "7.0084", "100.4747")
    
    if not cuaca_rawang or not cuaca_hatyai:
        print("❌ Gagal menjana log disebabkan ralat data API.")
        return

    # Reka bentuk paparan visual widget dashboard yang kemas dan berstail pro
    md_content = f"""# 🌦️ Laporan Cuaca Live: Garaj & Laluan Kembara 🏍️

> 🗓️ **Kemas Kini Terakhir:** `{masa_formatted}`  
> *Sistem automasi terasing dipandu sepenuhnya oleh Python & GitHub Actions.*

---

## 🏠 1. Pangkalan Utama: Rawang, Selangor
```text
🌡️ Suhu Semasa    : {cuaca_rawang['temperature_2m']}°C
💧 Kelembapan Udara : {cuaca_rawang['relative_humidity_2m']}%
💨 Kelajuan Angin   : {cuaca_rawang['wind_speed_10m']} km/h
📊 Status Laluan    : {tukar_kod_cuaca(cuaca_rawang['weather_code'])}
