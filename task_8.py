class MorseMsg:
    """
    Morse code message class

    Attributes:
        coded_str (str): A coded message in the form of a string of dots and dashes.
    """
    ENG_MORSE = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }

    RUS_MORSE = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э',
        '..--': 'Ю', '.-.-': 'Я'
    }

    ENG_VOWELS = "AEIOUY"
    RU_VOWELS = "АЕЁИОУЫЭЮЯ"

    ENG_CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
    RU_CONSONANTS = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"

    def __init__(self, coded_str: str) -> None:
        """
        Initializes an instance of the MorseMsg class.

        Args:
            coded_str: A string of an encoded Morse message.
        """
        self.coded_str = coded_str.strip().split(" ")

    def eng_decode(self) -> str:
        """
        Decodes the message into Latin letters.
        Returns:
            str: Decrypted message in Latin letters
        """
        decoded_letters = []
        for ch in self.coded_str:
            if ch in self.ENG_MORSE:
                decoded_letters.append(self.ENG_MORSE[ch])
        return "".join(decoded_letters)

    def ru_decode(self):
        """
        Decodes the message into Russian letters.
        Returns:
            str: Decrypted message in Cyrillic letters.
        """
        decoded_letters = []
        for ch in self.coded_str:
            if ch in self.RUS_MORSE:
                decoded_letters.append(self.RUS_MORSE[ch])
        return "".join(decoded_letters)

    def get_vowels(self, lang):
        """
        Returns a list of vowels in the lang language, in the order they appear
        in the message.
        Args:
            lang (str): The language of the message.

        Returns:
            list: A list of vowels from the message.
        """
        decoded = self.eng_decode() if lang == 'eng' else self.ru_decode()
        vowels = self.ENG_VOWELS if lang == 'eng' else self.RU_VOWELS
        return [ch for ch in decoded if ch in vowels]

    def get_consonants(self, lang):
        """
        Returns a list of consonants in the lang language, in the order they appear
        in the message.
        Args:
            lang (str): The language of the message.

        Returns:
            list: A list of consonants from the message.
        """
        decoded = self.eng_decode() if lang == 'eng' else self.ru_decode()
        cons = self.ENG_CONSONANTS if lang == 'eng' else self.RU_CONSONANTS
        return [ch for ch in decoded if ch in cons]

    def __str__(self) -> str:
        """
        Returns a string representation of the object that shows the encoded message.
        """
        return " ".join(self.coded_str)

    def __repr__(self) -> str:
        """
        Returns a string representation for debugging.

        Returns:
            str: A string that allows you to recreate the object.
        """
        return f"MorseMsg('{' '.join(self.coded_str)}')"


msgs = []
msgs.append(MorseMsg('.. .-.. .. -.- . .--. -.-- - .... --- -.'))
msgs.append(MorseMsg('-- --- .-.- .--. .-. --- --. .-. .- -- -- .-'))
for msg in msgs:
    print(msg)
print(msgs[0].eng_decode())
print(msgs[0].get_vowels('eng'))
print(msgs[0].get_consonants('eng'))
print(msgs[1].ru_decode())
print(msgs[1].get_vowels('ru'))
print(msgs[1].get_consonants('ru'))
