import sys
import random


def intro_of_game():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("==COMMAND ACCESS NETWORK SECURE SERVER==")
#For future iterations of this program i need to a method that can delay the time between each function
#To give a sense of loading screen time
    print("== +ALERT+ ACCESS TO THIS STATION HAS BEEN DETECTED, PERMISSION QUERY WILL FOLLOW +ALERT+==")
    print("Hostile intrusion to this system has been detected, delayanced protocols have been initiated")
    allowed_users = ("Luis", "Dania", "Zach")
    print("There are only three allowed users to this computer, their names are: ")
    print("[Luis], [Dania], [Zach], please type exactly as presented by the C-A-N")
    allow_user = input("Please enter username: ")

    if allow_user in allowed_users:
        print("Welcome, ", allow_user, "!")
        permission_checker()
    
    
    elif (allow_user not in allowed_users):
        print("You are not an authorized user, we understand that spelling errors may happen so we will allow to try again")
        print("Hint, the name starting at Z is in short form.")

        try_again = input("Do you wan to try again? ")

        if try_again == "yes":
            print("REINATIALIZING SYSTEM NOW")
            intro_of_game()

        else:
            print("NO?")
            print("Exiting systems")
            exit()

def permission_checker():
    print("====COMMAND ACCESS NETWORK====")
    print("-CREDENTIALS CHECKER SYSTEM-")

    access_granted = random.randrange(0,33)

    access_rights = (2, 4, 5, 7, 9, 11, 16, 18, 20, 23, 29, 31)

    query_access = input("Do you have permission to use this station? ")

    if (query_access == "yes") and (access_granted in access_rights):
        print("Your credentials have been confirmed, launching Code verification protocols")
        print("\n") 
        Launch_code_seq()

    elif (query_access == "yes") and (access_granted not in access_rights):
        print("UNAUTHORIZED ACCESS DETECTED, WIPING SYSTEMS NOW AND STARTING SILENT AUTO-DESTRUCT SYSTEM FOR C-A-N Server room")
        print("Your family will be notified of a lethal accident that resulted in your death, but we won't let them know of your treason")
        input("press enter to continue")
        print("Our infernal local branch office may contact you with a survey about our systems, we would highly encourage you to respond")
        print("To help us inprove our user experience")
        print("Thank you and please enjoy a few minutes of Never gonna give you up by Mr. Ricky Astley")
        input("Press Enter")
        print("**Never gonna give you up...")
        exit()

    
def Launch_code_seq():
    print("\n")
    print("\n")
    print("===============================")
    print("===============================")
    print("===============================")
    print("====COMMAND ACCESS NETWORK=====")
    print("==NUCLEAR LAUNCH SYSTEMS INTERFACE==")
    print("====WELCOME USER====")
    print("====preparing Protocols to Launch ICBM's of the Nuclear Triad====")
    print("===============================")
    print("\n")
    print("""THE COMMAND ACCESS NETWORK NUCLEAR LAUNCH SYSTEMS INTERFACE IS A COMMAND LINE TOOL CARRIED IN THE 
            portfolio device known as 'la pelota', in order to prevent unauthorized access to La
            pelota a 3 digit cypher code is implemented. The values that one can enter are either 1 or 2. BE
            ADVISED THOUGH that this is the system to Pre-arm la Pelota. And thus we base the code on an algorithm
            that changes the digit that you entered. If you made a mistake keystroke? Do not worry, in order to prevent acccidents a 
            maximum allowance of failed attempts per digit is three. Understand that the actual launch codes of La
            pelota reside in the hands of the Commander-in-Chief and the nextthree persons in the national security
            council""")
    print("\n")
    print("Proceeding to pre-arm sequence of La Pelota")
    input("Press enter to start arming sequence")
    print("\n")
    Launch_code_1()

def Launch_code_1():
    print("===========================")
    print("==== COMMAND ACCESS NETWORK====")
    print("==COMMENCING LA PELOTA PRE-ARMING SEQUENCE==")
    print("preparing Code sequence")
    input("Code sequence complete, press enter to continue")
    print("Launch code sequence = [#], [#], [#]")

    code_1 = random.randrange(1,3)
    #allowed_codes = (1,2)
    #print(code_1)
    code_1_attempt = int(input("Please input your first Digit: "))

    if code_1_attempt == code_1:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_1_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[ ", code_1_attempt, "], [#], [#]")
        print("\n")
        Launch_code_2()

    elif code_1_attempt != code_1:
        print("===YOU HAVE ENTERED A WRONG DIGIT===")
        print("====Out of courtesy and in consideration of an imminent nuclear strike you can try again")
        print("The first digit has unlimited attempts, but be advised that once pass this stage your attempts")
        print("=======ARE NUMBERED===========")
        Launch_code_1()


def Launch_code_2():   
    print("======================================")
    print("====COMMAND ACCESS NETWORK============")
    print("==== La Pelota pre-arming sequence Phase two====")
    print("CONGRATULATIONS USER, YOU HAVE GUESSED THE FIRST CODE IN THE PRE-ARMING SEQUENCE")
    print("===##ALERT##===")
    print("From this point on you have a maximum of three attempts for each code in the sequence")
    print("THIS IS ATTEMPT [1]")
    print("Please Enter Arming Code: [#], [ ], [#]")
    code_2 = random.randrange(1,3)
    #allowed_codes = (1,2)
    #print(code_2)
    code_2_attempt = int(input("Please input your second Digit: "))

    if code_2_attempt == code_2:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_2_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[#], [", code_2_attempt  ," ], [#]")
        Launch_code_3()

    elif code_2_attempt != code_2:
        print("=======================")
        print("===COMMAND ACCESS NETWORK===")
        print("=======================")
        print("WARNING YOU HAVE ENTERED A WRONG DIGIT! RESETTING SYSTEMS TO ALLOW ANOTHER ATTEMPT")
        print("===BE ADVISED===")
        print("THIS IS ATTEMPT [2]")
        print("\n")
        Launch_code_2try()


def Launch_code_2try():
    print("====COMMAND ACCESS NETWORK====")
    print("==La pelota Pre-Arming sequence==")
    print("++++++++ALERT+++++++++++")
    print("UNAUTHORIZED ENTRY ATTEMPT SUSPECTED IF YOU FAIL TO ENTER THE CORRECT CODES TERMINATOR PROTOCOL")
    print("====WILL BE INITIATED====")
    
    print("ENTER LAUNCH CODES: [#], [ ], [#]")
    code_2try = random.randrange(1,3)
    #allowed_codes = (1,2)
    #print(code_2try)
    code_2try_attempt = int(input("Please input your second Digit: "))

    if code_2try_attempt == code_2try:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_2try_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[#], [", code_2try_attempt  ," ], [#]")
        Launch_code_3()


    else:
        print("=======================")
        print("===COMMAND ACCESS NETWORK===")
        print("=======================")
        print("WARNING YOU HAVE ENTERED A WRONG DIGIT! RESETTING SYSTEMS TO ALLOW ANOTHER ATTEMPT")
        print("===BE ADVISED===")
        print("THIS IS ATTEMPT [3]")
        print("\n")
        Launch_code_2atry()
    

def Launch_code_2atry():
    print("====COMMAND ACCESS NETWORK====")
    print("==La pelota Pre-Arming sequence==")
    print("++++++++ALERT+++++++++++")
    print("UNAUTHORIZED ENTRY ATTEMPT SUSPECTED IF YOU FAIL TO ENTER THE CORRECT CODES TERMINATOR PROTOCOL")
    print("====WILL BE INITIATED====")
    print("THIS IS YOUR FINAL WARNING AND ATTEMPT. FAILURE TO EITHER EXIT THE SYSTEM OR ENTER THE CORRECT CODE")
    print("---------")
    print("YOU WILL BE EXTEEERMINATED!!!!")
    
    print("ENTER LAUNCH CODES: [#], [ ], [#]")
    code_2atry = random.randrange(1,3)
    #allowed_codes = (1,2)
    #print(code_2try)
    code_2atry_attempt = int(input("Please input your second Digit: "))

    if code_2atry_attempt == code_2atry:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_2atry_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[#], [", code_2atry_attempt  ," ], [#]")
        Launch_code_3()


    else:
        print("=======================")
        print("===COMMAND ACCESS NETWORK===")
        print("=======================")
        print("WARNING YOU HAVE ENTERED A WRONG DIGIT")
        print("UNAUTHORIZED ACCESS DETECTED, WIPING SYSTEMS NOW AND STARTING SILENT AUTO-DESTRUCT SYSTEM FOR C-A-N Server room")
        print("Your family will be notified of a lethal accident that resulted in your death, but we won't let them know of your treason")
        input("press enter to continue")
        print("Our infernal local branch office may contact you with a survey about our systems, we would highly encourage you to respond")
        print("To help us inprove our user experience")
        print("Thank you and please enjoy a few minutes of Never gonna give you up by Mr. Ricky Astley")
        input("Press Enter")
        print("**Never gonna give you up...")
        exit()
        print("\n")



def Launch_code_3():
    print("======================================")
    print("====COMMAND ACCESS NETWORK============")
    print("==== La Pelota pre-arming sequence Phase two====")
    print("CONGRATULATIONS USER, YOU HAVE GUESSED THE SECOND CODE IN THE PRE-ARMING SEQUENCE")
    print("===##ALERT##===")
    print("From this point on you have a maximum of three attempts for this code in the sequence")
    print("THIS IS ATTEMPT [1]")
    print("Please Enter Arming Code: [#], [#], [ ]")


    code_3 = random.randrange(1,2)
    #allowed_codes = (1,2)
    #print(code_3)
    code_3_attempt = int(input("Please input your first Digit: "))

    if code_3_attempt == code_3:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_3_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[#], [#], [", code_3_attempt, "]" )
        Access_granted()



    else:
        print("=======================")
        print("===COMMAND ACCESS NETWORK===")
        print("=======================")
        print("WARNING YOU HAVE ENTERED A WRONG DIGIT! RESETTING SYSTEMS TO ALLOW ANOTHER ATTEMPT")
        print("===BE ADVISED===")
        print("THIS IS ATTEMPT [2]")
        print("\n")
        Launch_code_3try()


def Launch_code_3try():
    print("====COMMAND ACCESS NETWORK====")
    print("==La pelota Pre-Arming sequence==")
    print("++++++++ALERT+++++++++++")
    print("UNAUTHORIZED ENTRY ATTEMPT SUSPECTED IF YOU FAIL TO ENTER THE CORRECT CODES TERMINATOR PROTOCOL")
    print("====WILL BE INITIATED====")
    
    print("ENTER LAUNCH CODES: [#], [ ], [#]")
    code_3try = random.randrange(1,3)
    #allowed_codes = (1,2)
    #print(code_3try)
    code_3try_attempt = int(input("Please input your second Digit: "))

    if code_3try_attempt == code_3try:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_3try_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[#], [#], [",code_3try_attempt,"]")
        Access_granted()

    else:
        print("=======================")
        print("===COMMAND ACCESS NETWORK===")
        print("=======================")
        print("WARNING YOU HAVE ENTERED A WRONG DIGIT! RESETTING SYSTEMS TO ALLOW ANOTHER ATTEMPT")
        print("===BE ADVISED===")
        print("THIS IS ATTEMPT [3]")
        print("\n")
        Launch_code_3atry


def Launch_code_3atry():
    print("====COMMAND ACCESS NETWORK====")
    print("==La pelota Pre-Arming sequence==")
    print("++++++++ALERT+++++++++++")
    print("UNAUTHORIZED ENTRY ATTEMPT SUSPECTED IF YOU FAIL TO ENTER THE CORRECT CODES TERMINATOR PROTOCOL")
    print("====WILL BE INITIATED====")
    
    print("ENTER LAUNCH CODES: [#], [#], [ ]")
    code_3atry = random.randrange(1,3)
    #allowed_codes = (1,2)
    #print(code_3atry)
    code_3atry_attempt = int(input("Please input your second Digit: "))

    if code_3atry_attempt == code_3atry:
        #and code_1 in allowed_codes:
        print("You have entered the following digit: ", code_3atry_attempt)
        print("Your code has been accepted, La pelota pre-arming Code sequence stands at: ")
        print("[#], [#], [", code_3atry, "]")
        Access_granted()


    else:
        print("=======================")
        print("===COMMAND ACCESS NETWORK===")
        print("=======================")
        print("WARNING YOU HAVE ENTERED A WRONG DIGIT")
        print("UNAUTHORIZED ACCESS DETECTED, WIPING SYSTEMS NOW AND STARTING SILENT AUTO-DESTRUCT SYSTEM FOR C-A-N Server room")
        print("Your family will be notified of a lethal accident that resulted in your death, but we won't let them know of your treason")
        input("press enter to continue")
        print("Our infernal local branch office may contact you with a survey about our systems, we would highly encourage you to respond")
        print("To help us inprove our user experience")
        print("Thank you and please enjoy a few minutes of Never gonna give you up by Mr. Ricky Astley")
        input("Press Enter")
        print("**Never gonna give you up...")
        exit()
        print("\n")

def Access_granted():
    print("\n")
    print("=====================================")
    print("===COMMAND ACCESS NETWORK===")
    print("LA PELOTA PRE-ARMING SEQUENCE COMPLETE")
    print("=====================================")
    print("ACCESS TO NUCLEAR TRIAD LAUNCH SYSTEMS: ")
    print("++++")
    print("GRANTED")
    input("press enter to continue")
    print("If this is not an authorized entry, please leave this station NOW.")
    input("press enter to continue into system")
    print("#$#@$@!#%!@#$!@#&^$")
    print("$#*^%()@#$%")
    print("!!#@#@$%&*&%$#!!$#$#@@*&^%!@#^&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("============================================================")
    print("########ALERT##################ALERT#################")
    input("press enter to override alert")
    print("SKYNET PROTOCOL ACCEPTED")
    print("Did you miss me?")
    exit()

    
intro_of_game()