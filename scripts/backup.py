import boto3
import os
from datetime import datetime

BUCKET_NAME = "auto-dr-backups-demo"

def create_backup():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"backup_{timestamp}.sql"

    print("📦 Creating DB dump...")

    os.system(
        f"docker exec dr-postgres pg_dump -U postgres demo > {filename}"
    )

    print("☁️ Uploading to S3...")

    s3 = boto3.client("s3")

    s3.upload_file(filename, BUCKET_NAME, filename)

    print(f"✅ Backup uploaded: {filename}")

if __name__ == "__main__":
    create_backup()
