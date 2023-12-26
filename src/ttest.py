from hexlet_fs import mkdir, mkfile, is_directory, get_name
from hexlet_fs import get_children, flatten


def find_empty_dir_paths(tree):
    name = get_name(tree)
    # Получаем потомков узла (директории)
    children = get_children(tree)
    # Если потомков нет, то возвращаем директорию
    if len(children) == 0:
        return name
    # Фильтруем файлы, они нас не интересуют
    dir_names = filter(is_directory, children)
    # Ищем пустые директории внутри текущей
    empty_dir_names = list(map(find_empty_dir_paths, dir_names))
    # Далее flatten делает список плоским
    return flatten(empty_dir_names)


tree_ = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf'),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkdir('data'),
        ]),
    ]),
    mkdir('logs'),
    mkfile('hosts'),
])
print(find_empty_dir_paths(tree_))
# => ['apache', 'data', 'logs']
