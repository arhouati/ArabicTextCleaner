import regex as re
from langdetect import detect
import logging
import os

dir_base = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(filename=dir_base + '/../logs/ArabicTextCleaner.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class ArabicTextCleaner:

    def __init__(self):
        return None

    def process(self, data=[]):
        data = list(map(self.process_text, data))
        data = list(filter(self.is_arabic, data))
        return data

    def process_text(self, text=''):
        text = self.remove_latin_char(text)
        text = self.remove_extra_spaces(text)

        return text

    def remove_latin_char(self, text=''):
        return re.sub('[\p{Latin}]', u'', text)

    def remove_extra_spaces(self, text=''):
        return ' '.join(text.split())

    def is_arabic(self, text=''):
        try:
            lang = detect(text)
            if lang == 'ar':
                return True
        except Exception as e:
            if __debug__:
                logging.warning("The text '{}' throws an error : {} ".format(text, e))
            return False

        return False