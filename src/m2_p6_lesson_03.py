# python-package  # Директория (метаданные: {'hidden': True})
# ├── Makefile  # Файл
# ├── README.md  # Файл
# ├── dist  # Пустая директория
# ├── tests  # Директория
# │   └── test_solution.py  # Файл
# ├── pyproject.toml  # Файл
# └── .venv  # Директория (метаданные: {'owner': 'root', 'hidden': False})
#     └── lib  # Директория
#         └── python3.6  # Директория
#             └── site-packages  # Директория
#                 └── hexlet-python-package.egg-link  # Файл

# import itertools
from m2_p6_lesson_03_hexlet_fs import mkdir, mkfile


# BEGIN (write your solution here)
def create_nested_df(noda, dir_, type_children, name_target):
    for value_ in noda:
        if value_['name'] == dir_ and type_children == 'directory':
            value_['children'].append(mkdir(name_target, []))
            return value_['children']
        elif value_['name'] == dir_ and type_children == 'file':
            value_['children'].append(mkfile(name_target))
            return value_['children']
    return None

def generate():
    tree = mkdir('python-package', [], {'hidden': True})
    tree_root = tree['children']
    tree_root.append(mkfile('Makefile'))
    tree_root.append(mkfile('README.md'))
    tree_root.append(mkdir('dist', []))
    tree_root.append(mkfile('pyproject.toml'))
    tree_root.append(mkdir('tests', []))
    tree_root.append(mkdir('.venv', [],
                                   {'owner': 'root', 'hidden': False}))

    _ = create_nested_df(tree_root, 'tests', 'file', 'test_solution.py')
    tree_subroot = create_nested_df(tree_root, '.venv', 'directory', 'lib')
    tree_subroot = create_nested_df(tree_subroot, 'lib',
                                    'directory', 'python3.6')
    tree_subroot = create_nested_df(tree_subroot, 'python3.6',
                                   'directory', 'site-packages')
    _ = create_nested_df(tree_subroot, 'site-packages',
                                   'file', 'hexlet-python-package.egg-link')

    return tree

# print(generate())
# print()
