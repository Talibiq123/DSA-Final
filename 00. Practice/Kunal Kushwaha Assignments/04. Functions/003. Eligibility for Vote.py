def is_eligible_to_vote(age_input):
    if age_input >= 18:
        return True
    else:
        return False


user_age = int(input("Enter your age: "))


if is_eligible_to_vote(user_age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
