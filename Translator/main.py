from re import T
from googletrans import Translator

trans = Translator()

txt = trans.translate('hello', dest='de')
print(txt)