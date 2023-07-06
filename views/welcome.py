
import flet as ft

from styles.s_welcome import SWelcome


def Welcome(page: ft.Page) -> ft.Column:
    """
    Ventana de bienvenida a la aplicación

    Se muestra el nombre de la aplicación, un mensaje de bienvenida
    y los botones de las ventanas a las que se puede dirigir el usuario

    Utiliza los controles declarados en la clase :class:`SWelcome` del archivo :file:`s_welcome.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """

    # Nombre de la aplicación
    app_name: ft.Text = SWelcome.app_name()
    # Mensaje de bienvenida
    subtitle: ft.Text = SWelcome.subtitle()
    # Fila de botones de redireccionamiento de ventana
    button_row: ft.Row = SWelcome.button_row(page)

    # Propiedades de la ventana de bienvenida
    window: ft.Column = ft.Column(
        spacing = 25,
        # Se compone de:
        # - Control de texto con el nombre la aplicación
        # - Control de texto con mensaje de bienvenida
        # - Tres botones que redireccionan a ventanas distintas
        controls = [
            # Espacio en blanco de 150px de altura
            ft.Row(
                controls = [
                    ft.Container(
                        expand = True,
                        height = 100,
                    )
                ]
            ),
            # Nombre de la aplicación
            ft.Row(
                controls = [
                    app_name
                ]
            ),
            # Mensaje de bienvenida
            ft.Row(
                controls = [
                    subtitle
                ]
            ),
            # Fila de botones de redireccionamiento de ventana
            ft.Row(
                controls = [
                    button_row
                ]
            )
        ]
    )

    return window