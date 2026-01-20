import json
import csv


purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            data = json.loads(line)
            purchases[data['user_id']] = data['category']

with open('visit_log.csv', 'r', encoding='utf-8') as f_in, \
     open('funnel.csv', 'w', newline='', encoding='utf-8') as f_out:
    
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    first_row = True
    for row in reader:
        user_id, source = row[0], row[1]
        
        if user_id in purchases and not first_row:

            writer.writerow([user_id, source, purchases[user_id]])
        
        first_row = False

print("Файл funnel.csv создан!")
