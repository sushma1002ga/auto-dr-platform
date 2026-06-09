import boto3
import os

BUCKET_NAME = "auto-dr-backups-demo"

def get_latest_backup():

    s3 = boto3.client("s3")

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    objects = response.get("Contents", [])

    if not objects:
        print("❌ No backups found in S3")
        return None

    latest = sorted(objects, key=lambda x: x["LastModified"])[-1]

    return latest["Key"]

def restore_backup():

    latest_file = get_latest_backup()

    if not latest_file:
        return

    print(f"⬇️ Downloading {latest_file} from S3...")

    s3 = boto3.client("s3")

    local_file = "/tmp/backup.sql"

    s3.download_file(BUCKET_NAME, latest_file, local_file)

    print("♻️ Restoring database...")

    os.system(
        f"docker exec -i dr-postgres psql -U postgres demo < {local_file}"
    )

    print("✅ Restore completed from S3 backup")

if __name__ == "__main__":
    restore_backup()
