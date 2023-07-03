
class Kanji:
    """
    Crea un objeto Kanji creado a partir de la información de la tabla de kanjis, require que la
    creación de la tabla de kanjis se haya realizado previamente a través del método :method:`build_table`
    de la clase :class:`KanjiTable` del archivo :file:`kanji_table.py`.

    El objeto Kanji puede crearse manualmente proporcionando los siguientes parámetros:
    - id: Identificador del kanji
    - kanji: Kanji
    - meaning: Significado del kanji
    - onyomi: Lectura on'yomi del kanji
    - kunyomi: Lectura kun'yomi del kanji

    Sin embargo, es recomendable crear el objeto a partir de los datos de la tabla de kanjis hecha a través
    del Excel ya que se usa como plantilla para hacer más eficiente el proceso de creación de los objetos Kanji
    """

    def __init__(self) -> None:
        self.id: int = 0
        self.kanji: str = ""
        self.meaning: str = ""
        self.onyomi: list = []
        self.kunyomi: list = []


    def build_kanji(self, id: int, kanji: str, meaning: str, onyomi: str, kunyomi: str) -> None:
        """
        Construye el objeto kanji a partir de los datos capturados de una fila de la tabla de kanjis,
        o por datos proporcionados manualmente
        """

        self.id = id
        self.kanji = kanji
        self.meaning = meaning
        self.onyomi = onyomi.split(",")
        self.kunyomi = kunyomi.split(",")
