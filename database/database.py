
import csv
import sqlite3


class Database:

    def __init__(self) -> None:
        self._csv_path: str = "database\genki_3rd_vocab_database.csv"
        self._db_path: str = "database\genki_3rd_vocab_database.db"
        self.search_results: dict[list[str], list[str]] = {
            "kanji" : [],
            "meaning" : []
        }


    def _csv_to_database(self) -> None:
        """
        Convierte un archivo .csv en una base de datos .db con SQLite3.
        """

        # Se crea la conexión y el cursor
        _connection: sqlite3.Connection = sqlite3.connect(self._db_path)
        _cursor: sqlite3.Cursor = _connection.cursor()

        # Se crea una lista temporal para almacenar los datos
        _temp_list: list[tuple[str, str]] = []

        # Se abre el archivo CSV, se leen los datos y se almacenan en la lista temporal
        with open(self._csv_path, newline = "", encoding = "utf-8") as csvfile:
            _reader = csv.reader(csvfile, delimiter = ",", quotechar = '"')
            for row in _reader:
                left_str_to_clean = row[0]
                right_str_to_clean = row[1]

                # Se eliminan las etiquetas HTML, como <rt> y <small>
                key_idx = left_str_to_clean.find("<rt>")
                if key_idx != -1:
                    left_str_to_clean = left_str_to_clean[6:key_idx]

                right_str_to_clean = right_str_to_clean.split("<small>")[0].strip()

                _temp_list.append((left_str_to_clean, right_str_to_clean))

        # Se crea la tabla y se insertan los datos
        _cursor.execute(
            ''' CREATE TABLE IF NOT EXISTS vocabulary (kanji TEXT, meaning TEXT) '''
        )

        _connection.commit()

        # Se elimina la lista temporal para liberar memoria

        # Se insertan los datos en la tabla
        _cursor.executemany(
            ''' INSERT INTO vocabulary VALUES (?, ?) ''', _temp_list
        )

        _connection.commit()

        del _temp_list

        # Prueba de que la base de datos se creó correctamente
        # Por defecto, se comenta para evitar que se imprima en la terminal
        # _test_printing = _cursor.execute(
        #     ''' SELECT * FROM vocabulary '''
        # )

        # for row in _test_printing:
        #     print(row)

        _cursor.close()
        _connection.close()


    def search_vocab(self, kanji: str) -> dict[list[str], list[str]]:

        _connection: sqlite3.Connection = sqlite3.connect(self._db_path)
        _cursor: sqlite3.Cursor = _connection.cursor()

        list_search_results: list[tuple[str, str]] = _cursor.execute(
            '''SELECT * FROM vocabulary WHERE kanji LIKE ?''', ('%' + kanji + '%',)
        ).fetchall()

        for result in list_search_results:
            self.search_results['kanji'].append(result[0])
            self.search_results['meaning'].append(result[1])

        _cursor.close()
        _connection.close()

        return self.search_results
