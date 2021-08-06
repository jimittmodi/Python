import os

#to get which commands os module supports
print(dir(os))

#to know what is the current working directory
print(os.getcwd())

#to change the directory
os.chdir('D:\Quantiphi\Training')
print(os.getcwd())

#to print the contents of the directory
print(os.listdir())

#to create a directory 
os.mkdir('Hello')

#to create directories within directories
os.makedirs('hello-1/bye/open-it')

#to delete a directory
os.rmdir('Hello')

#to remove directories within directories
os.removedirs('hello-1/bye/open-it')

#to rename the file
os.rename('hello.txt', 'bye.txt')

#to print the info of a file
print(os.stat('os_module.py'))

#to go through the directories
for dirpaths, dirnames, filenames in os.walk('D:\Quantiphi\Training'):
    print('Current Path: ', dirpaths)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

#to get the environment variable
print(os.environ.get('JAVA_HOME'))

#to join paths
path_file = os.path.join(os.environ.get('JAVA_HOME'),'text.txt')
print(path_file)