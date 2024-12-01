#Using import statement to get access to code from another module by importing the file/function 

should_continue = False


while not should_continue:
    user_choice = input("Please choose which code to run. Type between [1 to 2]: ")

    match user_choice:
        case "1":
            import bandname  #Working with variables to manage data
        case "2":
            import tipcalculator #Working with data types

    continue_selection = input("Would you like to try other options? Please type 'yes' or 'no': ").lower()

    if continue_selection == "no":
        should_continue = True
