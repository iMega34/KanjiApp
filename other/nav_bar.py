
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
        "sec_color" : "#E9E1C0",
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

    def _on_hover(_: ft.HoverEvent) -> None:
        """
        Permite a los botones cambiar de color al pasar el cursor sobre ellos
        """

        _.control.bgcolor = styles["buttons"]["sec_color"] if _.data == "true" else styles["buttons"]["color"]
        _.control.update()


    def nav_bar(page: ft.Page) -> ft.Container:

        nav_bar_content: ft.Container = ft.Container(
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
                    ft.Container(
                        width = styles['buttons']['width'],
                        height = styles['buttons']['height'],
                        border_radius = ft.border_radius.all(styles['buttons']['border_radius']),
                        bgcolor = styles['buttons']['color'],
                        alignment = ft.alignment.center,
                        offset = ft.Offset(-0.3, 0),
                        content = ft.Icon(
                            name = ft.icons.HOUSE,
                            color = styles['buttons']['home_color'],
                            size = styles['buttons']['icon_size']
                        ),
                        on_hover = NavBar._on_hover,
                        on_click = lambda _: page.go('/')
                    ),
                    # Botón para salir de la aplicación
                    ft.Container(
                        width = styles['buttons']['width'],
                        height = styles['buttons']['height'],
                        border_radius = ft.border_radius.all(styles['buttons']['border_radius']),
                        bgcolor = styles['buttons']['color'],
                        alignment = ft.alignment.center,
                        offset = ft.Offset(-0.3, 0),
                        content = ft.Icon(
                            name = ft.icons.CANCEL,
                            color = styles['buttons']['exit_color'],
                            size = styles['buttons']['icon_size']
                        ),
                        on_hover = NavBar._on_hover,
                        on_click = lambda _: page.window_destroy()
                    )
                ]
            )
        )

        return nav_bar_content