#Banknotes
a = int(input())
print(a)

for i in [100,50,20,10,5,2,1]:
     print(f'{a//i} nota(s) de R$ {i},00')
     a = a%i
     