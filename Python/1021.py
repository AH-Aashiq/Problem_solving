#Banknotes and Coins
a = float(input())
print('NOTAS:')

for i in [100,50,20,10,5,2]:
     print(f'{int(a/i)} nota(s) de R$ {i}.00')
     a = float(f'{a%i:.2f}')
# print (a)

print('MOEDAS:')

for i in [1.00,0.50,0.25,0.10,0.05,0.01]:
     print(f'{int(a/i)} moeda(s) de R$ {i:.2f}')
     a = float(f'{a % i:.2f}')
# print (a)