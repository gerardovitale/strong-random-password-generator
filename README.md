# Strong Random Password Generator
#### This is a first version of a python password generator. 
## Overview
The *Strong Random Password Generator* App (app.py) has been built in order to deliver the first **Ironhack** project. As its name suggest, this App generates strong passwords when the length of the desired password is given. The followings are some parameters that have been taken into account:

* The password is created from lowercase set [a-z], uppercase set [A-Z], number set [0-9], and *special characters* set; so the password can have at leats one character of each.
* The length of the password is a parameter that the user must provide, and  because of security issues, the length of the password has a minimum of 8 characters and a maximum of 12; which are the recommended range of characters that should have in oder to be strong.
* The App uses the random module (pseudo-random generator) to cronstruct the password.
* As additional info, the **password entropy** is calculated in order to show how strong is the **password generated**.
* And finally, it has a test.py to generate 'n' password.

## Structure
The main function of the **Strong Random Password Generator** (app.py) is structured on 5 functions as shown below:
1. create_bundle_list.py: creates a bundle (list) from which the `password_generator.py` takes characters to build the password.
2. get_input.py: gets the desired password length from the user, specifically an integer between 8 and 12.
3. password_generator.py: takes the the bundle and the length to randomly generate a strong password.
4. check_password.py: checks if the password has at least one character of each category (uppercase, lowercase, digits and special)
5. calculate_password_entropy.py: calculates the password entropy.
6. test.py: produces 'n' tests of app.py