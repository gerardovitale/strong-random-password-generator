# Strong Random Password Generator
#### This is a first version of a python password generator. 
## Overview
The *Strong Random Password Generator* App (app.py) has been built in order to deliver the first **Ironhack** project and taking into account some basic parameters as following;
* Based on [a-z], [A-Z], [0-9], and even *special characters*.
* At leats one character of each.
* A minimum length of 8 characters and a maximum of 12.
* It use the random module (pseudo-random generator)
* As additional info, the **password entropy** is calculated in order to show how strong is the **password generated**.
* And finally, it has a test.py to generate 'n' password.

## Structure
The main function of the **Strong Random Password Generator** (app.py) is structured on 5 functions as shown below:
1. bundle_list.py: creates a bundle (list) from which the password_generator.py takes inputs.
2. get_input.py: gets the desired password length from the user, specifically an integer between 8 and 12.
3. password_generator.py: takes the the bundle and the length to randomly generate a password.
4. check_point.py: checks if the password has at least one character of each category (uppercase, lowercase, digits and special)
5. get_entropy.py: calculates the password entropy.
6. test.py: produces 'n' tests of app.py