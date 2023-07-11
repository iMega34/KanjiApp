
import flet as ft


# Estilos usados por los controles que componen la ventana
styles: dict = {
    "text" : {
        "color" : "#032E2C"
    },
    "app_name" : {
        "font" : "Exo 2",
        "size" : 92
    },
    "subtitle" : {
        "font" : "Sawarabi Mincho",
        "size" : 80
    },
    "buttons" : {
        "font" : "Exo 2",
        "size" : 40,
        "height" : 75,
        "width" : 325,
        "row_height" : 200,
        "row_spacing" : 75,
        "color" : "#E4D6A0",
    },
}


class SWelcome:
    """
    Propiedades de los controles utilizados por la función :function:`Welcome`
    del archivo :file:`welcome.py` para la creación de la ventana de bienvenida
    """

    def app_name() -> ft.Container:
        """
        Nombre de la aplicación

        Regresa un objeto de la clase :class:`ft.Container`
        """
        app_name_content: ft.Container = ft.Container(
            expand = True,
            content = ft.Text(
                "KanjiApp",
                font_family = styles["app_name"]["font"],
                size = styles["app_name"]["size"],
                color = styles["text"]["color"],
                text_align = ft.TextAlign.CENTER
            )
        )

        return app_name_content


    def subtitle() -> ft.Container:
        """
        Mensaje de bienvenida

        Regresa un objeto de la clase :class:`ft.Container`
        """
        subtitle_content: ft.Container = ft.Container(
            expand = True,
            content = ft.Text(
                "ようこそ",
                font_family = styles["subtitle"]["font"],
                size = styles["subtitle"]["size"],
                color = styles["text"]["color"],
                text_align = ft.TextAlign.CENTER
            )
        )

        return subtitle_content


    def button_row(page: ft.Page) -> ft.Container:
        """
        Fila de botones para el redireccinamiento de ventana

        Recibe un objeto de la clase :class:`ft.Page` para poder
        realizar el redireccionamiento de ventanas

        Regresa un objeto de la clase :class:`ft.Container`
        """
        button_row_content: ft.Container = ft.Container(
            expand = True,
            height = styles["buttons"]["row_height"],
            content = ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                spacing = styles["buttons"]["row_spacing"],
                controls = [
                    # Botón hacia la ventana de lista de kanjis
                    ft.ElevatedButton(
                        height = styles["buttons"]["height"],
                        width = styles["buttons"]["width"],
                        bgcolor = styles["buttons"]["color"],
                        content = ft.Text(
                            "Lista de kanjis",
                            font_family = styles["buttons"]["font"],
                            size = styles["buttons"]["size"],
                            color = styles["text"]["color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER
                        )
                    ),
                    # Botón hacia la ventana de aprendizaje
                    ft.ElevatedButton(
                        height = styles["buttons"]["height"],
                        width = styles["buttons"]["width"],
                        bgcolor = styles["buttons"]["color"],
                        content = ft.Text(
                            "Aprender",
                            font_family = styles["buttons"]["font"],
                            size = styles["buttons"]["size"],
                            color = styles["text"]["color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER
                        ),
                        on_click = lambda _: page.go('/learn_kanji')
                    ),
                    # Botón hacia la ventana de vocabulario
                    ft.ElevatedButton(
                        height = styles["buttons"]["height"],
                        width = styles["buttons"]["width"],
                        bgcolor = styles["buttons"]["color"],
                        content = ft.Text(
                            "Vocabulario",
                            font_family = styles["buttons"]["font"],
                            size = styles["buttons"]["size"],
                            color = styles["text"]["color"],
                            weight = ft.FontWeight.W_300,
                            text_align = ft.TextAlign.CENTER
                        ),
                        on_click = lambda _: page.go('/vocabulary')
                    )
                ]
            )
        )

        return button_row_content
