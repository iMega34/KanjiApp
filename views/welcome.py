
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
    app_name: ft.Container = SWelcome.app_name()
    # Botón para salir de la aplicación
    exit_button: ft.Container = SWelcome().exit_button(page)
    # Mensaje de bienvenida
    subtitle: ft.Container = SWelcome.subtitle()
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
            # Botón para salir de la aplicación
            ft.Row(
                alignment = ft.MainAxisAlignment.END,
                height = 75,
                controls = [
                    exit_button
                ]
            ),
            ft.Container(
                expand = True,
                content = ft.Column(
                    offset = ft.Offset(0, -0.025),
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
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
            )
        ]
    )

    return window