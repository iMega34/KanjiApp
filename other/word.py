
import flet as ft

from other.audio_engine import AudioEngine


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "color" : "#032E2C"
    },
    "word_card" : {
        "font" : "Sawarabi Mincho",
        "size" : 30,
        "height" : 75,
        "width" : 520,
        "padding" : 10,
        "color" : "#AED8E5",
    }
}

# Motor de audio para la pronunciación de las palabras
audio: AudioEngine = AudioEngine("JA-JP_HARUKA_11.0")


class Word:
    """
    Contiene los métodos para la creación de una tarjeta de una palabra asociada a un kanji

    Requiere de la creación de un objeto de la clase :class:`Kanji` para poder construir un objeto de
    esta clase
    """

    def __init__(self) -> None:
        self._word = ft.Container()


    def _on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta elevarse al pasar el cursor sobre ella
        """

        if _.data == "true":
            for __ in range(20):
                self._word.elevation += 1
                self._word.update()

        else:
            for __ in range(20):
                self._word.elevation -= 1
                self._word.update()


    def build_word(self, word_kanji: str, meaning: str) -> ft.Card:
        """
        Construye una tarjeta de una palabra a partir de un objeto de la clase :class:`Kanji`.
        Permite leer la palabra en japonés en voz alta.

        Regresa un objeto de la clase :class:`ft.Card`
        """

        # Contenido de la tarjeta de la palabra
        self._content: ft.Container = ft.Container(
            border_radius = ft.border_radius.all(10),
            height = styles["word_card"]["height"],
            width = styles["word_card"]["width"],
            bgcolor = styles["word_card"]["color"],
            padding = styles["word_card"]["padding"],
            # Controles de la tarjeta
            content = ft.Row(
                scroll = True,
                auto_scroll = True,
                on_scroll_interval = 0.1,
                controls = [
                    # Palabra en japonés y su traducción
                    ft.Container(
                        alignment = ft.alignment.center,
                        content = ft.Text(
                            f"{word_kanji} - {meaning}",
                            font_family = styles["word_card"]["font"],
                            size = styles["word_card"]["size"],
                            color = styles["text"]["color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER,
                            selectable = True,
                            no_wrap = True,
                        )
                    )
                ]
            ),
            on_click = lambda _: audio.read_text(word_kanji),
            on_hover = lambda _: self._on_hover(_),
        )

        # Tarjeta de la palabra
        self._word: ft.Card = ft.Card(
            elevation = 0,
            content = self._content
        )

        return self._word