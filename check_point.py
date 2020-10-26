import bundle_list as bl
import password_generator

def check_point(password):
    check_dic = {
        'uppercase': False,
        'lowercase': False,
        'number': False,
        'special': False
    }
    for s in password:
        if s in bl.UPPERCASE:
            check_dic['uppercase'] = True
        elif s in bl.LOWERCASE:
            check_dic['lowercase'] = True
        elif s in bl.NUMBERS:
            check_dic['number'] = True
        elif s in bl.SPECIAL:
            check_dic['special'] = True
    if not all(check_dic.values()):
        return False
    else: 
        return password