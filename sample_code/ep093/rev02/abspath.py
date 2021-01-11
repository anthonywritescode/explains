import os.path


print(f'my path is {__file__}')

my_parent_dir = os.path.normpath(os.path.join(__file__, '..'))
print(my_parent_dir)
