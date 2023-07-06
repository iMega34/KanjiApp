
import flet as ft

from styles.s_learn_kanji import SLearnKanji


def LearnKanji(page: ft.Page) -> ft.Container:
    """
    Ventana de aprendizaje de kanjis

    Se muestra una columna con el kanji a aprender, su significado y sus lecturas en on'yomi y kun'yomi,
    seguido de otra columna con el vocabulario relacionado al kanji mostrado en pantalla y un botón para
    generar una nueva tarjeta con un kanji aleatorio

    Utiliza los controles declarados en la clase :class:`SLearnKanji` del archivo :file:`s_learn_kanji.py`

    Regresa un objeto de la clase :class:`ft.Container`
    """

    # Permite la generación de un nuevo kanji para mostrar en pantalla
    def new_kanji(func) -> None:
        kanji_card.controls[0] = SLearnKanji.kanji_info()
        page.update()

    # Propiedades de la ventana de aprendizaje de kanjis
    page.padding = 100

    # Primer kanji que se mostrará en pantalla
    kanji_card: ft.Column = SLearnKanji.kanji_info()
    # Botón para generar un nuevo kanji
    new_kanji_button: ft.ElevatedButton = SLearnKanji.new_kanji_button()
    new_kanji_button.on_click = new_kanji

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
                kanji_card,
                new_kanji_button
            ]
        )
    )

    return window
