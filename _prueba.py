
import flet as ft
from jamdict import Jamdict

# result = jam.lookup('水曜%')
kanji = '飲'
jam = Jamdict()
result = jam.lookup_iter(f'%{kanji}%', strict_lookup = True)

vocabulary: dict[str: list[str]] = {
    "word_kana" : [],
    "word_kanji" : [],
    "meaning" : []
}

for count, entry in enumerate(result.entries):
    if count < 50:
        vocabulary['word_kana'].append(entry.kana_forms[0])
        vocabulary['word_kanji'].append(entry.kanji_forms[0])
        vocabulary['meaning'].append(entry.senses[0].gloss[0])
    else:
        break

for kanji, kana, meaning in zip(vocabulary['word_kanji'], vocabulary['word_kana'], vocabulary['meaning']):
    print(kanji, kana, meaning)
