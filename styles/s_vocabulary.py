
import flet as ft

from other.word import Word


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "color" : "#032E2C"
    },
    "title" : {
        "font" : "Exo 2",
        "size" : 50
    },
    "horz_div" : {
        "color" : "#032E2C",
        "height" : 2,
        "width" : 1150
    },
    "vert_div" : {
        "color" : "#032E2C",
        "height" : 450,
        "width" : 2
    },
    "list_view" : {
        "spacing" : 10,
        "padding" : 10,
        "width" : 550,
        "height" : 450
    },
    "search_bar" : {
        "font" : "Sawarabi Mincho",
        "size" : 15,
        "button_height" : 53,
        "button_width" : 53,
        "text_field_width" : 1045,
        "bgcolor" : "#DBD1A7",
        "border_color" : "#A39768",
        "cursor_color" : "#537B79",
    }
}


class SVocabulary:
    """
    Propiedades de los controles utilizados por la función :function:`Vocabulary` del archivo
    :file:`vocabulary.py` para la creación de la ventana de vocabulario

    Se apoya de la clase :class:`Word`, del archivo :file:`word.py`, para la creación de las tarjetas
    de vocabulario
    """

    def title() -> ft.Container:
        """
        Título de la ventana

        Regresa un objeto de la clase :class:`ft.Container`
        """

        title_content: ft.Container = ft.Container(
            expand = True,
            content = ft.Text(
                "Vocabulario",
                font_family = styles["title"]["font"],
                size = styles["title"]["size"],
                color = styles["text"]["color"],
                weight = ft.FontWeight.W_300,
                text_align = ft.TextAlign.CENTER
            )
        )

        return title_content


    def divider() -> ft.Container:
        """
        Divisor entre el título y el resto de la ventana

        Regresa un objeto de la clase :class:`ft.Container`
        """

        divider_content: ft.Container = ft.Container(
            bgcolor = styles["horz_div"]["color"],
            width = styles["horz_div"]["width"],
            height = styles["horz_div"]["height"],
        )

        return divider_content


    def search_bar() -> ft.Container:
        """
        Barra de búsqueda de vocabulario por medio de un kanji o una serie de palabras

        Regresa un objeto de la clase :class:`ft.Container`
        """

        search_bar_content: ft.Container = ft.Container(
            content = ft.Row(
                expand = True,
                controls = [
                    # Cuadro de texto para ingresar la búsqueda
                    ft.TextField(
                        width = styles["search_bar"]["text_field_width"],
                        label = "Busca un kanji o una palabra...",
                        label_style = ft.TextStyle(
                            font_family = styles["search_bar"]["font"],
                            color = styles["text"]["color"],
                            size = styles["search_bar"]["size"]
                        ),
                        text_style = ft.TextStyle(
                            font_family = styles["search_bar"]["font"],
                            color = styles["text"]["color"],
                            size = styles["search_bar"]["size"]
                        ),
                        cursor_color = styles["search_bar"]["cursor_color"],
                        border_radius = ft.border_radius.only(top_left = 10, bottom_left = 10),
                        border_color = styles["search_bar"]["border_color"],
                        bgcolor = styles["search_bar"]["bgcolor"],
                    ),
                    # Botón para realizar la búsqueda
                    ft.Container(
                        width = styles["search_bar"]["button_width"],
                        height = styles["search_bar"]["button_height"],
                        border = ft.border.all(1, styles["search_bar"]["border_color"]),
                        border_radius = ft.border_radius.only(top_right = 10, bottom_right = 10),
                        bgcolor = styles["search_bar"]["bgcolor"],
                        alignment = ft.alignment.center,
                        ink = True,
                        content = ft.Text(
                            "🔎",
                            font_family = styles["search_bar"]["font"],
                            size = styles["search_bar"]["size"],
                            color = styles["text"]["color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER,
                        )
                    )
                ]
            )
        )

        return search_bar_content


    def build_vocab(vocab_dict: dict[str, list[str]]) -> ft.Row:
        """
        Resultados de la búsqueda de vocabulario para el kanji o palabra ingresados a la ventana

        Recibe un diccionario con las listas de palabras en kanji, palabras en kana y significado de las palabras

        Regresa un objeto de la clase :class:`ft.Row`
        """

        column = 1

        # Se crean objetos de la clase ft.ListView para contener las tarjetas de vocabulario:
        # list_view_1 sería la columna izquierda y list_view_2 la columna derecha 
        list_view_1: ft.ListView = ft.ListView(
            spacing = styles["list_view"]["spacing"],
            padding = styles["list_view"]["padding"],
            width = styles["list_view"]["width"],
            height = styles["list_view"]["height"]
        )
        list_view_2: ft.ListView = ft.ListView(
            spacing = styles["list_view"]["spacing"],
            padding = styles["list_view"]["padding"],
            width = styles["list_view"]["width"],
            height = styles["list_view"]["height"]
        )

        # Se agregan tarjetas de vocabulario al objeto de la clase ft.ListView
        for kanji, kana, meaning in zip(vocab_dict['word_kanji'], vocab_dict['word_kana'], vocab_dict['meaning']):
            word: ft.Container = Word().build_word(kanji, kana, meaning)
            if column == 1:
                list_view_1.controls.append(word)
                column = 2
            else:
                list_view_2.controls.append(word)
                column = 1

        vocab_content: ft.Row = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            spacing = 15,
            controls = [
                ft.Container(
                    alignment = ft.alignment.center,
                    content = list_view_1
                ),
                ft.Container(
                    bgcolor = styles["vert_div"]["color"],
                    width = styles["vert_div"]["width"],
                    height = styles["vert_div"]["height"]
                ),
                ft.Container(
                    alignment = ft.alignment.center,
                    content = list_view_2
                )
            ]
        )

        return vocab_content
