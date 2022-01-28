import csv
from datetime import datetime
def logAlert(username, alertReason):
    fields=[datetime.utcnow(),username,alertReason]
    with open(r'alertLog.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        f.close()
