# -*- coding: utf-8 -*-
import time

ENCRYPT_DICT = {
    'a': 'cda', 'b': 'fba', 'c': 'dvn', 'd': 'hxw', 'e': 'kel', 'f': 'wcg', 'g': 'qjr',
    'h': 'opz', 'i': 'msa', 'j': 'erb', 'k': 'cui', 'l': 'dot', 'm': 'rpe', 'n': 'uyx',
    'o': 'ncz', 'p': 'tfm', 'q': 'htq', 'r': 'hlp', 's': 'wzf', 't': 'zua', 'u': 'bak',
    'v': 'drk', 'w': 'she', 'x': 'foq', 'y': 'dor', 'z': 'imd', 'A': 'cDa', 'B': 'FbA',
    'C': 'Dvn', 'D': 'hxW', 'E': 'Kel', 'F': 'wCG', 'G': 'QJr', 'H': 'OPZ', 'I': 'MsA',
    'J': 'eRb', 'K': 'CUi', 'L': 'DOT', 'M': 'RPe', 'N': 'Uyx', 'O': 'Ncz', 'P': 'TFm',
    'Q': 'htQ', 'R': 'hLP', 'S': 'wZf', 'T': 'ZUA', 'U': 'BaK', 'V': 'dRk', 'W': 'She',
    'X': 'FOq', 'Y': 'doR', 'Z': 'IMD', ' ': '9sb', '!': '..@', '@': '[&8.', '#': '3[]',
    '$': '*g*', '%': '&qX', '^': '000', '&': 'AAA', '*': '5d:', '(': 'z11', ')': '235',
    '-': 'n4-', '_': '9n3', '=': '-=-', '+': '#i#', '[': '(s)', '{': '888', ']': '456',
    '}': '8gh', ';': 'p.,', ':': '^r*', "'": '$3d', '"': '+Zl', '|': 'J.&', '<': '5U{',
    ',': '_S,', '>': '!8+', '.': 'T??', '/': 'Z^^', '?': ';R;', '0': '2zz', '1': '3Tc',
    '2': '4z0', '3': '5-R', '4': '6sW', '5': '7PR', '6': '89F', '7': '997', '8': '10d',
    '9': '11J'
}

DECRYPT_DICT = {v: k for k, v in ENCRYPT_DICT.items()}
def encrypt(text):
    result = []
    for char in text:
        result.append(ENCRYPT_DICT.get(char, char))
    return ''.join(result)

def decrypt(text):
    result = []
    temp = ""
    for char in text:
        temp += char
        if temp in DECRYPT_DICT:
            result.append(DECRYPT_DICT[temp])
            temp = ""
    return ''.join(result)
print("Για κρυπτογράφηση πατήστε 'e'")
time.sleep(1)
print("Για αποκρυπτογράφηση πατήστε 'd'")

choice = input("Επιλογή: ").strip().lower()

while choice not in {'e', 'd'}:
    print("Λανθασμένη επιλογή.")
    choice = input("Επιλογή: ").strip().lower()

if choice == 'e':
    text = input("Πληκτρολογήστε το κείμενο για κρυπτογράφηση: ")
    encrypted_text = encrypt(text)
    print(f"Κρυπτογραφημένο κείμενο: {encrypted_text}")
elif choice == 'd':
    text = input("Πληκτρολογήστε το κείμενο για αποκρυπτογράφηση: ")
    decrypted_text = decrypt(text)
    print(f"Αποκρυπτογραφημένο κείμενο: {decrypted_text}")


