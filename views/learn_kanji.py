
import flet as ft

from styles.s_learn_kanji import SLearnKanji


def LearnKanji(page: ft.Page) -> ft.Container:
    """
    Ventana de aprendizaje de kanjis

    Se muestra una columna con el kanji a aprender, su significado y sus lecturas en on'yomi y kun'yomi,
    seguido de otra columna con el vocabulario relacionado al kanji mostrado en pantalla

    Utiliza los controles declarados en la clase :class:`SLearnKanji` del archivo :file:`s_learn_kanji.py`

    Regresa un objeto de la clase :class:`ft.Container`
    """

    # Propiedades de la ventana de aprendizaje de kanjis
    page.padding = 100

    window: ft.Container = ft.Container(
        expand = True,
        border = ft.border.all(1, "#FF0000"),
        # Se compone de:
        # - Columna con la tarjeta del kanji a aprender
        # - Columna con el vocabulario relacionado al kanji
        content = ft.Row(
            expand = True,
            controls = [
                # Tarjeta del kanji
                SLearnKanji.kanji_info()
            ]
        )
    )

    return window
