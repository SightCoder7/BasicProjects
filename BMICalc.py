#Import
from time import sleep
#Instructions
instructions = "▪ Make sure to leave space between the number and the symbol"
print(f"Welcome to BMI Calculator \n {instructions}")
#Def Get Values
def getvalues():
    try:
        #Weight 
        weightt = input("Enter your weight:")
        weightV = weightt.split()
        weightE = float(weightV[0])
        weight = round(weightE, 2)
        conversion_W = weightV[1]
        #Height
        heightt = input("Enter your height:")
        heightV = heightt.split()
        heightE = float(heightV[0])
        height = round(heightE, 2)
        conversion_H = heightV[1]
        #Checks for float and length of list
        if isinstance(weight, float) and len(weightV) == 2 and isinstance(height, float) and len(heightV) == 2:
            return weight, conversion_W, height, conversion_H
        else:
            print("Error happend pls check your input again")
    except:
        #Try and error
        print("Error happend pls check your input again")
        exit()
#Values received
weight, symbol, height, symbol_H = getvalues()
#Converts to m and kg
def conversion(W,WH,H,HH):
    try:
        if WH == "kg":
          pass
        elif WH == "pound":
          W = W*0.45          
        elif WH == "g":#Who in the world would write in grams
          W = W/1000
        else:
          print("Check the symbol")
        if HH == "m":
         pass
        elif HH == "inch":
         H = H*0.025
        elif HH == "cm":
         H = H/100
        elif HH == "feet":
         H =H*0.3048
        else:
         print("Check your symbols")
        W = round(W, 2)
        H = round(H, 2)
        return W,H
    except:
        #Trial error
      print('An exception occurred')
#Values received
W,H = conversion(weight,symbol,height,symbol_H)
#Gets BMI
def get_BMI(W,H):
    Hs = H*H
    BMIExacto = W/Hs
    BMI = round(BMIExacto,2)
    return BMI
#BMI received
BMIV = get_BMI(W, H)
#Loading
print(f"Loading...")
sleep(1.03) #I entered the value cause writing floats is cool
print(f"Calculating...")
sleep(1.26)# Same reason
#Calculates BMI
def BMI(bmi):
    if bmi<18.5:
        review = "Underweight"
    elif bmi<24.9:
        review = "Health weight"
    elif bmi<29.9:
        review = "Over weight"
    elif bmi>30:#U can write else statement here if u want
        review = "Obese"
    return review
#Gets review
review = BMI(BMIV)
#Prints BMI
print(f"Your BMI is {BMIV} \n Our review states that u are {review}")

