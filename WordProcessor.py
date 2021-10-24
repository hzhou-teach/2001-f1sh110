f = open("word.txt", "r")
args = f.readline().split()
args[0], args[1] = int(args[0]), int(args[1])

word = f.readline().split()
print(args)
print(word)

line = ''
count = 0

f.close()
for i in word:
  if count + len(i) <= args[1]:
    count += len(i)
    line += i
  else:
    count = len(i)
    line = line[:-1]
    line += '\n' + i
  line += ' '
line = line[:-1]

print(line)
f = open('answer.txt', 'w')
f.write(line)
f.close()