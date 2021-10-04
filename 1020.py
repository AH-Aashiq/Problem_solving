#AGE IN DAYS
# Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

# Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

# Input
# The input file contains 1 integer value.

#Input Sample: 400
#Output Sample: # 1 ano(s)
                # 1 mes(es)
                # 5 dia(s)

days = int(input())

years = int(days/365)
days %= 365

months = int(days/30)
days %= 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')