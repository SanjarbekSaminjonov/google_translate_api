from googletrans import Translator

translater = Translator()


def translate(text, src, dest):
    try:
        return translater.translate(text, src=src, dest=dest).text
    except:
        return "Xatolik bor!"

