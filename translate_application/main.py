from translate import Translator


def delimiter_lines(func):
    def wrapper():
        print('*' * 13)
        func()

    return wrapper


@delimiter_lines
def print_main_menu():
    print('(t)ranslate')
    print('e(x)it')


def get_translation(text, lang):
    trans = Translator(to_lang=lang)
    return trans.translate(text)


def is_target_language_valid(lang):
    return lang and len(lang) == 2


if __name__ == '__main__':
    while True:
        print_main_menu()
        menu_option = input('Please choose an action: ')

        if menu_option.upper() == 'X':
            print('Bye!')
            break
        elif menu_option.upper() == 'T':
            txt_to_translate = input('Enter the string to translate: ')
            target_language = input('Enter the target language: ')

            if is_target_language_valid(target_language):
                print(f'Your {target_language} translated text is:')
                print(get_translation(txt_to_translate, target_language))
            else:
                print('Invalid language. Please retry!')
        else:
            print('Invalid command, please try again!')
