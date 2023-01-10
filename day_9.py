# wap to check entry of the user in pub based on if he is minor or not and tells suggestion to apply after certain years

def check_pub_entry():
    age = int(input("What is your age? "))

    if age < 18:
        print("You are not legally allowed to enter a pub, come back after " + str(18 - age) + " years.")
    else:
        print("You are legally allowed to enter a pub.")

check_pub_entry()