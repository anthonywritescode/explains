

f = open('filename', 'w')
try:
    f.write('hello hello world\n')
finally:
    f.close()


with (
        open('filename', 'w') as f,
        open('filename2', 'w') as f2,
):
    f.write('hello hello world\n')
    f2.write('hello hello world2\n')


with open('filename', 'w') as f, open('filename2', 'w') as f2:
    f.write('hello hello world\n')
    f2.write('hello hello world2\n')


with open('filename', 'w') as f:
    with open('filename2', 'w') as f2:
        f.write('hello hello world\n')
        f2.write('hello hello world2\n')

print('done')
