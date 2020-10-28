def get_input():
    # Ask one user about her password requirement,
    # specifically about the lenght and the content.
    while True:
        try:
            length = int(input('How long must the password be? Lenght (8 to 12 characthers): '))
            while length < 8  or length > 12:
                print("Sorry, the integer you've provided is not between 8 and 12; please try again.")
                length = int(input('How long must the password be? Lenght (8 to 12 characthers): '))
        except ValueError:
            print('The input provided is not an integer between 8 and 12. Please try again.')
            continue
        else:
            return length