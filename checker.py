# Ground rules: password should be atleast 8 characters, 1 uppercase character, atleast 1 number, 1 special character, 1 lowercase character
# A password score of max of 6?
# provide suggestions just like a actual password checker 


def check_strength(password):
    score = 0
    feedback = []

    # First, I check how long the password is
    if len(password) >= 12:
        score += 2  # really good length
    elif len(password) >= 8:
        score += 1  # decent length
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Now I'm checking if the password has at least one big (uppercase) letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Now I'm checking for a lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Checking if it has a number
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Now I check for special characters like ! or @
    special_characters = "!@#$%^&*()-_=+{};:,.<>"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if has_special:
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$ etc).")


        # Now I print the final score and give feedback
    print("Password Score: " + str(score) + " / 6")     # Show score out of 6
    if score >= 6:
        print("Strong password.")                      
    elif score >= 4:
        print("Moderate password.")                  
    else:
        print("Weak password.")                         

    # If I found any problems I could maybe print some tips to the user
    if len(feedback) > 0:
        print("Suggestions:")                          
        for tip in feedback:
            print(" - " + tip)                       

    return score                                     
#successs!!!!!!!!

#phase 2 keep asking the user to enter a proper password until they get a perfect score 
while True:                                             
    user_password = input("Enter a password to check: ")  
                                                        
    result = check_strength(user_password)              
    if result >= 6:                                     
        break                                           
    print("Please try again with a stronger password.") 
                                                       
# sucesss!!!!!!!!!!
