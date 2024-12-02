from typing import Tuple

# Some tone-marked characters can be represented as a single Unicode character
_single_characters = {
    'a': {
        2: '\u00e1',
        3: '\u00e0',
        5: '\u00e2',
        6: '\u01ce',
        7: '\u0101',
    },
    'e': {
        2: '\u00e9',
        3: '\u00e8',
        5: '\u00ea',
        6: '\u011b',
        7: '\u0113',
    },
    'i': {
        2: '\u00ed',
        3: '\u00ec',
        5: '\u00ee',
        6: '\u01d0',
        7: '\u012b',
    },
    'o': {
        2: '\u00f3',
        3: '\u00f2',
        5: '\u00f4',
        6: '\u01d2',
        7: '\u014d',
        9: '\u0151',
    },
    'u': {
        2: '\u00fa',
        3: '\u00f9',
        5: '\u00fb',
        6: '\u01d4',
        7: '\u016b',
        9: '\u0171',
    },
    'm': {
        2: '\u1e3f',
    },
    'n': {
        2: '\u0144',
        3: '\u01f9',
        6: '\u0148',
    },
    'A': {
        2: '\u00c1',
        3: '\u00c0',
        5: '\u00c2',
        6: '\u01cd',
        7: '\u0100',
    },
    'E': {
        2: '\u00c9',
        3: '\u00c8',
        5: '\u00ca',
        6: '\u011a',
        7: '\u0112',
    },
    'I': {
        2: '\u00cd',
        3: '\u00cc',
        5: '\u00ce',
        6: '\u01cf',
        7: '\u012a',
    },
    'O': {
        2: '\u00d3',
        3: '\u00d2',
        5: '\u00d4',
        6: '\u01d1',
        7: '\u014c',
        9: '\u0150',
    },
    'U': {
        2: '\u00da',
        3: '\u00d9',
        5: '\u00db',
        6: '\u01d3',
        7: '\u016a',
        9: '\u0170',
    },
    'M': {
        2: '\u1e3e',
    },
    'N': {
        2: '\u0143',
        3: '\u01f8',
        6: '\u0147',
    },
}

_single_characters_2 = {
    v2: (k1, k2)
    for k1, v1 in _single_characters.items()
    for k2, v2 in v1.items()
}

# Some tone-marked characters cannot be represented as a single Unicode character
# In this case, we need to combine the base character with a combining mark
_combining_marks = {
    2: '\u0301',
    3: '\u0300',
    5: '\u0302',
    6: '\u030c',
    7: '\u0304',
    8: '\u030d',
    9: '\u030b',
}

_combining_marks_2 = {v: k for k, v in _combining_marks.items()}


def add_tone_character(char: str, tone: int) -> str:
    '''
    Add a tone mark to a character.

    If the tone-marked character can be represented as a single Unicode character, return that character.
    Otherwise, use Unicode combining marks to add the tone.
    '''
    if char.lower() not in ['a', 'e', 'i', 'o', 'u', 'm', 'n']:
        raise ValueError(f'Character {char} cannot bear a tone')
    if not 1 <= tone <= 9:
        raise ValueError('Tone must be between 1 and 9')
    if tone in [1, 4]:
        return char
    if char in _single_characters:
        if tone in _single_characters[char]:
            return _single_characters[char][tone]
    return char + _combining_marks[tone]


def parse_character(char: str) -> Tuple[str, int]:
    '''
    Parse a tone-marked character into its base character and tone number.

    The 1st and 4th tones are both unmarked. Tones of unmarked characters are treated as 1.
    '''
    if char in _single_characters_2:
        return _single_characters_2[char]
    if len(char) == 1:
        return char, 1
    if len(char) == 2 and char[1] in _combining_marks_2:
        return char[0], _combining_marks_2[char[1]]
    raise ValueError(f'Invalid tone-marked character {char}')


def add_tone_syllable(syllable: str, tone: int) -> str:
    '''
    Add a tone mark to a syllable.
    '''
    if not 1 <= tone <= 9:
        raise ValueError('Tone must be between 1 and 9')
    i = _find_tone_index(syllable)
    return syllable[:i] + add_tone_character(syllable[i],
                                             tone) + syllable[i + 1:]


def _find_tone_index(syllable: str) -> int:
    syllable = syllable.lower()
    first_index = -1
    last_index = -1

    for i, char in enumerate(syllable):
        if char in ['a', 'e', 'i', 'o', 'u']:
            if first_index == -1:
                first_index = i
            last_index = i

    if first_index != -1:
        vowels = syllable[first_index:last_index + 1]
        for i in vowels:
            if i not in ['a', 'e', 'i', 'o', 'u']:
                raise ValueError(f'Invalid syllable {syllable}')
        return first_index + _find_tone_index_vowels(vowels)
    else:
        # If there is no vowel, the tone mark goes on either 'm' or 'ng'
        ng_index = syllable.find('ng')
        if ng_index != -1:
            return ng_index
        m_index = syllable.find('m')
        if m_index != -1:
            return m_index
        raise ValueError(f'Invalid syllable {syllable}')


def _find_tone_index_vowels(vowels: str) -> int:
    vowels = vowels.lower()
    if vowels == 'iu':
        return 1
    order = ['a', 'o', 'e', 'i', 'u']
    order = {char: i for i, char in enumerate(order)}
    target = min(vowels, key=lambda x: order[x])
    return vowels.index(target)


def _is_jip_siann(syllable: str) -> bool:
    '''
    Determine if a syllable is ji̍p-siann (入聲).
    '''
    return syllable[-1].lower() in ['p', 't', 'k', 'h']


def parse_syllable(syllable: str) -> Tuple[str, int]:
    '''
    Parse a syllable into its base form and tone number.
    '''
    for i in range(len(syllable)):
        if syllable[i] in _combining_marks_2:
            return syllable[:i] + syllable[i +
                                           1:], _combining_marks_2[syllable[i]]
    syllable = list(syllable)
    for i in range(len(syllable)):
        if syllable[i] in _single_characters_2:
            base, tone = _single_characters_2[syllable[i]]
            syllable[i] = base
            return ''.join(syllable), tone
    return ''.join(syllable), 4 if _is_jip_siann(syllable) else 1
