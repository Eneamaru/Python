import os

root = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in folders:
    if not os.path.exists(os.path.join(root, folder)):
        os.makedirs(os.path.join(root, folder))
