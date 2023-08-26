
import flet as ft

from other.kanji import Kanji
from other.audio_engine import AudioEngine


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "font" : "Exo 2",
        "size" : 50,
        "color" : "#032E2C"
    },
    "kanji" : {
        "font" : "Noto Serif JP",
        "size" : 250,
        "color" : "#000000",
        "height" : 450,
        "width" : 480,
    },
    "on_kun" : {
        "font" : "Sawarabi Mincho",
        "size" : 30,
        "spacing" : 15,
    },
    "vocab_title" : {
        "size" : 60
    },
    "vocab_word" : {
        "font" : "Sawarabi Mincho",
        "size" : 50
    },
    "buttons" : {
        "size" : 35,
        "height" : 75,
        "width" : 325,
        "color" : "#E4D6A0"
    },
    "card" : {
        "height" : 650,
        "width" : 530,
        "padding" : 25,
        "color" : "#D2E5EB",
        "sec_color" : "#B4E3EC",
        "shadow_color" : "#A6A6A6"
    },
    "simple_card" : {
        "height" : 275,
        "width" : 275,
        "kanji_size" : 150,
        "meaning_size" : 35,
        "kanji_color" : "#000000",
        "bgcolor_light" : "#D2E5EB",
        "sec_bgcolor_light" : "#C5E2E7",
        "bgcolor_dark" : "#AED8E5",
        "sec_bgcolor_dark" : "#C6E2EA",
    }
}

# Motor de audio para la pronunciación del onyomi y kunyomi
audio: AudioEngine = AudioEngine("JA-JP_HARUKA_11.0")


class Card:
    """
    Contiene los métodos para la creación de la tarjeta del kanji

    Requiere de la creación de un objeto de la clase :class:`Kanji` para poder construir un objeto de
    esta clase
    """

    def __init__(self) -> None:
        self._card = ft.Container()


    def _on_hover(_: ft.HoverEvent) -> None:
        """
        Permite al cuadro de lecturas cambiar de color al pasar el cursor sobre ella
        """

        _.control.bgcolor = styles["card"]["sec_color"] if _.data == "true" else styles["card"]["color"]
        _.control.update()


    def _light_card_on_hover(_: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta simple cambiar de color al pasar el cursor sobre ella
        """

        _.control.bgcolor = styles["simple_card"]["sec_bgcolor_light"] if _.data == "true" else styles["simple_card"]["bgcolor_light"]

        _.control.update()


    def _dark_card_on_hover(_: ft.HoverEvent) -> None:
        """
        Permite a la tarjeta simple cambiar de color al pasar el cursor sobre ella
        """

        _.control.bgcolor = styles["simple_card"]["sec_bgcolor_dark"] if _.data == "true" else styles["simple_card"]["bgcolor_dark"]

        _.control.update()


    def build_card(self, kanji: Kanji) -> ft.Container:
        """
        Construye la tarjeta del kanji a partir de un objeto de la clase :class:`Kanji`

        Recibe un objeto de la clase :class:`Kanji` como parámetro

        Regresa un objeto de la clase :class:`ft.Container`
        """

        self._card: ft.Container = ft.Container(
            border_radius = ft.border_radius.all(40),
            height = styles["card"]["height"],
            width = styles["card"]["width"],
            bgcolor = styles["card"]["color"],
            padding = styles["card"]["padding"],
            shadow = ft.BoxShadow(
                color = styles["card"]["shadow_color"],
                offset = ft.Offset(0, 12)
            ),
            # Contenido de la tarjeta del kanji
            content = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    # Kanji y significado del kanji
                    ft.Row(
                        controls = [
                            ft.Container(
                                height = styles["kanji"]["height"],
                                width = styles["kanji"]["width"],
                                offset = ft.Offset(0, -0.075),
                                alignment = ft.alignment.top_center,
                                content = ft.Column(
                                    controls = [
                                        # Significado del kanji
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            offset = ft.Offset(0, 0.75),
                                            content = Card._get_meaning(kanji)
                                        ),
                                        # Kanji
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            content = Card._get_kanji(kanji)
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                    # On'yomi y kun'yomi
                    ft.Row(
                        offset = ft.Offset(0, -0.4),
                        controls = [
                            # Columna de on'yomi
                            ft.Container(
                                expand = True,
                                height = 150,
                                border_radius = ft.border_radius.all(20),
                                content = ft.Column(
                                    spacing = styles["on_kun"]["spacing"],
                                    controls = [
                                        # On'yomi
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            content = ft.Text(
                                                "On'yomi",
                                                font_family = styles["text"]["font"],
                                                size = styles["on_kun"]["size"],
                                                color = styles["text"]["color"],
                                                weight = ft.FontWeight.W_300,
                                                text_align = ft.TextAlign.CENTER
                                            )
                                        ),
                                        # Lecturas
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            content = Card._build_onyomi_list(kanji)
                                        )
                                    ]
                                ),
                                on_click = lambda _: audio.read(kanji.onyomi),
                                on_hover = Card._on_hover
                            ),
                            # Columna de kun'yomi
                            ft.Container(
                                expand = True,
                                height = 150,
                                border_radius = ft.border_radius.all(20),
                                content = ft.Column(
                                    spacing = styles["on_kun"]["spacing"],
                                    controls = [
                                        # Kun'yomi
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            content = ft.Text(
                                                "Kun'yomi",
                                                font_family = styles["text"]["font"],
                                                size = styles["on_kun"]["size"],
                                                color = styles["text"]["color"],
                                                weight = ft.FontWeight.W_300,
                                                text_align = ft.TextAlign.CENTER
                                            )
                                        ),
                                        # Lecturas
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            content = Card._build_kunyomi_list(kanji)
                                        )
                                    ]
                                ),
                                on_click = lambda _: audio.read(kanji.kunyomi),
                                on_hover = Card._on_hover
                            )
                        ]
                    )
                ]
            )
        )

        return self._card


    def build_simple_card(self, kanji: Kanji) -> ft.Container:
        """
        Construye la tarjeta del kanji a partir de un objeto de la clase :class:`Kanji`

        Versión simplificada de la tarjeta del kanji, unicaménte contiene el kanji y su significado

        Recibe un objeto de la clase :class:`Kanji` como parámetro

        Regresa un objeto de la clase :class:`ft.Container`
        """

        self._card: ft.Container = ft.Container(
            height = styles["simple_card"]["height"],
            width = styles["simple_card"]["width"],
            bgcolor = styles["simple_card"]["bgcolor_light"] if kanji.id % 2 == 0 else styles["simple_card"]["bgcolor_dark"],
            # Contenido de la tarjeta del kanji
            content = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    # Kanji y significado del kanji
                    ft.Row(
                        controls = [
                            ft.Container(
                                height = styles["simple_card"]["height"],
                                width = styles["simple_card"]["width"],
                                offset = ft.Offset(0, -0.04),
                                alignment = ft.alignment.top_center,
                                content = ft.Column(
                                    controls = [
                                        # Significado del kanji
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            offset = ft.Offset(0, 0.75),
                                            content = Card._get_simple_meaning(kanji)
                                        ),
                                        # Kanji
                                        ft.Container(
                                            alignment = ft.alignment.center,
                                            content = Card._get_simple_kanji(kanji)
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            ),
            on_hover = Card._light_card_on_hover if kanji.id % 2 == 0 else Card._dark_card_on_hover
        )

        return self._card


    def _get_kanji(kanji: Kanji) -> ft.Text:
        """
        Obtiene el kanji del objeto de la clase :class:`Kanji`
        y lo regresa como un objeto de la clase :class:`ft.Text`
        """

        kanji: ft.Text = ft.Text(
            kanji.kanji,
            font_family = styles["kanji"]["font"],
            size = styles["kanji"]["size"],
            color = styles["kanji"]["color"],
            text_align = ft.TextAlign.CENTER,
            selectable = True
        )

        return kanji


    def _get_simple_kanji(kanji: Kanji) -> ft.Text:
        """
        Obtiene el kanji del objeto de la clase :class:`Kanji`
        y lo regresa como un objeto de la clase :class:`ft.Text`

        Versión simplificada del kanji, formato más pequeño
        """

        kanji: ft.Text = ft.Text(
            kanji.kanji,
            font_family = styles["kanji"]["font"],
            size = styles["simple_card"]["kanji_size"],
            color = styles["kanji"]["color"],
            text_align = ft.TextAlign.CENTER,
            selectable = True
        )

        return kanji


    def _get_meaning(kanji: Kanji) -> ft.Text:
        """
        Obtiene el significado del kanji del objeto de la clase :class:`Kanji`
        y lo regresa como un objeto de la clase :class:`ft.Text`
        """

        meaning: ft.Text = ft.Text(
            kanji.meaning,
            font_family = styles["text"]["font"],
            size = styles["text"]["size"],
            color = styles["text"]["color"],
            weight = ft.FontWeight.W_300,
            text_align = ft.TextAlign.CENTER
        )

        return meaning


    def _get_simple_meaning(kanji: Kanji) -> ft.Text:
        """
        Obtiene el significado del kanji del objeto de la clase :class:`Kanji`
        y lo regresa como un objeto de la clase :class:`ft.Text`

        Versión simplificada del significado, formato más pequeño
        """

        meaning: ft.Text = ft.Text(
            kanji.meaning,
            font_family = styles["text"]["font"],
            size = styles["simple_card"]["meaning_size"],
            color = styles["text"]["color"],
            weight = ft.FontWeight.W_300,
            text_align = ft.TextAlign.CENTER
        )

        return meaning


    def _build_onyomi_list(kanji: Kanji) -> ft.Text:
        """
        Obtiene la lista de lecturas on'yomi del objeto de la clase :class:`Kanji`
        y lo regresa como un objeto de la clase :class:`ft.Text`
        """

        onyomi_list: ft.Text = ft.Text(
            "",
            font_family = styles["on_kun"]["font"],
            size = styles["on_kun"]["size"],
            color = styles["text"]["color"],
            text_align = ft.TextAlign.CENTER,
        )

        counter: int = 1

        # Previene que se agregue una coma al final de la lista cuando se llega al último elemento
        for reading in kanji.onyomi:
            if counter != len(kanji.onyomi):
                onyomi_list.value += f"{reading}, "
                counter += 1
            else:
                onyomi_list.value += f"{reading}"
        
        return onyomi_list


    def _build_kunyomi_list(kanji: Kanji) -> ft.Text:
        """
        Obtiene la lista de lecturas kun'yomi del objeto de la clase :class:`Kanji`
        y lo regresa como un objeto de la clase :class:`ft.Text`
        """

        kunyomi_list: ft.Text = ft.Text(
            "",
            font_family = styles["on_kun"]["font"],
            size = styles["on_kun"]["size"],
            color = styles["text"]["color"],
            text_align = ft.TextAlign.CENTER,
        )

        counter: int = 1

        # Previene que se agregue una coma al final de la lista cuando se llega al último elemento
        for reading in kanji.kunyomi:
            if counter != len(kanji.kunyomi):
                kunyomi_list.value += f"{reading}, "
                counter += 1
            else:
                kunyomi_list.value += f"{reading}"
        
        return kunyomi_list
