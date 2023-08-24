
import flet as ft


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "color" : "#032E2C"
    },
    "word_card" : {
        "font" : "Sawarabi Mincho",
        "size" : 30,
        "height" : 75,
        "width" : 500,
        "padding" : 10,
        "color" : "#AED8E5",
        "sec_color" : "#D2E5EB",
    }
}


class Word:
    """
    Contiene los métodos para la creación de una tarjeta de una palabra asociada a un kanji

    Requiere de la creación de un objeto de la clase :class:`Kanji` para poder construir un objeto de
    esta clase
    """

    def __init__(self) -> None:
        self._word = ft.Container()


    def _on_hover(_: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta cambiar de color al pasar el cursor sobre ella
        """

        _.control.bgcolor = styles["word_card"]["sec_color"] if _.data == "true" else styles["word_card"]["color"]
        _.control.update()


    def build_word(self, word_kanji: str, word_kana: str, meaning: str) -> ft.Container:
        """
        Construye una tarjeta de una palabra a partir de un objeto de la clase :class:`Kanji`

        Regresa un objeto de la clase :class:`ft.Container`
        """

        self._word: ft.Container = ft.Container(
            height = styles["word_card"]["height"],
            width = styles["word_card"]["width"],
            border_radius = ft.border_radius.all(10),
            bgcolor = styles["word_card"]["color"],
            padding = styles["word_card"]["padding"],
            content = ft.Row(
                scroll = True,
                auto_scroll = True,
                on_scroll_interval = 0.1,
                controls = [
                    ft.Container(
                        alignment = ft.alignment.center,
                        content = ft.Text(
                            f"{word_kanji} - {meaning}",
                            font_family = styles["word_card"]["font"],
                            size = styles["word_card"]["size"],
                            color = styles["text"]["color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER,
                            no_wrap = True,
                        )
                    )
                ]
            ),
            on_hover = Word._on_hover,
        )

        return self._word