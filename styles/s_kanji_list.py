
import flet as ft


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "color" : "#032E2C"
    },
    "title" : {
        "font" : "Exo 2",
        "size" : 50
    }
}


class SKanjiList:
    """
    Propiedades de los controles utilizados por la función :function:`KanjiList` del archivo
    :file:`kanji_list.py` para la creación de la ventana de lista de kanjis

    Se apoya de la clase :class:`Kanji`, del archivo :file:`kanji.py`, para la creación de las tarjetas
    de kanjis
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