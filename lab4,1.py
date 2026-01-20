import json

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:  # Пропускаем пустые строки
            data = json.loads(line)
            user_id = data['user_id']
            category = data['category']
            purchases[user_id] = category


for i, (user_id, category) in enumerate(purchases.items()):
    if i < 2:
        print(user_id, category)
