# Basic test for database insertion and retrieval
from db.database import init_db, insert_entry, fetch_entry_by_date
from datetime import date

init_db()

sample_date = str(date.today())
insert_entry(sample_date, "journal text", "dream", "focus", "priority1, priority2, priority3", "reflection result")

result = fetch_entry_by_date(sample_date)
assert result is not None, "❌ Failed to retrieve inserted entry"
print("✅ Database test passed.")
