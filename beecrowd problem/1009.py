#Salaray with bonus
name = input()

fix_sal = float(input())  
value = float(input())

bonus = float(value * (15/100))

total = fix_sal + bonus

print(f'TOTAL = R$ {total:.2f}')
