from translate import Translator

try:
    with open('text.txt') as my_file:
        text = my_file.read()
    translated = Translator(to_lang='fr')
    print(translated.translate(text))
except FileNotFoundError:
    print('File does not exist')
