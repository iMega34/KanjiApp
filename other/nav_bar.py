
import flet as ft


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "color" : "#032E2C"
    },
    "title" : {
        "font" : "Exo 2",
        "size" : 35
    },
    "buttons" : {
        "width" : 60,
        "height" : 60,
        "border_radius" : 50,
        "color" : "#DBD1A7",
        "bgcolor" : "#D9D9D9",
        "home_color" : "#4AB8FC",
        "exit_color" : "#FF0000",
        "icon_size" : 40
    },
    "bar" : {
        "height" : 75
    }
}


class NavBar:
    """
    Contiene las propiedades de los controles utilizados para la creación de la barra de navegación
    usada en las ventanas de la aplicación
    """

    def __init__(self) -> None:
        self._nav_bar = ft.Container()


    def _home_button_on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite al botón de regreso al menú principal elevarse cuando el cursor pasa sobre él
        """

        if _.data == "true":
            for __ in range(20):
                self._home_button.elevation += 1
                self._home_button.update()

        else:
            for __ in range(20):
                self._home_button.elevation -= 1
                self._home_button.update()


    def _home_button_on_click(self, page: ft.Page, _: ft.ControlEvent) -> None:
        """
        Permite regresar al menú principal al dar clic sobre el botón y regresa el botón a su estado
        original
        """

        self._home_button.elevation = 0

        page.go('/')


    def _exit_button_on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite al botón de salida de la aplicación elevarse cuando el cursor pasa sobre él
        """

        if _.data == "true":
            for __ in range(20):
                self._exit_button.elevation += 1
                self._exit_button.update()

        else:
            for __ in range(20):
                self._exit_button.elevation -= 1
                self._exit_button.update()


    def nav_bar(self, page: ft.Page) -> ft.Container:
        """
        Barra de navegación que se utiliza en las ventanas de la aplicación

        Regresa un objeto de la clase :class:`ft.Container`
        """

        self._home_button: ft.Card = ft.Card(
            elevation = 0,
            color = styles['buttons']['color'],
            content = ft.Container(
                width = styles['buttons']['width'],
                height = styles['buttons']['height'],
                alignment = ft.alignment.center,
                content = ft.Icon(
                    name = ft.icons.HOUSE,
                    color = styles['buttons']['home_color'],
                    size = styles['buttons']['icon_size']
                ),
                on_hover = lambda _: self._home_button_on_hover(_),
                on_click = lambda _: self._home_button_on_click(page, _)
            )
        )

        self._exit_button: ft.Card = ft.Card(
            elevation = 0,
            color = styles['buttons']['color'],
            content = ft.Container(
                width = styles['buttons']['width'],
                height = styles['buttons']['height'],
                alignment = ft.alignment.center,
                content = ft.Icon(
                    name = ft.icons.CANCEL,
                    color = styles['buttons']['exit_color'],
                    size = styles['buttons']['icon_size']
                ),
                on_hover = lambda _: self._exit_button_on_hover(_),
                on_click = lambda _: page.window_destroy()
            )
        )

        self._nav_bar: ft.Container = ft.Container(
            expand = True,
            height = styles['bar']['height'],
            content = ft.Row(
                controls = [
                    # Nombre de la aplicación en la barra de navegación
                    ft.Container(
                        expand = True,
                        height = styles['bar']['height'],
                        alignment = ft.alignment.center_left,
                        offset = ft.Offset(0.025, 0),
                        content = ft.Text(
                            "KanjiApp",
                            font_family = styles['title']['font'],
                            size = styles['title']['size'],
                            color = styles['text']['color'],
                        )
                    ),
                    # Botón de regreso al menú principal
                    self._home_button,
                    # Botón para salir de la aplicación
                    self._exit_button
                ]
            )
        )

        return self._nav_bar