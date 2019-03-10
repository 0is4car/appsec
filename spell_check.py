from spellchecker import SpellChecker
import sys

spell = SpellChecker()

def get_text(filename):
    with open(filename,'r') as f:
        text = f.read()

    return text

def check(text):
    print(text)
    text_list = spell.split_words(text)
    misspelled = spell.unknown(text_list)
    print('unknow words:')
    for word in misspelled:
        print(word)

def main():
    try:
        filename = sys.argv[1]
        text = get_text(filename)
    except:
        print('Usage: python spell_check.py <filename>')
        return
    check(text)

if __name__ == '__main__':
    main()
