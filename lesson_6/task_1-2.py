result = []
req = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ls = line.split()
        print((ls[0], ls[5].strip('"'), ls[6]))
        if ls[0] not in req:
            req[ls[0]] = 1
        else:
            req[ls[0]] += 1
v = 0
k = ''
for key, value in req.items():
    if value > v:
        v = value
        k = key
print(k, v)
