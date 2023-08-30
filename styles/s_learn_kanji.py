
import flet as ft
from jamdict import Jamdict

from other.word import Word
from other.card import Card
from other.kanji import Kanji
from other.kanji_table import KanjiTable
from database.database import Database


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
    "vocab_title" : {
        "font" : "Exo 2",
        "width" : 750,
        "size" : 50
    },
    "horz_div" : {
        "color" : "#032E2C",
        "height" : 2,
        "width" : 750
    },
    "buttons" : {
        "font" : "Exo 2",
        "size" : 40,
        "height" : 75,
        "width" : 370,
        "color" : "#E4D6A0",
        "text_color" : "#032E2C"
    },
    "list_view" : {
        "spacing" : 10,
        "padding" : 10,
        "width" : 750,
        "height" : 450
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

    def _search_vocab(kanji: str) -> dict[list[str], list[str]]:
        """
        Busca palabras asociada al kanji que se pasa como parámetro

        Recibe un objeto de la clase :class:`str`

        Regresa un diccionario con las palabras encontradas en el vocabulario de Genki 3rd Edition
        """

        # Se crea un objeto de la clase Jamdict, pero se utiliza el método lookup_iter para buscar
        # palabras asociadas al kanji que se pasa como parámetro, ya que este método regresa un iterador,
        # lo que permite encontrar las palabras de una manera más rápida y eficiente
        # jam = Jamdict()
        # result = jam.lookup_iter(f'%{kanji}%', strict_lookup = True)

        # Se crea un objeto de la clase Database para buscar las palabras asociadas al kanji que se pasa como parámetro
        database = Database()
        vocabulary = database.search_vocab(kanji)

        return vocabulary


    def vocab_title() -> ft.Container:
        """
        Título de la columna con el vocabulario

        Regresa un objeto de la clase :class:`ft.Container`
        """

        vocab_title_content: ft.Container = ft.Container(
            width = styles["vocab_title"]["width"],
            content = ft.Text(
                "Vocabulario",
                font_family = styles["vocab_title"]["font"],
                size = styles["vocab_title"]["size"],
                color = styles["text"]["color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return vocab_title_content


    def vocab_divider() -> ft.Container:
        """
        Divisor entre el título de la columna y la lista de vocabulario

        Regresa un objeto de la clase :class:`ft.Container`
        """

        divider_content: ft.Container = ft.Container(
            bgcolor = styles["horz_div"]["color"],
            width = styles["horz_div"]["width"],
            height = styles["horz_div"]["height"],
        )

        return divider_content


    def kanji_card() -> ft.Container:
        """
        Información del kanji que se mostrará en pantalla

        Regresa un objeto de la clase :class:`ft.Container`
        """

        # Creación del objeto Kanji que se pasará como parámetro al método build_card()
        kanji: Kanji = kanjis[SLearnKanji._counter]

        kanji_card_content: ft.Container = ft.Container(
            content = Card().build_card(kanji),
        )

        return kanji_card_content


    def kanji_vocab() -> ft.Container:
        """
        Lista con el vocabulario relacionado al kanji mostrado en pantalla

        Adaptación de la función :function:`create_vocab` del archivo :file:`s_vocabulary.py`,
        con un tamaño del control reducido y actualización automática de la lista mostrada en pantalla

        Regresa un objeto de la clase :class:`ft.Container`
        """

        kanji: Kanji = kanjis[SLearnKanji._counter].kanji

        vocab_dict: dict[str, list[str]] = SLearnKanji._search_vocab(kanji)

        # Se crea un objeto de la clase ft.ListView para contener las tarjetas de vocabulario
        list_view: ft.ListView = ft.ListView(
            spacing = styles["list_view"]["spacing"],
            padding = styles["list_view"]["padding"],
            width = styles["list_view"]["width"],
            height = styles["list_view"]["height"]
        )

        # Se agregan tarjetas de vocabulario al objeto de la clase ft.ListView
        for kanji, meaning in zip(vocab_dict['kanji'], vocab_dict['meaning']):
            word: ft.Container = Word().build_word(kanji, meaning)
            list_view.controls.append(word)

        # Se coloca el objeto list_view, de la clase ft.ListView, en un objeto de la clase ft.Container
        kanji_vocab_content: ft.Container = ft.Container(
            alignment = ft.alignment.center,
            content = list_view
        )

        return kanji_vocab_content


    def next_kanji_button() -> ft.ElevatedButton:
        """
        Botón para avanzar a la tarjeta del siguiente kanji

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


    def previous_kanji_button() -> ft.ElevatedButton:
        """
        Botón para regresar a la tarjeta del kanji anterior

        Regresa un objeto de la clase :class:`ft.ElevatedButton`
        """

        button: ft.ElevatedButton = ft.ElevatedButton(
            height = styles["buttons"]["height"],
            width = styles["buttons"]["width"],
            bgcolor = styles["buttons"]["color"],
            content = ft.Text(
                "Anterior",
                font_family = styles["buttons"]["font"],
                size = styles["buttons"]["size"],
                color = styles["buttons"]["text_color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return button
