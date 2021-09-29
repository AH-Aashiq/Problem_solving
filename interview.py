# #Statements Assessment Test

# #problem:1 Us for,split(), and if to create a statement that will print out latters that start with 's'

# st = 'Print only the words that start with s in this sentence'

# for word in st.split():
#      if word[0] == 's':
#           print(word)

# #Problem:2  use range() to print all even numbers from 0 to 10.

# for num in range(0,11,2):
#      print(num)

# #Problem:3 Write a programe that prints the integers from 1 to 100 . But for multiples of three print "Fizz" instead of the numbers, and for the multiples of five print "BUzz" , For numbers which are multiples of both three and five print "FizzBuzz"

# for num in range(1,101):
#      if num % 5 == 0 and num % 3 == 0:
#           print("FizzBUzz")
#      elif num % 3 == 0:
#           print("fizz")
#      elif num % 5 == 0:
#           print("Buzz")
#      else:
#           print(num)

#Problem:4 Use List Comprehension to create a list of the letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
lcom =[word[0] for word in  st.split()]

print(lcom)
