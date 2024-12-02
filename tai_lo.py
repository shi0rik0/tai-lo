from typing import Tuple


def add_tone_letter(letter: str, tone: int) -> str:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u', 'm', 'n']:
        raise ValueError(f'Letter {letter} cannot bear a tone')
    if not 1 <= tone <= 9:
        raise ValueError('Tone must be between 1 and 9')
    if tone in [1, 4]:
        return letter
    single = {
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
            5: '\u0148',
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
            5: '\u0147',
        },
    }
    if letter in single:
        if tone in single[letter]:
            return single[letter][tone]
    combining_marks = {
        2: '\u0301',
        3: '\u0300',
        5: '\u0302',
        6: '\u030c',
        7: '\u0304',
        8: '\u030d',
        9: '\u030b',
    }
    return letter + combining_marks[tone]


def add_tone_syllable(syllable: str, tone: int) -> str:
    if not 1 <= tone <= 9:
        raise ValueError("Tone must be between 1 and 9")
    if syllable == 'm':
        pass


def parse_syllable(syllable: str) -> Tuple[str, int]:
    return syllable[:-1], int(syllable[-1])


single = {
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
        5: '\u0148',
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
        5: '\u0147',
    },
}
print(single)
