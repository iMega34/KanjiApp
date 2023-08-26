
import flet as ft

from views.welcome import Welcome
from views.learn_kanji import LearnKanji
from views.vocabulary import Vocabulary
from views.kanji_list import KanjiList


class Router:
    """
    Contiene la declaración de las propiedades del objeto
    :object:`Router` y sus funcionalidades en el programa
    """

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        # Rutas que componen el programa
        self.routes = {
            "/" : Welcome(page),                # Ventana de bienvenida
            "/kanji_list" : KanjiList(page),    # Ventana de lista de kanjis
            "/learn_kanji" : LearnKanji(page),  # Ventana de aprendizaje
            "/vocabulary" : Vocabulary(page)    # Ventana de vocabulario
        }
        # Ventana y ruta predeterminadas del router
        self.window = ft.Container(
            content = self.routes['/'],
            expand = True
        )

    def route_change(self, route) -> None:
        """
        Lleva el manejo de las rutas a las que accede el router
        """

        self.window.content = self.routes[route.route]
        self.window.update()
