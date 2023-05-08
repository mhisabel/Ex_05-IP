'''
num = int(input('Quantidade: '))

while (num > 0):
    for i in range(1, num+1):
        print(i)

    num = int(input('Quantidade: '))
'''

while (True):
  num = int(input('num: '))
  if (num <= 0):
    break
  for i in range(1,num+1):
    print(i, ' ',end='')
  print()
