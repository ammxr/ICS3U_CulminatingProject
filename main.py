#-----------------------------------------------------------------------------
# Name:        Hakim Hairstylists Journey (main.py)
# Purpose:     Simulating and portraying use of functions in daily
#          	activity
#
# Author:      Ammar Hakim
# Created:     05-April-2021
# Updated:     09-April-2021
#-----------------------------------------------------------------------------
 
import random
import numpy as np
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
 
logging.debug("Program Starting")
#Functions
def percentCalc(original,percent):
  '''
 Calculates a percentage off of base number to provide for new amounts, values, and costs
     Allows for only float or integer input while raising an error if otherwise. If values met; continues with funtion sending new amount.
  
  Parameters
 ----------
 original : float/int
   Base number for conversion to start at
  percent : float/int
   Percentage at which it is to be multiplied with for a new amount
 
 Returns
 -------
 float
   Converts to the new value amount rounded to 2 decimal places
 Raises
 ------
  TypeError
    Raised incase of input original or percent parameters entered are not an integer or float number.
  ValuError
    Raised if percent is entered as less than or equal to zero.
 '''
  logging.info("Calling percentCalc() using original value of" + str(original) +" and " +str(percent) +"%")
  if not isinstance(original, (int,float)):
    raise TypeError("Invalid original number must enter a number.")
    logging.error("Entered original number is not the correct type.")
  if not isinstance(percent, (int,float)):
    raise TypeError("Invalid discount must enter a number.")
    logging.error("Entered percentage number is not the correct type.")
  #If discount parameter type is not 0-100 or price is smaller than 0 raise ValueError
  elif (percent<0 or percent>100) or percent<0:
    logging.error("Percentage must be between 1-100")
    raise ValueError("percent parameter must within 1-100 range")
  #if all conditions are met continue and return conversion
  else:
    logging.debug("Valid parameters entered, returning calculation.")
    logging.info("Basing from " + str(original) + " applying" + str(percent)+ "% off ")
    returnedValue=float(((100-percent)/100)*original)
    logging.debug("percentCalc function succesfully returned value.")
  #return conversions to 2 decimal places
  return round(returnedValue,2)
 
def pointsProgramCount(adults,childs):
  '''
 Calculates points rewarded to clients dependant on the adults and children cuts they have had on location
     Allows for only float or integer input while raising an error if otherwise. If values met; continues with funtion sending new amount.
  
  Parameters
 ----------
 adults : int
   Number of adults taking trims on site
  childs : int
   Number of children taking trims on site
 
 Returns
 -------
 float
   Points value amount rounded to 2 decimal places
 Raises
 ------
  TypeError
    Raised incase of input adults or children parameters entered are not an integer (cant have decimal of a human).
 '''
  logging.info("Calling pointsProgramCount using adults value of" + str(adults)+" and childs value of " +str(childs))
  if not isinstance(adults, int):
    logging.error("adults value is not the correct type (int or float.")
    raise TypeError("Invalid number of adults must enter integer.")
  if not isinstance(childs, int):
    logging.error("childs value is not the correct type (int or float.")
    raise TypeError("Invalid number of children must enter integer.")
  logging.debug("Valid parameters entered, returning calculation.")
  logging.info("Calculating points with " + str(adults)+ " worth 1 point each and  "+ str(childs) +" worth 0.2 points each")
  adults=adults*1
  childs=childs*0.2
  total=adults+childs
  logging.debug("pointsProgramCount function succesfully returned value.")
  return total
 
 
#Assertion Testing
# Function 1 (percentCalc)
assert percentCalc(10,50) == 5, "50% off 10 is 5"
assert percentCalc(20,20) == 16, "20% off 20 is 4"
passed = False
try:
  percentCalc(111,-20)
except Exception as e:
  if "percent parameter must within 1-100 range" in str(e):
    passed = True
assert passed
 
# Function 2 (pointsProgramCount)
assert pointsProgramCount(1,2) == 1.4, "1 adult point + 0.4 (0.2x2) children points should be equal to 1.4 total"
assert pointsProgramCount(2,4) == 2.8, "2 adult point + 0.8 (0.2x4) children points should be equal to 2.8 total"
assert pointsProgramCount(0,0) == 0, "No people should be equal to no points"



 
#Main Program
 
#Introduction of first client
print("You just got your first customer today!!!")
print('Knowing she would like a trim you present a variety of ideas ranging lengths from approx 50% ,65%,75%,80%,85% of total hair length')

#Establishing integer value for valid inputs for loops to come
validHowShort= (50,65,75,80,85)

#Sets valid to 0 to initiate and key an exit for the while loop
valid=0
while valid==0:
  try:  
    #Asks for integer input
    howShort = int(input("How short would she liker her hair? "))
    #If integer is not of the valid input raises exception
    if howShort not in validHowShort:
      raise Exception
    #If valid then sets valid to 1 to exit loop
    else:
      valid=1
  except:
    #If error is to occur or invalid integer is entered it loops the input question.
    print('Please from our availible trims; 50%, 65%,75%, 80%, 85% \n TYPE INTEGER ONLY ')
#When valid=1 it permits calling of function to convert to the new hair length
else:
  returnedValue=percentCalc(12,howShort)
  logging.info("Program called percentCalc function using 12 inches as the original value and " +str(howShort) +"% as the percent being cut off")
  print("---Great with that being said if her hair is 12inches long her new trim must be at "+str(returnedValue) +"inches long")

  
#Pricing on Annual Anniversary
print('\nHere at Hakim Hairstylists annual anniversy, our rates are inversely proportional to the trim length in which is cut \n Ex: with 60% trim you are charged 40% off the base cost')
print('---\nWith the base cost being $40 how much would the your Clients trim cost them? ')

#Price is inversely proportional to cut length.
cost1= 100-howShort
# Calling function to return new price to variable for answer check
returnedValue=percentCalc(40,cost1)
logging.info("Program called percentCalc function using $40 as the original value and " +str(cost1) +"% as the percent being cut off")
#Guess Validity Check
valid=False
while valid==False:
    try:
      costGuess = float(input("Enter your guess "))
      #If both Guess and Answer are equal: Question was answered correctly
      if costGuess==returnedValue:
        logging.debug("Guess was equal to the returned answer")
        print('-----')
        print("CORRECT!!!")
        print('-----')
        #Valid set True (to exit loop)
        valid=True
      #if answer is not correct, prompt incorrect message+loop till correct answer.
      elif costGuess>40 or costGuess<0:
        print('Invalid response, number must be positive & lower than 40 ')
      else:
        print('Wrong; please try again')
        logging.debug("Guess "+str(costGuess) + " was not equal to the answer")
        #Valid set False (to keep cycling loop)
        valid=False
  #If any Value is not a float value it may return error message
    except ValueError:
      print('Incorrect value: Please enter an integer!')
logging.debug("All went well with guessing cost with first discount , proceeding to next segment.")
 
 
#List of promotional offers based off day of the week (Sun-Sat)
promotionalOffers= [25, 10, 13, 0, 0, 5, 5]
print("On regular days however, your company offers many great prices for the average client, however this all depends on the day. ")
#Valid set to False to enter loop
valid=False
while valid==False:
    try:
        #Asking for integer reply of day of the week
        week = int(input("What day of the week is it today? "))
        if week < 1 or week > 7:
            print("Please enter a number between 1-7")
            valid=False
        #Day-index of promotional discounts   
        elif week >= 1 and week <= 7:
            if week == 1:
                dayChosen= "Sunday"
                discount= promotionalOffers[0]
            elif week == 2:
                dayChosen= "Monday"
                discount= promotionalOffers[1]
            elif week == 3:
                dayChosen= "Tuesday"
                discount= promotionalOffers[2]
            elif week == 4:
                dayChosen= "Wednesday"
                discount= promotionalOffers[3]
            elif week == 5:
                dayChosen= "Thursday"
                discount= promotionalOffers[4]
            elif week == 6:
                dayChosen= "Friday"
                discount= promotionalOffers[5]
            elif week == 7:
                dayChosen= "Saturday"
                discount= promotionalOffers[6]
            #If all goes well exits loop
            valid=True
            logging.info("Assigned dayChosen as" +str(dayChosen) +"to assign discount later to be used function")
    except Exception:
        #If integer value is not given prints error message
        print("Error Occured: \n  Must enter number between 1-7 : ")
#Saturday Special Discount
#50% chance of a Saturday having a discount of 40% off
if dayChosen=="Saturday":
  #Chooses random number
  randomSaturday = random.randrange(1, 101)
  #If number is even then changes Saturdays discount index to 40% off
  if randomSaturday%2 == 0:
      promotionalOffers.remove(5)
      promotionalOffers.append(40)
#Discount gained depending on day of week
print("With your chosen day being " +dayChosen +" you gain " +str(discount) +"% off")
#Final Price depending on chosen day
logging.info("Using " +str(returnedValue) + " as a base now  calling function to apply a dicount using a percentage of " +str(discount))
finalCost=percentCalc(returnedValue,discount)
print("______________\nYour final price will be $" +str(finalCost) +"\n______________")
 
#Using percentages to calculate stock
print('A customer books an online appointment to dye their hair for saturday. You noticing your short on dye ask for the color on your website. What colour did she choose? Please enter a colour from the list below:')
#Options for hairdye colours
hairColours=["black", "brown", "gray", "blonde", "red", "blue", "green", "pink", "purple"]
print(*hairColours,sep = ", ")
valid=False
#Lets customer choose preffered colour
chosenColour=input("Enter your preffered colour: ")
while chosenColour.lower() not in hairColours:
    print("We do not currently serve that colour, Please choose fromt he list printed above: ")
    chosenColour=input("Enter your preffered colour: ")
logging.debug("Hairdye colour input succesfull proceeding to stock")
 
#Stock dictionary for each colour with random used capacity 1-40%
colourStock={"black":(random.randint(1, 40)), "brown":(random.randint(1, 40)), "gray":(random.randint(1, 40)), "blonde":(random.randint(1, 40)), "red":(random.randint(1, 40)), "blue":(random.randint(1, 40)), "green":(random.randint(1, 40)), "pink":(random.randint(1, 40)), "purple":(random.randint(1, 40))}
logging.debug("Succesfully assigned base values to stock of all supported colors proceeding to pre-function math ")
 
#Filling up stock
print("With a current stock of "+chosenColour +" dye being at " +str(colourStock[chosenColour])+"% of full capacity your company makes an order to fill 100%")
#How much more is needed if 20bottles = random %
print("If you had 20 bottles how many MORE bottles would you need to fill the max capacity?")
#Math inversing percentage formula
bottlesCalc1=(1-((100-int(colourStock[chosenColour]))/100))
bottlesCalc2=(20/bottlesCalc1)
bottlesFinalCalc= round((bottlesCalc2-20),2)
#Checking Answers by calling function
bottlesAnswer=percentCalc(bottlesCalc2,(colourStock[chosenColour]))
bottlesAnswer=round(bottlesAnswer,0)
valid=0
#Allows for 4 total attempts
while valid<3:
  try:
    #Expecting integer value guessed otherwise forwarded to except
    bottlesGuess= int(input('How many MORE!! bottles would be required to fill at 100% stock?'))
    logging.info("Assigning guess value to later compare with answer value returned by pointsProgramCount() function.")
    #If guess is correct exit loop
    if bottlesAnswer==bottlesGuess:
      print("\nYOU GOT IT CORRECT")
      valid=4
    #Else raise exception
    else:
      raise Exception
  except:
    #Error adds valid+1 to allow for maximum attempts
    print("\nIncorrect, please try again (3 more attempts)")
    valid+=1
    #If not guessed in attempts print answer
    if valid==3:
      print('You took too many tries the answer was '+str(bottlesAnswer))
      logging.debug("User took too many tries succesfully printed answer proceeding to points program")
 
 
#Points Program
print("-----------\nHere at Hakim Hairstylists, we take a modern approach and know customers are all about rewards. So we established a POINTS PROGRAM!! \nFor every 20 points a customer gains they are ellible to recieve 1 free haircut")
print('Oooo here comes another group of people! How many people are here? Please specify adults and children')
#Input on how many people you see coming in
#Entering loop with valid=False
valid=False
while valid==False:
    try:
        #Number of adults
        specifiedAdults = int(input("--How many adults? (if None enter 0) "))
        logging.info("Adult value interger succesfully assigned now exiting loop")
        #Exitting loop
        valid=True
    except Exception:
        #If value is not integer continues through loop
        print("Error Occured: \n  Must enter an integer value: ")
valid=False
while valid==False:
    try:
        #Number of children
        specifiedChilds = int(input("--How many children? (if None enter 0) "))
        logging.info("Childs value interger succesfully assigned now exiting loop")
        #Exitting loop
        valid=True
    except Exception:
        #If value is not integer continues through loop
        print("Error Occured: \n  Must enter an integer value: ")
 
logging.debug("Valid parameters entered for points calculation proceeding to call on function")
#If all goes well calls on function and returns points value
pointsValue=pointsProgramCount(specifiedAdults,specifiedChilds)
print("Therefore they now have "+str(pointsValue) +" points")
logging.info("Function succesfully called")
 
print("\nMoving on, recently due to the pandemic, your company is quite limited on the permitted population allowed in-store.\nSpecifically the building is capped at 10 people in-store at a time")
 
#Reversing points to solve for amount of people in-store
print("Assuming there are 6 adults in store with the combined points of 7 points. How many children are present?")
#Entering loop
valid=False
while valid==False:
  try:
    #Expecting integer input for number of children guess
    childrenNumber= int(input("Remember 1pt/adult and 0.2pts/child \nEnter your Guess "))
    logging.info("Correct type of parameter entered for childrenNumber ")
    #If guess is correct proceed out of loop
    if childrenNumber==5:
      print("--------\nCorrect!!\n--------")
      #Exits loop
      valid=True
    #Else raise error
    else:
      raise Exception
  except:
    #Continues loop
    print("Wrong please try again: ")
#Once loop is exit print result
#How many people allowed in-store and whom must wait outside
checkAns=pointsProgramCount(6,5)
 
if (childrenNumber*0.2)+6==checkAns:
  print("\nTherefore since there is 11 total people 1 must wait outside")
else:
  print('False answer entered')
 
print('This can also be checked by counting induvidually as shown below using 2 different methods ')
#Since range does not allow our float values which is needed for our count (0.2pts/child) we can go up by a common value instead of a 1 number gap, we do 1*5 which is a 5 number gap to make our step also 1.
print("---------Method 1 Persons------------")
for count1 in range(1, 6, 1):
  logging.debug("Printed 5 steps (1 each) to show for loop.")
  print("+1 child count at " +str(count1))
 
print("---------Method 2 Points------------")
#However with the help of a library numpy, we may use arrange to do the same with sensible non-converted numbers.
for count2 in np.arange(0, 1, 0.2):
    logging.debug("Printed 5 steps (0.2 each) to show for loop.")
    print("+1 child count at "+str(count2))
 
#Program End
print("____________________________\n Thank you for participating in this journey of Hakim Hairstylists")
 
logging.debug("Program Finished")