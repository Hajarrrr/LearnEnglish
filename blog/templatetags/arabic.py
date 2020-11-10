from django import template

register = template.Library()

@register.simple_tag
def trans(eng):
        from googletrans import Translator
        translator = Translator()
        r=translator.translate(eng, dest='ar')
        return r.text