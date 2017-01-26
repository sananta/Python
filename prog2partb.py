## prog2partb.py
## Srivarshini Ananta
## January 26, 2016

def inchesToMeters(inches):
    """ compute meters given inches """
    exchangerate = 0.0254
    result = inches * exchangerate
    return result 

def poundsToKgs(pounds):
    """ compute kilograms given pounds """
    exchangerate2 = 0.453592
    result = pounds * exchangerate2
    return result

def bmi(height, weight):
    """ given the height in meters and weight in kilograms compute body mass index """
    result = weight/ ((height) ** 2)
    return result

def bodyMassIndex():
    name = str(input("Please enter the subject's name: "))
    height=float(input("Please enter the subject's height in inches: "))
    weight=float(input("Please enter the subject's weight in pounds: "))
    height_to_meters = inchesToMeters(height)
    weight_to_kg = poundsToKgs(weight) 
    print(name, "has a body mass index of: ", bmi(height_to_meters, weight_to_kg))

    if bmi(height_to_meters, weight_to_kg) < 18.5:
        print(name, " is underweight")
    elif (bmi(height_to_meters, weight_to_kg) >= 18.5) and (bmi(height_to_meters, weight_to_kg) < 25):
        print(name, " is normal weight")
    elif (bmi(height_to_meters, weight_to_kg) >= 25) and (bmi(height_to_meters, weight_to_kg) < 30):
        print(name, " is overweight")
    elif bmi(height_to_meters, weight_to_kg) >= 30:
        print(name, " is obese") 
    

                                                     
