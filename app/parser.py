
"""Parser.py."""
import re


class Parser:
    """Phrase parser class."""

    def del_punctuation(self, msg):
        """Remove the punctuation.

        Parameter:
            msg(str) Character string to be processed.

        Return:
            (str)
        """
        return re.sub(r'[^\w\s]', ' ', msg.lower())

    def list_cleaner(self, word_list):
        """Remove non-essential items.

        Parameter:
            word_list(lst) List of string.

        Return:
            (lst) List of string cleaned.
        """
        return [elt for elt in word_list if len(elt) > 1]

    def find_location(self, msg):
        """Try to find a location in a query.

        Parameter:
            msg(str): Character string to be processed.

        Return:
            (lst) List of words referring to a place.
        """
        key_words = ['adresse',
                     'trouve',
                     'indique moi',
                     'emplacement de',
                     'o[u,ù] est',
                     'location de',
                     'end_list'
                     ]

        msg = self.del_punctuation(str(msg))

        if 'script' in msg:
            return None

        for word in key_words:
            if word == 'end_list':
                return None
            if word in msg:
                result = re.findall('(?<=' + word + '.).*', msg)
                break

        return self.list_cleaner(result[0].split(' '))
