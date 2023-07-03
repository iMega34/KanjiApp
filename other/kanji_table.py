
import pandas as pd


class KanjiTable:
    """
    Contiene el método :method:`build_table` que construye la tabla de kanjis
    a partir de un archivo de Excel que contiene la información de los kanjis
    proporcionados por el usuario

    Altamente recomendable que se use esta clase para construir la tabla de kanjis, ya que el archivo
    de Excel sirve como plantilla para la creación de los objetos de la clase :class:`Kanji`
    y así hacer más eficiente el proceso de creación de los mismos
    """

    def __init__(self) -> None:
        self.table = pd.DataFrame()


    def build_table(self, spreadsheet: str) -> pd.DataFrame:
        """
        Construye la tabla de kanjis a partir de un archivo de Excel
        """

        self.table = pd.read_excel(spreadsheet)
        self.table.set_index('ID', inplace = True)
        # Previene que se muestren los valores NaN en las listas de lecturas
        self.table = self.table.fillna('')

        return self.table
