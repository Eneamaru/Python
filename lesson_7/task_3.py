import os
import shutil

my_project = os.path.join(os.path.dirname(__file__), 'my_project')
templates = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(templates):
    os.mkdir(templates)

for root, dirs, files in os.walk(my_project):
    if root.count('templates'):
        for _dir in dirs:
            if not os.path.exists(os.path.join(templates, _dir)):
                root_dir = os.path.join(root, _dir)
                templates_dir = os.path.join(templates, _dir)
                shutil.copytree(root_dir, templates_dir)

print(my_project)
print(templates)