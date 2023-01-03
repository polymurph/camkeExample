import os
import re

# https://stackoverflow.com/questions/3368969/find-string-between-two-substrings

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

currentPath = os.getcwd()

CMakeListsPath = os.path.join(currentPath, 'CMakeLists.txt')

print('path to CMakeLists.txt')
print(CMakeListsPath)
print('searching for project name...')

with open(CMakeListsPath, 'r') as file:
	content = file.read()
        projectName = find_between_r(content, 'set(PROJECT_NAME "', '")')
	
if projectName == 'None':
    print('could not find project name!')
else:
    print(os.getcwd())
    os.system('cd build/')
    print(os.getcwd())
    os.system('./' + projectName)


