import json
import requests


def get_translation_json():
    url = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
    resp = requests.get(url)
    return json.loads(resp.text)


def generate_word_list(input_file):
    word_list = []
    for line in input_file:
        for word in line.split(" "):
            word_list.append(word)
    return word_list



def translate_to_lolcat(word_list, translation_dictionary):
    translated_string = ''
    for word in word_list:
        translation = translation_dictionary.get(word, word)
        translated_string += translation + ' '
    return translated_string


def main():
    translation_dictionary = get_translation_json()

    file_name = input("Enter file name to translate: ")
    name_file = input('Enter a name for the translated file: ')
    input_file = open(file_name, 'r')
    word_list = generate_word_list(input_file)
    

    translated_string = translate_to_lolcat(word_list, translation_dictionary)

    translated_text_file = open(name_file, 'w')
    translated_text_file.write(translated_string)
    translated_text_file.close()


if(__name__ == '__main__'):
    main()