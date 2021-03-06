import os


os.mkdir('outdir')

# v1
os.chdir('outdir')
os.mkdir('innerdir')

file_path = os.path.join('innerdir', 'empty.txt')

with open(file_path, 'w'):
    pass

for path, dirnames, filenames in os.walk('.'):
    print(path, dirnames, filenames)

os.remove(file_path)

# v1.1
# os.rmdir('innerdir')
# os.rmdir(os.getcwd())

# v.1.2
os.removedirs(os.path.join(os.getcwd(), 'innerdir'))



# v2
# outdir_path = 'outdir'
# innerdir_path = os.path.join(outdir_path, 'innerdir')
# empty_file_path = os.path.join(innerdir_path, 'empty.txt')
#
# os.mkdir(innerdir_path)
#
# with open(empty_file_path, 'w'):
#     pass
#
# for path, dirnames, filenames in os.walk(outdir_path):
#     print(path, dirnames, filenames)
#
# os.remove(empty_file_path)
# os.removedirs(innerdir_path)
