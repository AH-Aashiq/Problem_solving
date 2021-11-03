#  #Statements Assessment Test

#  #problem:1 Us for,split(), and if to create a statement that will print out latters that start with 's'

#  st = 'Print only the words that start with s in this sentence'

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

#  #Problem:4 Use List Comprehension to create a list of the letters of every word in the string below:

# st = 'Create a list of the first letters of every word in this string'
# lcom =[word[0] for word in  st.split()]

# print(lcom)

# #prohlem 5: Go through the string below and if the lenght of a word is even print "Even"

# st = 'print every word in this sentence that has an even number of letters'

# for word in st.split():
#      if len(word) % 2 == 0:
#           print(word + "<--- has an even lenght!")


#  #Function and Methods Problem

#  #Problem 1: Write a funcion that computes the volume of a shere given its radius 

# def vol(rad):
#      return (4.0/3)*(3.14)*(rad**3)

# print(vol(10))

# # #Problem 2: Write a function that checks whether a number is in a given range (inclusive of high and low)

# def ran_check(num,low,high):
#      #Check if num is between Low and high (including low and high)
#      if num in range(low,high):
#           print("%s is in the range" %str(num))
     
#      else:
#           print("The numbner is outside the range")

# print(ran_check(3,1,10))

# # #If you only wanted to return a boolean value

# # def ran_bool(num,low,high):
# #      return num in range(low,high)

# # print(ran_bool(3,1,10))  #True



#  #Problem 3: Write a python fucntion that accepts a string and calculate the number of upper case letters and lower case letters.
#  #Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#  #Expected output:
#  #No. of Upper case Characters: 4
#  #No. of Lower case Characters: 33


#  #Problem 4: write a pyhton fucntion that takes a list and returns a new list with unique elements of the first list

#  # Sample List : [1,1,1,1,2,3,3,3,4,5]
#  # Unique List : [1,2,3,4,5]

# def unique_list(l):
#      x = []
#      for a in l:
#           if a not in x:
#                x.append(a)
#      return x

# print(unique_list([1,1,1,1,2,3,3,3,4,5]))



#  #Problem 5: Write a Python function to multiply all the numbers in a list
#  #Sample List : [1,2,3,-4]
#  #Sample Output : -24

# def multiply(numbers):
#      total = numbers[0]
#      for x in numbers:
#           total *= x
#      return total

# print(multiply([1,2,3,-4]))


# Problem 6: Write a Python function that checks whether as passed string is palindrome or not.

# def palindrome(s):
#      pass

#  #Problem 7(Hard): Write a Python fucntion checks whether a string is pangram or not.
#  #Note : Pangram are words or sentences containing every letter of the alphabet at least onece. 
#  #For example : "The quick brown fox jumps over the lazy dog"

# import string
# def ispangram(str1, alphabet=string.ascii_lowercase):
#      alphaset = set(alphabet)
#      return alphaset <= set(str1.lower())

# print(ispangram("The quick brown fox jumps over the lazy dog"))


#Find the prime number 
# lower = int(input("Enter the lower value:"))
# upper = int(input("Enter the upper value:"))
# for number in range(lower,upper+1):
#     if number>1:
#         for i in range(2,number):
#             if (number%i)==0:
#                 break
#         else:
#             print(number)


# for i in range(2,101):
#     if i < 10 and i == 2 or i == 3 or i == 5 or i == 7:
#         print(i)
    
#     elif not (i%2 and i%3 and i%5 and i%7):
#         pass

#     else:
#         print(i)

