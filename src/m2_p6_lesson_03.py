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
# def create_nested_dir_file(noda, dir_, dir_file, flag_d_f):
def create_nested_dir_file(noda, dir_):
    for value_ in noda:
        if value_['name'] == dir_ and value_['type'] == 'directory':
            return value_['children']
    return None

def module_test():
    tree = mkdir('python-package', [], {'hidden': True})
    root_noda = tree['children']
    root_noda.append(mkfile('Makefile'))
    root_noda.append(mkfile('README.md'))
    root_noda.append(mkdir('dist', []))
    root_noda.append(mkdir('tests', []))
    root_noda.append(mkfile('pyproject.toml'))
    root_noda.append(mkdir('.venv', [], {'owner': 'root', 'hidden': False}))

    noda = create_nested_dir_file(root_noda, 'tests')
    if not noda is None:
        noda.append(mkfile('test_solution.py'))

    noda = create_nested_dir_file(root_noda, '.venv')
    if not noda is None:
        noda.append(mkdir('lib', []))

    noda = create_nested_dir_file(noda, 'lib')
    if not noda is None:
        noda.append(mkdir('python3.6', []))

    noda = create_nested_dir_file(noda, 'python3.6')
    if not noda is None:
        noda.append(mkdir('site-packages', []))

    noda = create_nested_dir_file(noda, 'site-packages')
    if not noda is None:
        noda.append(mkfile('hexlet-python-package.egg-link'))
    
    return tree

# print(tree)
# for value_ in root_noda:
#     if value_['name'] == 'tests' and value_['type'] == 'directory':
#         target_mkdir = value_['children']
#         target_mkdir.append(mkfile('test_solution.py'))
#         break
# for value_ in root_noda:
#     if value_['name'] == '.venv' and value_['type'] == 'directory':
#         target_mkdir = value_['children']
#         target_mkdir.append(mkdir('lib', []))
#         break
# for value_ in target_mkdir:
#     if value_['name'] == 'lib' and value_['type'] == 'directory':
#         target_mkdir = value_['children']
#         target_mkdir.append(mkdir('python3.6', []))
#         break

# for value_ in target_mkdir:
#     if value_['name'] == 'python3.6' and value_['type'] == 'directory':
#         target_mkdir = value_['children']
#         target_mkdir.append(mkdir('site-packages', []))
#         break

# for value_ in target_mkdir:
#     if value_['name'] == 'site-packages' and value_['type'] == 'directory':
#         target_mkdir = value_['children']
#         target_mkdir.append(mkfile('hexlet-python-package.egg-link'))
#         break

# target_mkdir.append(mkdir('lib', []))

# noda = get_children_dir(root_noda, 'pes')
# noda = get_children_dir(root_noda, 'tests')
# noda = get_children_dir(root_noda, 'pes', 'tests')

# noda = get_children_dir(root_noda, 'tests', 'tests')
# noda = get_children_dir(root_noda, 'tests')
# if not noda is None:

# noda = get_children_dir(root_noda, '.venv/lib')
# if not noda is None:


# tree['children'] = mkdir('.venv',
#                          [mkdir('lib',
#                                 [mkdir('python3.6',
#                                        [mkdir('site-packages',
#                                               [mkfile('hexlet-python-package.egg-link')]
#                                               )
#                                         ]
#                                        )
#                                  ]
#                                 )
#                           ],
#                          {'owner': 'root', 'hidden': False})

# def get_children_dir(noda, full_path, target_mkdir):
# def get_children_dir(noda, full_path):
#     tmp_path = full_path.split('/')[0]
#     for value_ in noda:
#         if value_['name'] == tmp_path and value_['type'] == 'directory' \
#             and "/" in full_path:
#                 return get_children_dir([noda], full_path.split('/')[1])
#         if value_['name'] == tmp_path and value_['type'] == 'directory' \
#             and not "/" in full_path:
#             return value_
#     if not "/" in full_path:
#         return None
#     return get_children_dir(noda, full_path.split('/')[1])
    # return get_children_dir(noda, full_path.split('/')[1], target_mkdir)
# END
