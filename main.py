
import flet as ft

from views.router import Router


def main(page: ft.Page):
    # Propiedades de la ventana
    page.title = "KanjiApp"
    page.bgcolor = "#D9D9D9"
    page.window_title_bar_hidden = True
    page.window_full_screen = True

    # Declaración del router de la clase Router para redireccionar
    # a otras ventanas
    router: Router = Router(page)

    # Asignación de la ruta a la que se va a acceder
    page.on_route_change = router.route_change

    # Se añade la ventana accedida por el router a la ventana actual
    page.add(router.window)

    # Se accede a la ventana de bienvenida
    page.go('/')


ft.app(target = main)
