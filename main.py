file11 = open('arish.txt')
print(file11.readline())
print(file11.read(6))

#coping a file's data to another file

f1 = open('file1.txt','r')
f2 = open('file2.txt','w')

for line in f1.readlines():
    if not (line.startswith('Coding')):
        f2.write(line)

f2.close()
f1.close()