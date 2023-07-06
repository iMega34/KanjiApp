
import flet as ft

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

# Estilos usados por los controles que componen la ventana
styles: dict = {
    "buttons" : {
        "font" : "Exo 2",
        "size" : 40,
        "height" : 75,
        "width" : 325,
        "color" : "#E4D6A0",
        "text_color" : "#032E2C"
    }
}


class SLearnKanji:
    """
    Propiedades de los controles utilizados por la función :function:`LearnKanji`
    del archivo :file:`learn_kanji.py` para la creación de la ventana de aprendizaje
    de kanjis

    Se apoya de las clases :class:`Card`, del archivo :file:`card.py`, y :class:`Word`,
    del archivo :file:`word.py`, para la creación de los controles utilizados en la ventana
    """

    _counter: int = 0

    def kanji_info() -> ft.Column:
        """
        Información del kanji que se mostrará en pantalla

        Regresa un objeto de la clase :class:`ft.Column`
        """

        # Creación del objeto Kanji que se pasará como parámetro al método build_card()
        kanji: Kanji = kanjis[SLearnKanji._counter]

        kanji_content: ft.Column = ft.Column(
            controls = [
                # Tarjeta del kanji
                Card().build_card(kanji)
            ]
        )

        if SLearnKanji._counter < (len(kanjis) - 1):
            SLearnKanji._counter += 1
        else:
            SLearnKanji._counter = 0

        return kanji_content


    def new_kanji_button() -> ft.ElevatedButton:
        """
        Botón para generar una nueva tarjeta con un kanji aleatorio

        Regresa un objeto de la clase :class:`ft.ElevatedButton`
        """

        button: ft.ElevatedButton = ft.ElevatedButton(
            height = styles["buttons"]["height"],
            width = styles["buttons"]["width"],
            bgcolor = styles["buttons"]["color"],
            content = ft.Text(
                "Siguiente",
                font_family = styles["buttons"]["font"],
                size = styles["buttons"]["size"],
                color = styles["buttons"]["text_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return button
