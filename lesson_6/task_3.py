import sys
import json

result = {}
with open('users.csv', 'r', encoding='utf-8-sig') as f_1, open('hobby.csv', 'r', encoding='utf-8-sig') as f_2:
    for line_1 in f_1:
        line_2 = f_2.readline().strip().replace(',', ' ')
        if not line_2:
            line_2 = None
        if line_1 not in result:
            result[line_1.strip().replace(',', ' ')] = line_2
    condition = f_2.read()
    if condition:
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as result_f:
    result_f.write(json.dumps(result, ensure_ascii=False))
with open('result.json', 'r', encoding='utf-8') as f:
    result = json.loads(f.read())
print(result)
