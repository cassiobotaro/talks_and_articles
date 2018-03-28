#!/usr/bin/python3

import pathlib

absolute_path = pathlib.Path(__file__).resolve().parent

print(f'Absolute path is {absolute_path}')

# old style
# absolute_path = os.path.join(os.path.abspath(__file__))
# absolute path as string

print('Listing slide files...')

for file in absolute_path.glob('*.slide'):
    print(file)

# old style
# for file in glob.glob('*.slide'):
#     print(file)
# ...

file = absolute_path / 'codes' / 'python_moderno' / 'output.txt'

file.write_text('teste')

if file.exists():
    print('file content is: ', file.read_text())
