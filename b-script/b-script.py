#!/usr/bin/env python3

def to_upper(char_list):
    return list(map(lambda char: char.upper(), char_list))

def main():
    english_vowels = ['a', 'e', 'i', 'o', 'u']
    english_vowels = english_vowels + to_upper(english_vowels)

    czech_vowels = english_vowels + ['y', 'á', 'é', 'í', 'ó', 'ú', 'ů', 'ě']
    czech_vowels = czech_vowels + to_upper(czech_vowels)

    base_constonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    english_constonants = base_constonants + ['y']
    english_constonants = english_constonants + to_upper(english_constonants)

    czech_constonants = base_constonants + ['š', 'č', 'ř', 'ž', 'ť', 'ď']
    czech_constonants = czech_constonants + to_upper(czech_constonants)

    black_list = ['v', 'd', 'p']

    for line in sys.stdin:
        new_line = "".join(list(map(lambda char: '🅱️' if char in black_list else char, line)))
        print(new_line, end='')
        

if __name__ == "__main__":
    import sys
    main()
