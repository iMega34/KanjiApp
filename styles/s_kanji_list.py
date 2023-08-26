
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
    "text" : {
        "color" : "#032E2C"
    },
    "title" : {
        "font" : "Exo 2",
        "size" : 50
    },
    "kanji_list" : {
        "spacing" : 10,
        "width" : 1415,
        "height" : 570
    }
}


class SKanjiList:
    """
    Propiedades de los controles utilizados por la función :function:`KanjiList` del archivo
    :file:`kanji_list.py` para la creación de la ventana de lista de kanjis

    Se apooya de la clases :class:`Card`, del archivo :file:`card.py`, para la creación de los
    controles utilizados en la ventana
    """

    def title() -> ft.Container:
        """
        Título de la ventana

        Regresa un objeto de la clase :class:`ft.Container`
        """

        title_content: ft.Container = ft.Container(
            expand = True,
            content = ft.Text(
                "Lista de kanjis",
                font_family = styles["title"]["font"],
                size = styles["title"]["size"],
                color = styles["text"]["color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return title_content
    

    def kanji_list() -> ft.Container:
        """
        Lista con los kanjis que se mostrarán en la ventana

        Adapatación del metodo :method:`vocab_list` del archivo :file:`s_learn_kanji.py` para la
        creación de las tarjetas de los kanjis disponibles, mostrando únicamente el kanji y
        su significado en un formato más compacto

        Regresa un objeto de la clase :class:`ft.Container`
        """

        _counter: int = 0

        # Se crea un objeto de la clase ft.ListView para contener una las tarjetas de los kanjis disponibles
        list_view: ft.ListView = ft.ListView(
            spacing = styles["kanji_list"]["spacing"],
            width = styles["kanji_list"]["width"],
            height = styles["kanji_list"]["height"]
        )

        # Se crean objetos de la clase ft.Row para contener las tarjetas de los kanjis disponibles en grupos de 3
        for row in range((len(kanjis) // 5) + 1):
            list_row: ft.Row = ft.Row()
            for kanji in range(5):
                try:
                    kanji_card: ft.Card = Card().build_simple_card(kanjis[_counter])
                    list_row.controls.append(kanji_card)
                    _counter += 1
                except IndexError:
                    break
            list_view.controls.append(list_row)

        # Se coloca el objeto list_view, de la clase ft.ListView, en un objeto de la clase ft.Container
        kanji_list_content: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = list_view
        )

        return kanji_list_content