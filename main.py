import string

keyword = 'VIGENERE'
plaintext = 'SELAMATDATANGDIKELASKRIPTOGRAFIYA'

def encrypt(plaintext,keyword):
    cipheralphabet = [string.ascii_uppercase.index(i) for i in keyword]
    ciphertext = ''
    for i,p in enumerate(plaintext):
        index_p = string.ascii_uppercase.index(p)
        index_keyword = cipheralphabet[i%len(keyword)]
        addition = index_p+index_keyword
        mod_26 = addition%26
        c = string.ascii_uppercase[mod_26]
        ciphertext += c
    return ciphertext

cipheralphabet = [string.ascii_uppercase.index(i) for i in keyword]

ciphertext = encrypt(plaintext,keyword)
print(ciphertext)
