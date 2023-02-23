# Шифрует открытый текст шифром простой замены
def substitution_cipher(open_text):
    open_text            = open_text.lower()
    normal_alphebet      = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    substituted_albhabet = 'глфызшбжхёпвчнкъэдьретсамюцщяуиой'

    ciphered_text = ''
    for char in open_text:
        char_index = normal_alphebet.find(char)
        ciphered_text += substituted_albhabet[char_index]

    return ciphered_text


# Выравнивает ключевое слово по длине шифртекста (нужно для дешифратора Вижернера)
def normalize_key_word(key_word, normal_length):
    k = 0
    while len(key_word) != normal_length:
        key_word += key_word[k]
        k = (k + 1) % len(key_word)
    return key_word

# Дешифатор шифра Виженера
def vigenere_decipher(ciphered_text, key_word):
    alphabet             = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_cardinality = len(alphabet)
    ciphered_text        = ciphered_text.lower()
    key_word = normalize_key_word(key_word.lower(), len(ciphered_text))

    open_text = ''
    for i in range(len(ciphered_text)):
        ciphered_text_char_index = alphabet.find(ciphered_text[i])
        key_word_char_index = alphabet.find(key_word[i])
        open_text_char_index = (ciphered_text_char_index - key_word_char_index) % alphabet_cardinality
        open_text += alphabet[open_text_char_index]

    return open_text