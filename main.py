
import flet as ft

from views.router import Router


def main(page: ft.Page):
    # Propiedades de la ventana
    page.title = "KanjiApp"
    page.bgcolor = "#D9D9D9"
    page.window_full_screen = True

    router: Router = Router(page)

    page.on_route_change = router.route_change

    page.add(router.window)

    page.go('/')


ft.app(target = main)

