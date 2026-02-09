from supabase import create_client
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
import random

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# ---- Sensor read functions (replace with real ones later) ----
def read_ph():
    return round(7 + (random.random() - 0.5) * 1.0, 2)          # ~6.5–7.5

def read_temperature():
    return round(26 + (random.random() - 0.5) * 4, 2)          # ~24–28 °C

def read_turbidity():
    return round(3 + random.random() * 2, 2)                   # NTU-ish

def read_water_level():
    return round(60 + (random.random() - 0.5) * 20, 2)         # cm

# ------------------------------------------------------------

def collect_readings():
    now = datetime.now(timezone.utc).isoformat()

    return [
        {
            "sensor_id": "sensor_ph_1",
            "value": read_ph(),
            "recorded_at": now,
        },
        {
            "sensor_id": "sensor_temp_1",
            "value": read_temperature(),
            "recorded_at": now,
        },
        {
            "sensor_id": "sensor_turbidity_1",
            "value": read_turbidity(),
            "recorded_at": now,
        },
        {
            "sensor_id": "sensor_water_1",
            "value": read_water_level(),
            "recorded_at": now,
        },
    ]

def insert_readings():
    readings = collect_readings()
    result = supabase.table("readings").insert(readings).execute()
    print("Inserted:", len(readings))

if __name__ == "__main__":
    insert_readings()
