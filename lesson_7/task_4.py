import os

folder = 'some_data'
result_dct = {}
for root, dirs, files in os.walk(folder):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        border = 10 ** len(str(size))
        if result_dct.get(border):
            result_dct[border] += 1
        else:
            result_dct[border] = 1
result_dct = {key: result_dct[key] for key in sorted(result_dct)}
print(result_dct)
