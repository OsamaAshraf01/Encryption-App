# GLOBAL VARIABLES
import sys
KEY_CODE = 0b101010101
# ---------------------------------------


def main_loop():
    while True:
        print('----------------------------------------')
        print('Choose Operation:\n 1)Encrypt \n 2)Decipher \n 0)Exit')
        print('----------------------------------------')
        operation = input()
        try:
            check_operation(operation)
        except:
            print('Enter a valid choice !')


def check_operation(operation):
    if operation == '1':
        k = int(input('Enter your key[0:9999]: '))
        message = input('Enter your message: ')
        X = encrypt(message, k)
        print('Encrypted :', X)

    elif operation == '2':
        message = input('Enter your Encrypted message: ')
        try:
            X = decipher(message)
            print('Real Message :', X)
        except:
            print('Can not decipher !')
            
    elif operation == '0':
        sys.exit()
    else:
        print('Enter valid choice !')


def list_key(key):
    l_key = ['0', '0', '0', '0']
    s_key = str(key)
    for i in range(1, len(s_key) + 1):
        l_key[-i] = s_key[-i]

    return l_key


def append_encrypted_key(msg, key):
    l_key = list_key(key)
    for i in range(4):
        msg += chr(int(ord(l_key[i])) ^ KEY_CODE)

    return msg


def decipher_key(e_key):
    x = ''
    for c in e_key:
        x += chr(int(ord(c)) ^ KEY_CODE)

    return int(x)


def apply_key(msg, key):
    x = ''
    for c in msg:
        x += chr(int(ord(c)) ^ key)
    return x


def encrypt(word, key):
    word = apply_key(word, key)
    word = append_encrypted_key(word, key)
    return word


def decipher(e_message):
    key = decipher_key(e_message[-4:])  # Get Key
    e_message = e_message[:-4]          # Remove key from encrypted message

    x = apply_key(e_message, key)
    return x
