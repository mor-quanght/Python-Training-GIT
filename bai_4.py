import re
def website():
    password=input('password: ')

    list_word=password.split(',')
    out_put=[]

    for password in list_word:
        if check_password(password)!=False:
            out_put.append(check_password(password))

    return out_put






def check_password(password):
    if len(password)>12 or len(password)<6:
        return False
    elif not re.search('[a-z]', password):
        return False
    elif not re.search('[0-9]', password):
        return False
    elif not re.search('[A-Z]', password):
        return False
    elif not re.search('[$#@]', password):
        return False
    else:
        return password


print(website())