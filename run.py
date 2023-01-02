import os
import re

'''
s = "abc123AUG|GAC|UGAasdfg789"

pattern = "AUG\|(.*?)\|UGA"


substring = re.search(pattern, s).group(1)

print(substring)
'''


currentPath = os.getcwd()

CMakeListsPath = os.path.join(currentPath, 'CMakeLists.txt')

print('path to CMakeLists.txt')
print(CMakeListsPath)
print('searching for project name...')

with open(CMakeListsPath, 'r') as file:
	content = file.read()
        #print(content)
        regexPattern = '5' + '(.*?)' + 'kgt)'
	projectName = re.search(regexPattern, '12345Testkgt').group(1)
	
if projectName == 'None':
    print('could not find project name!')
else:
    print(projectName)


