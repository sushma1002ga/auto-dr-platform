import os
from datetime import datetime

backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

command = (
    f"docker exec dr-postgres "
    f"pg_dump -U postgres demo > {backup_name}"
)

os.system(command)

print(f"Backup Created: {backup_name}")
