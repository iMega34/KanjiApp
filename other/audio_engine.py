
import pyttsx3


class AudioEngine:
    """
    Contiene los métodos para la lectura de texto en el programa

    Para el constructor, se requiere de los siguientes parámetros:
        - :param:`voice`: Es el identificador de la voz que se usará para la lectura del texto. Si no se pasa nada se asume que es la voz por defecto

    Existen otros dos parámetros opcionales:
        - :param:`rate`: Es la velocidad a la que se leerá el texto. Por defecto es 150
        - :param:`volume`: Es el volumen al que se leerá el texto. Por defecto es 1.0

    Las voces disponibles para su uso dentro del programa depende de qué voces se encuentren instaladas en el sistema operativo
    Para obtener una lista de las voces disponibles, se puede usar el método :method:`list_available_voices`
    """

    engine: pyttsx3.Engine

    def __init__(self, voice: str = None, rate: int = 125, volume: float = 1.0) -> None:
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty("voice", f"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_{voice}")
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)


    def list_available_voices(self) -> None:
        """
        Imprime en consola una lista de las voces disponibles para su uso dentro del programa

        Los datos que se muestran son el nombre de la voz y el identificador de la voz, el cual se debe copiar y pegar
        para ser pasado dentro del constructor de la clase :class:`AudioEngine` como el parámetro :param:`voice`
        """

        voices: list[str] = [self.engine.getProperty("voices")]

        for id, voice in enumerate(voices[0]):
            # Se elimina la parte inicial del identificador de la voz, ya que es la misma para todas las voces.
            # Permite que solo se muestre la parte del identificador de la voz en que se diferencia de las demás
            # y por lo tanto, lo que se debe copiar y pegar para usarlo en el constructor de la clase AudioEngine
            # 
            # IMPORTANTE: Por el momento, esto solo funciona en Windows, ya que el identificador de la voz es
            # diferente en otros sistemas operativos
            voice.id = voice.id.strip("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_")
            print(f"{id + 1}: {voice.name} \t ID: {voice.id}")


    def read_readings(self, readings: list[str]) -> None:
        """
        Realiza la lectura del texto que se pasa como parámetro

        Recibe una lista con texto como parámetro y lo lee en voz alta con la voz que se haya pasado en el constructor
        """

        self.engine.startLoop(False)
        # Convierte la lista de palabras en una cadena de texto separada por comas
        readings = ", ".join(readings)
        self.engine.say(readings)
        self.engine.iterate()
        self.engine.endLoop()


    def read_text(self, text: str) -> None:
        """
        Realiza la lectura del texto que se pasa como parámetro

        Recibe un texto como parámetro y lo lee en voz alta con la voz que se haya pasado en el constructor
        """

        self.engine.startLoop(False)
        self.engine.say(text)
        self.engine.iterate()
        self.engine.endLoop()
