import os
import random
from django import template
from django.conf import settings
from ..models import nouns

register = template.Library()

@register.simple_tag
def CorespondingWord(url,nouns):
        for noun in nouns :
            if url==noun.photo_url:
                return noun.eng
            else :
                print("yes")
                continue