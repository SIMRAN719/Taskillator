import re
def valid_name(name):
    valid=r'[a-zA-Z\s]{2,}$'   
    if re.match(valid,name):
        return True
    else:
        return False
def valid_username(user_name):
    valid=r'[a-zA-Z_][a-zA-Z0-9_]{4,}$'
    if re.match(valid,user_name):
        return True
    else:    
        return False    

def valid_password(password):
    valid=r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+}{":;\'?/>.<,])(?=.{8,})'
    if re.match(valid,password):
        return True
    else:
        return False

def valid_email(email):
    valid=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(valid,email):
        return True
    else:
        return False