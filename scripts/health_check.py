import psycopg2
import time
import os

recovery_in_progress = False

while True:

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="demo",
            user="postgres",
            password="postgres"
        )

        conn.close()

        print("✅ Database Healthy")
        recovery_in_progress = False

    except Exception:

        if not recovery_in_progress:

            print("❌ Database Failure Detected")
            print("🚨 Triggering Recovery Once")

            recovery_in_progress = True

            os.system("python scripts/restore.py")

        else:
            print("⏳ Recovery already in progress... waiting")

    time.sleep(5)
