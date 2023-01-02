#import pathlib
import os


#currentPath = pathlib.Path(__file__).parent.resolve()
#print(currentPath)

currentPath = os.getcwd()

buildFolderPath = os.path.join(currentPath, 'build')

os.mkdir(buildFolderPath)

os.chdir(buildFolderPath)

os.system('cmake ../ .')

os.system('cmake --build .')
