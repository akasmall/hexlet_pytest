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

    # noda = create_nested_dir_file(root_noda, 'tests')
    # if not noda is None:
    #     noda.append(mkfile('test_solution.py'))

    # noda = create_nested_dir_file(root_noda, '.venv')
    # if not noda is None:
    #     noda.append(mkdir('lib', []))

    # noda = create_nested_dir_file(noda, 'lib')
    # if not noda is None:
    #     noda.append(mkdir('python3.6', []))

    # noda = create_nested_dir_file(noda, 'python3.6')
    # if not noda is None:
    #     noda.append(mkdir('site-packages', []))

    # noda = create_nested_dir_file(noda, 'site-packages')
    # if not noda is None:
    #     noda.append(mkfile('hexlet-python-package.egg-link'))
    
    # return tree


# for v_venv in root_noda:
#     if v_venv['name'] == 'tests' and v_venv['type'] == 'directory':
#         target_mkdir = v_venv['children']
#         target_mkdir.append(mkfile('test_solution.py'))
#         break
# for v_venv in root_noda:
#     if v_venv['name'] == '.venv' and v_venv['type'] == 'directory':
#         target_mkdir = v_venv['children']
#         target_mkdir.append(mkdir('lib', []))
#         break
# for v_venv in target_mkdir:
#     if v_venv['name'] == 'lib' and v_venv['type'] == 'directory':
#         target_mkdir = v_venv['children']
#         target_mkdir.append(mkdir('python3.6', []))
#         break

# for v_venv in target_mkdir:
#     if v_venv['name'] == 'python3.6' and v_venv['type'] == 'directory':
#         target_mkdir = v_venv['children']
#         target_mkdir.append(mkdir('site-packages', []))
#         break

# for v_venv in target_mkdir:
#     if v_venv['name'] == 'site-packages' and v_venv['type'] == 'directory':
#         target_mkdir = v_venv['children']
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
#     for v_venv in noda:
#         if v_venv['name'] == tmp_path and v_venv['type'] == 'directory' \
#             and "/" in full_path:
#                 return get_children_dir([noda], full_path.split('/')[1])
#         if v_venv['name'] == tmp_path and v_venv['type'] == 'directory' \
#             and not "/" in full_path:
#             return v_venv
#     if not "/" in full_path:
#         return None
#     return get_children_dir(noda, full_path.split('/')[1])
    # return get_children_dir(noda, full_path.split('/')[1], target_mkdir)
# END
