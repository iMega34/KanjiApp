
import flet as ft
from random import randint

from other.card import Card
from other.kanji import Kanji
from other.kanji_table import KanjiTable


# Lista de kanjis
kanji_table: KanjiTable = KanjiTable().build_table("kanji.xlsx")
kanjis: list[Kanji] = []

for index, row in kanji_table.iterrows():
    kanji: Kanji = Kanji()
    kanji.build_kanji(index, row["Kanji"], row["Meaning"], row["On'yomi"], row["Kun'yomi"])
    kanjis.append(kanji)


class SLearnKanji:
    """
    Propiedades de los controles utilizados por la función :function:`LearnKanji`
    del archivo :file:`learn_kanji.py` para la creación de la ventana de aprendizaje
    de kanjis

    Se apoya de las clases :class:`Card`, del archivo :file:`card.py`, y :class:`Word`,
    del archivo :file:`word.py`, para la creación de los controles utilizados en la ventana
    """


    def kanji_info() -> ft.Column:
        """
        Información del kanji que se mostrará en pantalla

        Regresa un objeto de la clase :class:`ft.Column`
        """

        # Creación del objeto Kanji que se pasará como parámetro al método build_card()
        kanji: Kanji = kanjis[randint(0, len(kanjis) - 1)]

        kanji_content: ft.Column = ft.Column(
            controls = [
                # Tarjeta del kanji
                Card().build_card(kanji)
            ]
        )

        return kanji_content
