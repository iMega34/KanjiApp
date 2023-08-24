
import flet as ft

from styles.s_learn_kanji import SLearnKanji
from other.nav_bar import NavBar

styles: dict = {
    "controls" : {
        "width" : 150,
        "height" : 75,
        "border_radius" : 10,
    },
}


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
    page.padding = 35

    # Barra de navegación
    nav_bar: ft.Container = NavBar.nav_bar(page)

    # Primer kanji que se mostrará en pantalla
    kanji_card: ft.Column = SLearnKanji.kanji_info()
    # Botón para generar un nuevo kanji
    new_kanji_button: ft.ElevatedButton = SLearnKanji.new_kanji_button()
    new_kanji_button.on_click = new_kanji

    window: ft.Container = ft.Container(
        expand = True,
        # Se compone de:
        # - Barra de navegación
        # - Columna con la tarjeta del kanji a aprender
        # - Columna con el vocabulario relacionado al kanji
        # - Botón para generar un nuevo kanji
        content = ft.Column(
            expand = True,
            controls = [
                # Barra de navegación
                ft.Row(
                    controls = [
                        nav_bar
                    ]
                ),
                # Espacio de la ventana
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        # Tarjeta del kanji
                        kanji_card,
                        # Botón para cambio de kanji
                        ft.Column(
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                new_kanji_button
                            ]
                        )
                    ]
                )
            ]
        )
    )

    return window
