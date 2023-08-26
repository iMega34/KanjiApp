
import flet as ft

from styles.s_kanji_list import SKanjiList
from other.nav_bar import NavBar


def KanjiList(page: ft.Page) -> ft.Container:
    """
    Ventana de lista de kanjis

    Se muestra una tabla con los kanjis disponibles en el programa, cada uno con su significado

    Utiliza los controles declarados en la clase :class:`SKanjiList` del archivo :file:`s_kanji_list.py`

    Regresa un objeto de la clase :class:`ft.Container`
    """

    # Propiedades de la ventana de lista de kanjis
    page.padding = 35

    # Barra de navegación
    nav_bar: ft.Container = NavBar.nav_bar(page)

    window: ft.Container = ft.Container(
        border = ft.border.all(1, "#FF0000"),
        expand = True,
        # Se compone de:
        # - Barra de navegación
        # - Columna de la tabla de kanjis
        content = ft.Column(
            controls = [
                # Barra de navegación
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        nav_bar
                    ]
                ),
                # Columna de la tabla de kanjis
                ft.Row(
                    expand = True,
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        ft.Container(
                            expand = True,
                            border = ft.border.all(1, "#00FF00"),
                        )
                    ]
                )
            ]
        )
    )

    return window