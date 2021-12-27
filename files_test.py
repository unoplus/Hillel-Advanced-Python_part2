# Create by Bender

import os


def file_tree(some_path: str) -> None:
    """
    This function displays a tree of directories and files as entered by the
    user. Takes a directory path as input, as a string.
    :param some_path: path to directory
    :return:
    """
    if not os.path.exists(some_path):
        print('You shall not pass! ;)\nbecause path doesn`t exists.')
    else:
        for paths, dirs, files in os.walk(some_path):
            indents = paths.replace(some_path, '').count(os.sep)
            dirs_branch = ' ' * indents
            files_branch = ' ' * (indents + 1)
            print(f'{dirs_branch}/{os.path.basename(paths)}')
            print(f'{dirs_branch}/..')

            for file in files:
                print(f'{files_branch}{file}')


if __name__ == '__main__':
    file_tree(input('Type path to dir here which you want to list: '))
