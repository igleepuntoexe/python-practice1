import math
from re import A, X
from typing import Match
#Exercise 1
#The program should ask the user to enter a number. This number is collected in a type variable called radius. 
# Next, the length of the circle, the area and the volume of the sphere must be calculated in variable paths.
pi = 3.14
radio = float(input("Give me the radio: "))
length  = 2 * pi * radio
area = pi * (radio * radio)
volume = (4/3)* pi *(radio * radio * radio)
print (str("The length  es: " + str(length) + ", the area is: " + str(area) + " and the volum is: " + str(volume)))

#Exercise 2
#Design a program that asks the user to enter the price and the quantity of a certain product.
#Then it calculates the final amount that will be price * quantity and displays the following message on the screen:
#“The price of the product is x euros and the amount you buy is and therefore you must pay z euros. Come back soon."

price = float(input("How much does the product cost? "))
amount = int(input("How many products are you going to buy? "))
Fprice = price * amount #Finaly Price
print("The price of the product is " +  str(price) + " euros and the amount you buy is " + str(amount) + " therefore you must pay " + str(Fprice) + " euros. Come back soon.")

#Exercise 3
#Make a program that asks the user for two numbers and calculates saving it in VARIABLE PATHS: 
#The SUM, The SUBTRACTION, and The MULTIPLICATION of these two numbers and displays the results on the screen with messages such as:

num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))
sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print("The sum is: " +  str(sum) + ", the subtraction is: " +  str(subtraction) + " and the multiplication is: " +  str(multiplication))

#Exercise 4
#A given temperature in degrees Celsius (centigrade) can be converted to an equivalent Fahrenheit temperature according to the following formula:
#f = (9/5) * C + 32 <-- Formula
#Write a program that reads the temperature in degrees Celsius and converts it to degrees Fahrenheit.
degreesC = float(input("What is the current temperature? ")) #Degrees Celsius
degreesF = (9/5) * degreesC + 32 #Degrees Fahrenheit 
print("The temperature in degrees Fahrenheit is: " + str(degreesF))

#Exercise 5
#Create a program that reads by keyboard the volume, the number of moles, and the temperature and calculates the pressure,
#P: is the pressure in atmospheres.
#V: is the volume in liters.
#n: is the number of moles.
#R: It is a constant that is worth 0.082
#T: It is the temperature in Kelvin
#The ideal gas formula is: pv = nRT
#informing the user with the following message:
#"With a volume of V liters, and a temperature of T kelvin, n moles of an ideal gas have a pressure of P atmospheres"
R = 0.082
volume = float(input("Give me the liters: "))
moles = float(input("Give me the moles: "))
temperature = float(input("Give me the temperature (in kelvin): "))
pressure = moles * R * temperature
print("With a volume of " + str(volume) + " liters, and a temperature of " + str(temperature) +  " kelvin, " + str(moles) + 
" moles of an ideal gas have a pressure of " + str(pressure) + " atmospheres")

#Exercise 6
#Write a program that allows the contents of two variables x and y of a certain type of data to be exchanged.
n1 = int(input("Give me a number: "))
n2 = int(input("Give me another number: "))
n3 = n1
n4 = n2
print(str(n4))
print(str(n3))

#Exercise 7
#The program should ask the user to enter two data of type double: space in meters and time in seconds. 
# With these data it will report the speed in meters per second according to the mythical formula:
#Speed ​​= space / time
#The message will be: "The speed is" + speed + "meters / second"
space = float(input("Give me the meters: "))
temp = float(input("Give me the seconds: "))
speed = space / temp
print("The speed is " + str(speed) + " meters / second")

#Exercise 8
#Design a program that, from the side of a square, calculates its area, its perimeter and its diagonal:
#p = 4 * side
#d = side × √2
#A = side2

side = float(input("Give me the measurements: "))
p = 4 * side
d = side * math.sqrt(2)
A = side * side
print("The perimeter is: " + str (p) + " the diagonal is: " + str (d) + " the area is: " + str (A))

#Exercise 9
#Design a program that, from the sides of the legs of a right triangle, 
# calculates the hypotenuse to two decimal places according to the Pythagorean theorem:
#h2 = a2 + b2  
#h = Raiz(a2 + b2)

cat1 = float(input("Give me the hick: "))
cat2 = float(input("Give me another hick: "))
cat3 = (cat1 * cat1) + (cat2 * cat2)
h = math.sqrt(cat3)
print("The hypotenuse is: " + str(h))

#Exercise 10
#Design a program that calculates the discount made on a certain product from the initial price and the discount percentage. 
# The program should display a message informing:
#"By applying a x percent discount, the final price of the product is the x and therefore you save y euros."

price1 = float(input("How much does the shirt cost? "))
reduction = int(input("How much is the reduction? "))
Fprice = (reduction / 100) * price1 #<-- Final Price
Freduction = price1 - Fprice #<-- Final Reduction
print("By applying a " + str(reduction) + "% percent discount, the final price of the product is the " + str(Fprice) + "$ and therefore you save" + str(Freduction) + "$.")

#Exercise 11
#Make a program that reads the side of a cube and calculates the following data:
#D = √3 * a
#Al = 4 * a2
#V = a3

a1 = float(input("Give me the side: "))
d1 = math.sqrt(3) * a1
al = 4 * (a1 * a1)
v1 = a1 * a1 * a1
print("The D is "+ str(d1) +". The Al is "+ str(al) +". The V is: "+ str(v1))
