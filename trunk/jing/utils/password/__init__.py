# coding: utf-8
import random
import string
from hashlib import md5

def gen_salt(len = 6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(len))

def __hash_pwd(given_pwd, salt):
    m = md5(given_pwd)
    m.update(salt)
    return m.hexdigest()

def gen_pwd_and_salt(given_pwd):
    salt = gen_salt()
    pwd = __hash_pwd(given_pwd, salt)
    return (pwd, salt)

def check_pwd(saved_pwd, saved_salt, given_pwd):
    return saved_pwd == __hash_pwd(given_pwd, saved_salt)

if __name__ == '__main__':
    password = u'111wD'
    password, salt = gen_pwd_and_salt(password.encode('utf8'))
    
    print 'pwd: ', password, ' salt: ', salt
    print check_pwd(password, salt, '111wD')
    print check_pwd(password, salt, '1sd')