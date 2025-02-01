import os
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%SZ")
os.system(f"sudo mysqldump -u root first_database>first_database_{timestamp}.sql")