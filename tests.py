from functions.get_files_info import get_files_info


i = "".join(str(x) for x in get_files_info('calculator', '/'))
print(i)

print('Result for current directory:\n', get_files_info('calculator', '.'))
print('Result for pkg directory:\n', get_files_info('calculator', 'pkg'))
print('Result for /bin directory:\n', get_files_info('calculator', '/bin'))
print('Result for ../ directory:\n', get_files_info('calculator', '../'))
