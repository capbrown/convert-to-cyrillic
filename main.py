import eng_to_ipa as ipa
import re

appearance =\
{
    'A': 'A',
    'B': 'Б',
    'C': 'K',
    'D': 'Д',
    'E': 'Э',
    'F': 'Ф',
    'G': 'Г',
    'H': 'H',
    'I': 'И',
    'J': 'Ж',
    'K': 'K',
    'L': 'Л',
    'M': 'M',
    'N': 'И',
    'O': 'Ѳ',
    'P': 'Р',
    'Q': 'Ю',
    'R': 'Я',
    'S': 'C',
    'T': 'T',
    'U': 'Ц',
    'V': 'Ѵ',
    'W': 'Щ',
    'X': 'X',
    'Y': 'У',
    'Z': 'З'
}

sounds =\
{
    # Some common word + sounds not included in:
    #   https://en.wikipedia.org/wiki/Russian_alphabet
    'rəʃən': 'РУССКИЙ',
    'ˈrəʃə': 'РУССИЯ',
    'aɪ': 'я',
    'ð': 'З',
    'ɪ': 'Ы',
    'ə': 'А',
    'æ': 'Э',
    'oʊ': 'О',
    'aʊ': 'O',
    'ʊ': 'У',
    'ˈ': '',
    'ʃ': 'ш',
    'h': 'Х',
    'ŋ': 'НГ',
    'w': 'В',

    # Alphabet
    'a': 'А', 'ɑ': 'А',               # А \
    'b': 'Б', 'bʲ': 'Б',              # Б \
    'v': 'В', 'vʲ': 'В',              # В \
    'g': 'Г', 'gʲ': 'Г',              # Г \
    'd': 'Д', 'dʲ': 'Д',              # Д \
    'je': 'Е', 'ʲe': 'Е', 'ex': 'Е',  # Е \
    'jo': 'Ё', 'ʲo': 'Ё',             # Ё \
    'ʐ': 'Ж',                         # Ж \
    'z': 'З', 'zʲ': 'З',              # З \
    'i': 'И', 'ʲi': 'И', 'ɨx': 'И',   # И \
    'j': 'Й',                         # Й \
    'k': 'К', 'kʲ': 'К',              # К \
    'ɫ': 'Л', 'lʲ': 'Л', 'l': 'Л',    # Л \
    'm': 'М', 'mʲ': 'М',              # М \
    'n': 'Н', 'nʲ': 'Н',              # Н \
    'o': 'О',                         # О \
    'p': 'П', 'pʲ': 'П',              # П \
    'r': 'Р', 'rʲ': 'Р',              # Р \
    's': 'С', 'sʲ': 'С',              # С \
    't': 'Т', 'tʲ': 'Т',              # Т \
    'u': 'У',                         # У \
    'f': 'Ф', 'fʲ': 'Ф',              # Ф \
    'x': 'Х', 'xʲ': 'Х',              # Х \
    'ts': 'Ц',                        # Ц \
    'tɕ': 'Ч',                        # Ч \
    'ʂ': 'Ш',                         # Ш \
    'ɕɕ': 'Щ',                        # Щ \
    '': '',                           # Ъ \
    'ɨ': 'Ы',                         # Ы \
    'ʲ': 'Ь',                         # Ь \
    'e': 'Э',                         # Э \
    'ju': 'Ю', 'ʲu': 'Ю',             # Ю \
    'ja': 'Я', 'ʲa': 'Я'              # Я
}

def map(text, appearance_or_sound='sound'):
    
    if appearance_or_sound == 'appearance':
        text = text.upper()
        appearance_list = list(appearance)
        for i, key in enumerate(appearance):
            text = re.sub(appearance_list[i], appearance[appearance_list[i]], text)
    else:
        text = ipa.convert(text)
        print(text)
        sound_list = list(sounds)
        for i, key in enumerate(sounds):
            text = re.sub(sound_list[i], sounds[sound_list[i]], text)

    return text


if __name__ == "__main__":
    text = input("English text to convert:\n")
    text = map(text, 'appearance')
    print(text)
