import glob
import os

container_name = "dr-postgres"

# Step 1: ensure container is running
print("🔄 Starting database container...")

os.system(f"docker start {container_name}")

# Step 2: wait for DB to be ready
print("⏳ Waiting for DB to initialize...")
os.system("sleep 5")

# Step 3: find latest backup
files = sorted(glob.glob("backup_*.sql"))

if not files:
    print("❌ No backup found")
    exit()

latest = files[-1]

# Step 4: restore
print(f"♻️ Restoring from {latest}")

os.system(
    f"docker exec -i {container_name} "
    f"psql -U postgres demo < {latest}"
)

print("✅ Restore Complete")

print("🔍 Verifying DB...")

result = os.system(
    "docker exec dr-postgres psql -U postgres -d demo -c 'SELECT 1;'"
)

if result == 0:
    print("🎉 Recovery SUCCESS")
else:
    print("❌ Recovery FAILED")
