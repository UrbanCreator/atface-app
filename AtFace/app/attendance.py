import pandas as pd
from datetime import datetime
import os
from app import config

def mark_attendance(name, recorded, file_path=config.ATTENDANCE_FILE):
    if name in recorded:
        return
    now = datetime.now()
    date, time = now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=["Date", "Time", "Name"])

    df.loc[len(df)] = [date, time, "Unknown Face" if name == "Unknown" else name]
    df.to_excel(file_path, index=False)
    recorded.add(name)
