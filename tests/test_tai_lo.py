from tai_lo import *
from pathlib import Path

root_dir = Path(__file__).resolve().parent
while not (root_dir / '.HERE_IS_ROOT').is_file():
    root_dir = root_dir.parent


def test_syllable():
    with open(root_dir / 'tests' / 'syllables.txt', encoding='utf-8') as f:
        syllables = f.read().split('\n')

    if syllables[-1] == '':
        syllables.pop()

    for i in syllables:
        s, tone = parse_syllable(i)
        t = add_tone_syllable(s, tone)
        assert i == t, f'{i} != {t}'
