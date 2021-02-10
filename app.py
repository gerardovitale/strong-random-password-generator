from modules.get_input import get_input
import modules.create_bundle_list as cbl
from modules.password_generator import password_generator
from modules.check_password import check_password
from modules.calculate_password_entropy import calculate_password_entropy

def app():
    length = get_input()
    bundle = cbl.create_bundle_list(cbl.UPPERCASE, cbl.LOWERCASE, cbl.NUMBERS, cbl.SPECIAL)
    password = False
    while not password:
        password = password_generator(bundle, length)
        password = check_password(password)
    entropy = calculate_password_entropy(bundle, password)
    print('Your new password is: ', password)
    print("The password entropy is: ", '%.2f' % entropy, "which means that the password generated is secure.")
    print('Note: one password is considered strong when its entropy is greater than 50')

if __name__ == "__main__":
    app()