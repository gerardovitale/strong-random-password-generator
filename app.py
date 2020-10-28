import modules.get_input as get
import modules.bundle_list as bl
import modules.password_generator as generator
import modules.check_point as check
import modules.get_entropy as entropy

def app():
    length = get.get_input()
    bundle = bl.bundle_list(bl.UPPERCASE, bl.LOWERCASE, bl.NUMBERS, bl.SPECIAL)
    password = generator.password_generator(bundle, length)
    password = check.check_point(password)
    if not password:
        password = generator.password_generator(bundle, length)
    h = entropy.get_entropy(bundle, password)
    print('Your new password is: ', password)
    print("The password entropy is: ", '%.2f' % h, "which means that the password generated is secure.")
    print('Note: one password is considered strong when its entropy is greater than 50')

if __name__ == "__main__":
    app()