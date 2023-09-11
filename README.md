# KanjiApp

## Descripción

Apliación creada con el fin de ayudar a los estudiantes de japonés a aprender los kanjis de una manera más fácil y divertida. Además de contar con una base de datos de vocabulario para poder buscar palabras en japonés y su significado en inglés.

Los kanjis pueden facilmente ser agregados o modificados en el archivo _kanji.xlsx_. Solo se necesita indicar el kanji, sus lecturas en on'yomi y kun'yomi y su significado en inglés.

## Instalación

  - Requiere Python 3.8 o superior
  - Requiere Flet 0.10.0 o superior
  - Requiere pyttsx3 2.90 o superior
  - Requiere Pandas 1.2.4 o superior
  - Requiere PyInstaller v5.7.0 o superior

```python
pip install flet, pyttsx3, pandas, pyinstaller
```

## Preview de la aplicación:

### Menú principal

![image](/assets/main_menu.png "Menú principal")

La aplicación cuenta con 3 opciones:
  - **Aprender**: En esta opción se puede aprender los kanjis guardados en el archivo _kanji.xlsx_, además de ver vocabulario relacionado al kanji.
  - **Lista de kanjis**: En esta opción se puede ver la lista de kanjis guardados en el archivo _kanji.xlsx_.
  - **Vocabulario**: En esta opción se puede ver el vocabulario almacenado en la base de datos de la aplicación. Cuenta con la posibilidad de bsucar por kanji.
    - **Importante**: La base de datos se limita al vocabulario al utilizado por el libro de texto _Genki 3rd Edition_ de la editorial _The Japan Times_. Por lo que se si quiere agregar más vocabulario, se debe habilitar manualmente la base de datos de _JamDict_ (Favor de contactarme para llevar a cabo este proceso).

### Aprender

![image](/assets/aprender.png "Aprender")

La ventana más importante de la aplicación, en esta se puede aprender los kanjis guardados en el archivo _kanji.xlsx_, además de ver vocabulario relacionado al kanji.

### Lista de kanjis

![image](/assets/lista_de_kanjis.png "Lista de kanjis")

En esta ventana se puede ver la lista de kanjis guardados en el archivo _kanji.xlsx_.

### Vocabulario

![image](/assets/vocabulario.png "Vocabulario")

En esta ventana se puede ver el vocabulario almacenado en la base de datos de la aplicación. Cuenta con un buscador de palabras por kanji.

## Información de contacto

Para cualquier duda o comentario, favor de contactarme a mi correo electrónico. La retrolamentación es bienvenida ya que dediqué un buen tiempo a este proyecto y me gustaría saber que opinan de él.

  - **Nombre**: Erick Daniel Ortiz Cervantes
  - **Correo**: A01750495@tec.mx