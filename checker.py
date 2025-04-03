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

    # Now I'm checking for a small (lowercase) letter
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

    # Trying to make sure the password isn’t something super basic or common
    try:
        f = open("common_passwords.txt", "r")
        common_passwords = []
        for line in f:
            common_passwords.append(line.strip())
        f.close()

        if password.lower() in common_passwords:
            score -= 2  # I take away points if it’s a common password
            if score < 0:
                score = 0
            feedback.append("Password is too common. Choose something more unique.")
    except:
        # If the file isn’t there, I just skip this part
        feedback.append("Couldn't check for common passwords (file missing).")

    # Now I print the final score and give feedback
    print("\nPassword Score:", score, "/ 7")
    if score >= 6:
        print("✅ Strong password!")
    elif score >= 4:
        print("🟡 Moderate password.")
    else:
        print("🔴 Weak password.")

    # If I found any problems, I print some tips
    if len(feedback) > 0:
        print("\nSuggestions:")
        for tip in feedback:
            print(" -", tip)

    return score

# This part keeps asking until the password is strong enough
while True:
    user_password = input("Enter a password to check: ")
    result = check_strength(user_password)
    if result >= 6:
        break  # if it's strong, I stop asking
    print("\nPlease try again with a stronger password.\n")
