#Local Python Setup Exercise

# Practice function #1
# Create a function that prints a greeting to a user 
def hello():
    print("Greetings! Have a nice day!")

hello()

# Practice function #2
# Create a function that accepts three arguments and returns a single list with
# the three arguments as elements


def pack(one, two, three):
    return [one, two, three]

print(pack("one", "two", "three"))


#Practice function #3
# Create a function that accepts a list of any length, and print out a series of 
# strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 


def eat_lunch(lunch_meal):
    
    if len(lunch_meal) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch_meal)):
            if i == 0:
                print(f"First I eat {lunch_meal[0]}")
            else:
                print(f"Next I eat {lunch_meal[i]}")
                     
                

eat_lunch([])
eat_lunch(["a Salad"])
eat_lunch(["a Salad", "a Sandwich", "Pudding", "Cake"])