
#Password Strength Checker
#Author: Ismaeel Mahfooz
#Description: Checks password strength based on length and character variety.

import string

def check_password_strength(password):
    
    #Evaluates the strength of a password based on character variety and length.
    #Returns a strength rating and feedback list.
    
    strength_points = 0
    feedback = []

    # Check length
    if len(password) < 6:
        feedback.append("Password is too short (minimum 6 characters).")
    elif len(password) >= 8:
        strength_points += 1

    # Check for uppercase
    if any(char.isupper() for char in password):
        strength_points += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase
    if any(char.islower() for char in password):
        strength_points += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        strength_points += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        strength_points += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, ?).")

    # Final evaluation
    if strength_points <= 2:
        strength = "Weak"
    elif strength_points == 3 or strength_points == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print("-", tip)

