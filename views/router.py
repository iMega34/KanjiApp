
import flet as ft

from views.welcome import Welcome


class Router:

    def __init__(self, page) -> None:
        self.page = page
        self.ft = ft
        self.routes = {
            "/" : Welcome(page)
            # "/kanji_list" : KanjiList(page),
            # "/learn_kanji" : LearnKanji(page),
            # "/vocabulary" : Vocabulary(page)
        }
        self.window = ft.Container(
            content = self.routes['/'],
            border = ft.border.all(2, "#FD0000"),
            expand = True
        )

    def route_change(self, route) -> None:
        self.window.content = self.routes[route.route]
        self.window.update()
