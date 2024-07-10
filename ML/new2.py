import statistics
# py pro input string and print its characters in different lines two characters per line 

def brk(passs):
    for i in range(0,len(passs),2):
        print(passs[i:i+2])
        
str=input("ENTER A STRING : ")

brk(str)

# py pro to calculate body mass index of a person(bmi)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("Your BMI is:",bmi)


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

# py pro to print the area of circle .the radius of circle is given by user
r=float(input("\n\nENTER RADIUS = "))
area=3.14*r*r
print("THE AREA OF CIRCLE IS ",area)


# py pro to obtain the marks in a computer of some students and find mid median and mode
marks=[25,26,27,31,39]
# mean
mean=statistics.mean(marks)
print("\n\nTHE MEAN IS ",mean)

# median
sortt=sorted(marks)
meadiann=statistics.median(sortt)
print("THE MEADIAN IS ",meadiann)

# mode
mode=statistics.mode(marks)
print("MODE IS ",mode)

