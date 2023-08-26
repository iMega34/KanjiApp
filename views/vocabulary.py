
import flet as ft
from jamdict import Jamdict

from styles.s_vocabulary import SVocabulary
from other.nav_bar import NavBar


def Vocabulary(page: ft.Page) -> ft.Container:
    """
    Ventana de vocabulario

    Se muestra una columna con las primeras 50 palabras que se encuentren en el diccionario JMDict, además
    de una barra de busqueda donde se introduce un kanji para buscar palabras asociadas a él o palabras, y los
    resultados de la búsqueda se mostrarán en la columna

    Utiliza los controles declarados en la clase :class:`SVocabulary` del archivo :file:`s_vocabulary.py`, además de apoyarse
    de la clase :class:`Kanji` del archivo :file:`kanji.py` y de la clase :class:`Jamdict` de la librería
    :library:`jamdict` para la búsqueda de palabras

    Regresa un objeto de la clase :class:`ft.Container`
    """

    def _search_vocab(kanji: str) -> dict[str, list[str]]:
        """
        Busca palabras asociada al kanji que se pasa como parámetro

        Recibe un objeto de la clase :class:`str`

        Regresa un diccionario con las primeras 50 palabras encontradas en el diccionario JMDict
        """

        # Se crea un objeto de la clase Jamdict, pero se utiliza el método lookup_iter para buscar
        # palabras asociadas al kanji que se pasa como parámetro, ya que este método regresa un iterador,
        # lo que permite encontrar las palabras de una manera más rápida y eficiente
        jam = Jamdict()
        result = jam.lookup_iter(f'%{kanji}%', strict_lookup = True)

        # Diccionario que almacenará las palabras encontradas
        vocabulary: dict[str, list[str]] = {
            "word_kana" : [],
            "word_kanji" : [],
            "meaning" : []
        }

        for count, entry in enumerate(result.entries):
            if count < 50:
                vocabulary['word_kana'].append(entry.kana_forms[0])
                vocabulary['word_kanji'].append(entry.kanji_forms[0])
                vocabulary['meaning'].append(entry.senses[0].gloss[0])
            else:
                break

        return vocabulary


    def new_search(func) -> None:
        """
        Procesa la entrada de texto de la barra de búsqueda y actualiza la columna con el vocabulario encontrado
        """

        kanji: str = search_bar.content.controls[0].value
        vocab_results = _search_vocab(kanji)
        vocabulary.controls[:3] = SVocabulary.build_vocab(vocab_results).controls[:3]
        page.update()


    # Propiedades de la ventana de aprendizaje de kanjis
    page.padding = 35

    # Barra de navegación
    nav_bar: ft.Container = NavBar.nav_bar(page)

    vocab_results: dict[str: list[str]] = _search_vocab("月")

    # Título de la ventana
    title: ft.Container = SVocabulary.title()
    # Línea divisora entre el título y el contenido de la ventana
    divider: ft.Container = SVocabulary.divider()
    # Barra de búsqueda de vocabulario
    search_bar: ft.Container = SVocabulary.search_bar()
    search_bar.content.controls[1].on_click = new_search
    # Columna con el vocabulario encontrado
    vocabulary: ft.Row = SVocabulary.build_vocab(vocab_results)

    window: ft.Container = ft.Container(
        expand = True,
        # Se compone de:
        # - Barra de navegación
        # - El título de la ventana
        # - Una barra de búsqueda para ingresar un kanji o una palabra
        # - Un control con dos columnas de vocabulario que suman 50 palabras asociadas a la búsqueda
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
                # Línea divisora entre el título y el contenido de la ventana
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        divider
                    ]
                ),
                # Barra de búsqueda de vocabulario
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        search_bar
                    ]
                ),
                # Columnas con el vocabulario encontrado
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        vocabulary
                    ]
                )
            ]
        )
    )

    return window