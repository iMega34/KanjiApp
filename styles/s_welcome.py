
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
    "exit_button" : {
        "width" : 60,
        "height" : 60,
        "border_radius" : 50,
        "color" : "#DBD1A7",
        "exit_color" : "#FF0000",
        "icon_size" : 40
    }
}


class SWelcome:
    """
    Propiedades de los controles utilizados por la función :function:`Welcome`
    del archivo :file:`welcome.py` para la creación de la ventana de bienvenida
    """

    def _on_hover(self, _: ft.HoverEvent) -> None:
        """
        Permite a los botones cambiar de color al pasar el cursor sobre ellos
        """

        if _.data == "true":
            for __ in range(20):
                self._exit_button.elevation += 1
                self._exit_button.update()
        else:
            for __ in range(20):
                self._exit_button.elevation -= 1
                self._exit_button.update()


    def exit_button(self, page: ft.Page) -> ft.Card:
        """
        Botón para salir de la aplicación

        Recibe un objeto de la clase :class:`ft.Page` para poder
        realizar el cierre de la ventana

        Regresa un objeto de la clase :class:`ft.Card`
        """

        self._exit_button_content: ft.Container = ft.Container(
            width = styles["exit_button"]["width"],
            height = styles["exit_button"]["height"],
            border_radius = ft.border_radius.all(styles["exit_button"]["border_radius"]),
            bgcolor = styles["exit_button"]["color"],
            alignment = ft.alignment.center,
            content = ft.Icon(
                name = ft.icons.CANCEL,
                color = styles["exit_button"]["exit_color"],
                size = styles["exit_button"]["icon_size"]
            ),
            on_hover = lambda _: self._on_hover(_),
            on_click = lambda _: page.window_destroy()
        )

        self._exit_button: ft.Card = ft.Card(
            elevation = 0,
            color = styles["exit_button"]["color"],
            content = self._exit_button_content
        )

        return self._exit_button


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
                        ),
                        on_click = lambda _: page.go('/kanji_list')
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
