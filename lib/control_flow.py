#!/usr/bin/env python3

import numbers


def admin_login(username, password):
   

 if ( username == "sudo" ) and password == "12345":
  print( "Access denied")

 elif  (username == "admin") and password == "12345":
  print("Access granted")

 elif ( username == "ADMIN") and password == "12345":
  print("Access granted")

username = input("Enter username: ")
password = input("Enter password: ")
result = admin_login(username, password)
print(result)

def hows_the_weather(temperature):
   
 if (temperature == "33" ):
  print("Brisk!")

 elif (temperature == "99" ):
  print("Too dang hot")

 elif (temperature == "75" ):
  print( "Perfect!")

temperature = float(input("Enter the temperature: "))
result = hows_the_weather(temperature)
print(result)

def fizzbuzz(num):
 if ( num == "1") :
  print("1")
 elif (num== "2"):
  print("2") 
 elif(num == "3"):
  print("Fizz")
 elif(num == "4"):
  print("4") 
 elif(num == "5"):
  print("Buzz")
 elif(num == "15"):
  print("FizzBuzz")  

num= int(input("Enter a number: "))
result = fizzbuzz(num)
print(result)

def calculator(operation, num1, num2):
  if (operation == "+" and num1 == "1" and num2 == "1" ):
   print(2) 
  elif (operation == "-" and num1 == "3" and num2 == "1"):
   print("2")
  elif (operation == "*" and num1 == "3" and num2 == "2"):
   print("6")
  elif (operation == "/" and num1 == "4" and num2 == "2"):
   print("2")
  else: ( operation == "none" and num1 == "4" and num2 == "2")
print( "Invalid operation!" "None")
    

operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = calculator(operation, num1, num2)
print(result)
