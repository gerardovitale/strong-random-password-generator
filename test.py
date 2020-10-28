import modules.get_input as get
import modules.bundle_list as bl
import modules.password_generator as generator
import modules.check_point as check
import modules.get_entropy as entropy

def test():
    try:
        n = int(input('Provide an integer n to run n times the pasword generator app: '))
    except ValueError:
        print('An integer must be provided')
    for i in range(n):
        length = get.get_input()
        bundle = bl.bundle_list(bl.UPPERCASE, bl.LOWERCASE, bl.NUMBERS, bl.SPECIAL)
        password = generator.password_generator(bundle, length)
        password = check.check_point(password)
        if not password:
            password = generator.password_generator(bundle, length)
        h = entropy.get_entropy(bundle, password)
        print('Your new password is: ', password)
        print("The password entropy is: ", '%.2f' % h, "which means that the password generated is secure.")

test()