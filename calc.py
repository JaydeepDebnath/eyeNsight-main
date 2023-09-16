import predictor
import pyttsx3
engine = pyttsx3.init()

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

while True:
    
    # Narrate all the gestures for operations that can be done
    engine.say("Gestures for operations select accordingly.")
    engine.runAndWait()
    engine.say("Left hand Open palm:- Addition")
    engine.runAndWait()
    engine.say("Left hand close fist:- Substraction")
    engine.runAndWait()
    engine.say("Left hand index finger:- Multiply")
    engine.runAndWait()
    engine.say("left hand ok sign:- Divide")
    engine.runAndWait()
    
    # take input from the user
    choice = predictor.pred()

    # check if choice is one of the four options
    if choice in ('l1', 'l2', 'l3', 'l4'):
        
        # Enter the 1st number
        c1 = "r2"
        while c1 == "r2":
            
            # Narrate all the numbers that can be entered and all their respective gestures
            engine.say("Enter the 1st number")
            engine.runAndWait()
            engine.say("Available gestures:-")
            engine.runAndWait()
            engine.say("Right hand Open palm:- 1")
            engine.runAndWait()
            engine.say("Right hand close fist:- 2")
            engine.runAndWait()
            engine.say("Right hand index finger:- 3")
            engine.runAndWait()
            engine.say("Right hand ok sign:- 4")
            engine.runAndWait()
            
            num_1 = predictor.pred()
            
            if num_1 == "r1":
                num1 = 1
            if num_1 == "r2":
                num1 = 2
            if num_1 == "r3":
                num1 = 3
            if num_1 == "r4":
                num1 = 4
            
            # Confirm if the predicted number is corect
            engine.say("The predicted number is: "+ str(num1))
            engine.runAndWait()
            engine.say("Is it correct?")
            engine.runAndWait()
            engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
            engine.runAndWait()
            
            confirm = predictor.pred()
            
            if confirm == "r2":
                
                # Ask if the user wants to enter another digit
                engine.say("Do you want to enter another digit to this number?")
                engine.runAndWait()
                engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                engine.runAndWait()
                
                c1 = predictor.pred()
                
                # End input cycle
                if c1 == "l2":
                    break
                
                counter = 10
                
                while c1 == "r2":
                    
                    engine.say("Enter the number")
                    engine.runAndWait()
                    engine.say("Available gestures:-")
                    engine.runAndWait()
                    engine.say("Right hand Open palm:- 1")
                    engine.runAndWait()
                    engine.say("Right hand close fist:- 2")
                    engine.runAndWait()
                    engine.say("Right hand index finger:- 3")
                    engine.runAndWait()
                    engine.say("Right hand ok sign:- 4")
                    engine.runAndWait()
                    
                    num_1 = predictor.pred()
                    
                    if num_1 == "r1":
                        num1_ = 1
                    if num_1 == "r2":
                        num1_ = 2
                    if num_1 == "r3":
                        num1_ = 3
                    if num_1 == "r4":
                        num1_ = 4
                    
                    engine.say("The predicted number is: "+ str(num1_))
                    engine.runAndWait()
                    engine.say("Is it correct?")
                    engine.runAndWait()
                    engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                    engine.runAndWait()
                    
                    c2 = predictor.pred()
                    
                    if c2 == "r2":
                        num1 = (num1_* counter) + num1
                        counter = counter *10
                        engine.say("Do you want to continue?")
                        engine.runAndWait()
                        engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                        engine.runAndWait()
                        c1 = predictor.pred()
                    else :
                        engine.say("Do you want to continue?")
                        engine.runAndWait()
                        engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                        engine.runAndWait()
                        c1 = predictor.pred()
            
            if confirm == "l2":
                engine.say("Sorry for the wrong prediction. Please try again")
                engine.runAndWait()
        
        # Enter the 2st number
        c1 = "r2"
        while c1 == "r2":
            
            # Narrate all the numbers that can be entered and all their respective gestures
            engine.say("Enter the 2nd number")
            engine.runAndWait()
            engine.say("Available gestures:-")
            engine.runAndWait()
            engine.say("Right hand Open palm:- 1")
            engine.runAndWait()
            engine.say("Right hand close fist:- 2")
            engine.runAndWait()
            engine.say("Right hand index finger:- 3")
            engine.runAndWait()
            engine.say("Right hand ok sign:- 4")
            engine.runAndWait()
            
            num_2 = predictor.pred()
            
            if num_2 == "r1":
                num2 = 1
            if num_2 == "r2":
                num2 = 2
            if num_2 == "r3":
                num2 = 3
            if num_2 == "r4":
                num2 = 4
            
            # Confirm if the predicted number is corect
            engine.say("The predicted number is: " + str(num2))
            engine.runAndWait()
            engine.say("Is it correct?")
            engine.runAndWait()
            engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
            engine.runAndWait()
            
            confirm = predictor.pred()
            
            if confirm == "r2":
                
                engine.say("Do you want to enter another digit to this number?")
                engine.runAndWait()
                engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                engine.runAndWait()
                
                c1 = predictor.pred()
                
                # End input cycle
                if c1 == "l2":
                    break
                
                counter = 10
                
                while c1 == "r2":
                    
                    engine.say("Enter the number")
                    engine.runAndWait()
                    engine.say("Available gestures:-")
                    engine.runAndWait()
                    engine.say("Right hand Open palm:- 1")
                    engine.runAndWait()
                    engine.say("Right hand close fist:- 2")
                    engine.runAndWait()
                    engine.say("Right hand index finger:- 3")
                    engine.runAndWait()
                    engine.say("Right hand ok sign:- 4")
                    engine.runAndWait()
                    
                    num_2 = predictor.pred()
                    
                    if num_2 == "r1":
                        num2_ = 1
                    if num_2 == "r2":
                        num2_ = 2
                    if num_2 == "r3":
                        num2_ = 3
                    if num_2 == "r4":
                        num2_ = 4
                    
                    engine.say("The predicted number is: "+ str(num2_))
                    engine.runAndWait()
                    engine.say("Is it correct?")
                    engine.runAndWait()
                    engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                    engine.runAndWait()
                    
                    c2 = predictor.pred()
                    
                    if c2 == "r2":
                        num2 = (num2_* counter) + num2
                        counter = counter *10
                        engine.say("Do you want to continue?")
                        engine.runAndWait()
                        engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                        engine.runAndWait()
                        c1 = predictor.pred()
                    else :
                        engine.say("Do you want to continue?")
                        engine.runAndWait()
                        engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
                        engine.runAndWait()
                        c1 = predictor.pred()
            
            if confirm == "l2":
                engine.say("Sorry for the wrong prediction. Please try again")
                engine.runAndWait()

        if choice == 'l1':
            result = add(num1, num2)
            # say the result
            engine.say("The sum of" + str(num1) + "and" + str(num2) + "is" + str(result))
            engine.runAndWait()

        elif choice == 'l2':
            result = subtract(num1, num2)
            # say the result
            engine.say("The substraction of" + str(num1) + "and" + str(num2) + "is" + str(result))
            engine.runAndWait()

        elif choice == 'l3':
            result = multiply(num1, num2)
            # say the result
            engine.say("The Multiplication of" + str(num1) + "and" + str(num2) + "is" + str(result))
            engine.runAndWait()

        elif choice == 'l4':
            result = divide(num1, num2)
            # say the result
            engine.say("The division of" + str(num1) + "and" + str(num2) + "is" + str(result))
            engine.runAndWait()
        
    # check if user wants another calculation
    engine.say("Do you want to do another calculation?")
    engine.runAndWait()
    engine.say("Show your Right hand closed fist to confirm and left hand closed fist for no")
    engine.runAndWait()
    
    next_calculation = predictor.pred()

    # break the while loop if answer is no    
    if next_calculation == "l2":
        engine.say("Thankyou for using our app. Hope to see you again")
        engine.runAndWait()
        break
    
    else:
        print("Invalid Input")