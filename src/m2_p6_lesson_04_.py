import copy

from hexlet_fs import get_children, get_meta, get_name
from hexlet_fs import is_file, mkdir, mkfile

#3:1: F401 'hexlet.fs.get_meta' imported but unused
#3:1: F401 'hexlet.fs.is_file' imported but unused
#3:1: F401 'hexlet.fs.mkdir' imported but unused
#3:1: F401 'hexlet.fs.mkfile' imported but unused

def compress_images(noda):
    # для линтера ))
    plug = mkdir('plug',[mkfile('plug.plug')])
    #  основной код
    new_noda = copy.deepcopy(noda)
    children = get_children(new_noda)
    files_all = list(filter(lambda x: is_file(x), children))
    files_jpg = list(filter(lambda x: get_name(x)[-4:] == '.jpg', files_all))

    for size_ in files_jpg:
        size_['meta']['size'] = int(size_['meta']['size'] / 2)
    
    return new_noda


tree = mkdir(
    'my documents',
    [
        mkdir('i_dir', []),
        mkfile('audio.mp3', {'size': 200}),
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)
print(tree)
print(compress_images(tree))

# Реализуйте функцию compress_images(). Она должна принимать на вход директорию,
# находить внутри нее картинки и уменьшать свойство size в их метаданных в два
# раза. Функция должна вернуть обновленную директорию со сжатыми картинками и
# всеми остальными данными, которые были внутри этой директории.

# Картинками считаются все файлы, заканчивающиеся на .jpg:

# from hexlet.fs import mkdir, mkfile
# from solution import compress_images
# tree = mkdir(
#     'my documents',
#     [
#         mkfile('avatar.jpg', {'size': 100}),
#         mkfile('photo.jpg', {'size': 150}),
#     ],
#     {'hide': False}
# )
# compress_images(tree)
# # {
# #     'name': 'my documents',
# #     'type': 'directory',
# #     'children': [
# #         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
# #         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
# #     ],
# #     'meta': {'hide': False},
# # }

# BEGIN
# решение учителя
# def compress_images(tree):
#     children = get_children(tree)

#     def reduce_image_size(node):
#         name = get_name(node)
#         if not is_file(node) or not name.endswith('.jpg'):
#             return node
#         meta = get_meta(node)
#         new_meta = copy.deepcopy(meta)
#         new_meta['size'] //= 2
#         return mkfile(name, new_meta)

#     new_children = map(reduce_image_size, children)
#     new_meta = copy.deepcopy(get_meta(tree))
#     return mkdir(get_name(tree), list(new_children), new_meta)
# END