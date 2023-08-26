
import flet as ft

from styles.s_learn_kanji import SLearnKanji, kanjis
from other.nav_bar import NavBar


def LearnKanji(page: ft.Page) -> ft.Container:
    """
    Ventana de aprendizaje de kanjis

    Se muestra una columna con el kanji a aprender, su significado y sus lecturas en on'yomi y kun'yomi,
    seguido de otra columna con el vocabulario relacionado al kanji mostrado en pantalla y dos botones para
    navegar entre las tarjetas de los kanjis en la lista.

    Utiliza los controles declarados en la clase :class:`SLearnKanji` del archivo :file:`s_learn_kanji.py`

    Regresa un objeto de la clase :class:`ft.Container`
    """

    def next_kanji(func):
        """
        Muestra el siguiente kanji en la lista de kanjis

        Se verifica que el contador no exceda el número de kanjis en la lista
        permitiendo que si se llega al último kanji, se regrese al primero
        """

        if SLearnKanji._counter < len(kanjis) - 1:
            SLearnKanji._counter += 1
        else:
            SLearnKanji._counter = 0

        kanji_card.content = SLearnKanji.kanji_card()
        kanji_vocab.content = SLearnKanji.kanji_vocab()

        page.update()


    def prev_kanji(func):
        """
        Muestra el kanji anterior en la lista de kanjis

        Se verifica que el contador no sea menor a 0, permitiendo que si se llega
        al primer kanji, se avance al último
        """

        if SLearnKanji._counter > 0:
            SLearnKanji._counter -= 1
        else:
            SLearnKanji._counter = len(kanjis) - 1

        kanji_card.content = SLearnKanji.kanji_card()
        kanji_vocab.content = SLearnKanji.kanji_vocab()

        page.update()


    # Propiedades de la ventana de aprendizaje de kanjis
    page.padding = 35

    # Barra de navegación
    nav_bar: ft.Container = NavBar.nav_bar(page)

    # Título de la columna de vocabulario
    vocab_title: ft.Container = SLearnKanji.vocab_title()
    # Divisor entre el título de la columna y la lista de vocabulario
    vocab_divider: ft.Container = SLearnKanji.vocab_divider()

    # Primer kanji que se mostrará en pantalla
    kanji_card: ft.Container = SLearnKanji.kanji_card()
    # Columna con el vocabulario relacionado al kanji
    kanji_vocab: ft.Container = SLearnKanji.kanji_vocab()

    # Botón para avanzar a la tarjeta del siguiente kanji
    next_kanji_button: ft.ElevatedButton = SLearnKanji.next_kanji_button()
    next_kanji_button.on_click = next_kanji
    # Botón para regresar a la tarjeta del kanji anterior
    prev_kanji_button: ft.ElevatedButton = SLearnKanji.previous_kanji_button()
    prev_kanji_button.on_click = prev_kanji

    window: ft.Container = ft.Container(
        expand = True,
        # Se compone de:
        # - Barra de navegación
        # - Columna con la tarjeta del kanji a aprender
        # - Columna con el vocabulario relacionado al kanji
        # - Botón para generar un nuevo kanji
        content = ft.Column(
            expand = True,
            spacing = 15,
            controls = [
                # Barra de navegación
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        nav_bar
                    ]
                ),
                # Espacio de la ventana
                ft.Row(
                    expand = True,
                    alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                    controls = [
                        # Columna con la tarjeta del kanji a aprender
                        ft.Column(
                            controls = [
                                kanji_card
                            ]
                        ),
                        # Columna con el vocabulario relacionado al kanji
                        ft.Column(
                            spacing = 15,
                            controls = [
                                # Título de la columna
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    controls = [
                                        vocab_title
                                    ]
                                ),
                                # Divisor entre el título de la columna y la lista de vocabulario
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    controls = [
                                        vocab_divider
                                    ]
                                ),
                                # Lista con el vocabulario relacionado al kanji
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    controls = [
                                        kanji_vocab
                                    ]
                                ),
                                # Botones para avanzar o regresar a la tarjeta de otro kanji en la lista
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    controls = [
                                        ft.Container(
                                            content = ft.Row(
                                                width = 750,
                                                controls = [
                                                    prev_kanji_button,
                                                    next_kanji_button
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )

    return window
