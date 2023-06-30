
import flet as ft

from styles.s_welcome import SWelcome


def Welcome(page: ft.Page) -> ft.Column:
    """
    Ventana de bienvenida a la aplicación

    Se muestra el nombre de la aplicación, un mensaje de bienvenida
    y los botones de las ventanas a las que se puede dirigir el usuario

    Utiliza los controles declarados en la clase :class:`SWelcome` del
    archivo :file:`s_welcome.py`

    Regresa un objeto de la clase :class:`ft.Column`
    """

    # Propiedades de la ventana de bienvenida
    window: ft.Column = ft.Column(
        spacing = 25,
        # Se compone de:
        # - Control de texto con el nombre la aplicación
        # - Control de texto con mensaje de bienvenida
        # - Tres botones que redireccionan a ventanas distintas 
        controls = [
            # Espacio en blanco de 275px de altura
            ft.Row(
                controls = [
                    ft.Container(
                        expand = True,
                        height = 235,
                    )
                ]
            ),
            # Nombre de la aplicación
            ft.Row(
                controls = [
                    SWelcome.app_name()
                ]
            ),
            # Mensaje de bienvenida
            ft.Row(
                controls = [
                    SWelcome.subtitle()
                ]
            ),
            # Fila de botones de redireccionamiento de ventana
            ft.Row(
                controls = [
                    SWelcome.button_row()
                ]
            )
        ]
    )

    return window