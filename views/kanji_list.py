
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

    # Título de la ventana
    title: ft.Container = SKanjiList.title()

    # Columna de la tabla de kanjis
    kanji_list: ft.Container = SKanjiList.kanji_list()

    window: ft.Container = ft.Container(
        expand = True,
        # Se compone de:
        # - Barra de navegación
        # - Columna de la tabla de kanjis
        content = ft.Column(
            expand = True,
            spacing = 15,
            controls = [
                # Barra de navegación
                ft.Row(
                    controls = [
                        nav_bar
                    ]
                ),
                # Título de la ventana
                ft.Row(
                    controls = [
                        title
                    ]
                ),
                # Columna de la tabla de kanjis
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        kanji_list
                    ]
                )
            ]
        )
    )

    return window