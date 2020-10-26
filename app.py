import get_input as get
import bundle_list as bl
import password_generator as generator
import check_point as check
import get_entropy

length = get.get_input()
bundle = bl.bundle_list(bl.UPPERCASE, bl.LOWERCASE, bl.NUMBERS, bl.SPECIAL)
password = generator.password_generator(bundle, length)
password = check.check_point(password)
if not password:
    password = generator.password_generator(bundle, length)
h = get_entropy.get_entropy(bundle, password)
print('Your new password is: ', password)
print("The password entropy is: ", '%.2f' % h, "which means that the password generated is secure.")
print('Note: one password is considered strong when its entropy is greater than 50')