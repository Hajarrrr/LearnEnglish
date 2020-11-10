import nltk
import numpy as np
import random
import string # to process standard python strings

from nltk.chat.util import Chat,reflections

pairs=[
    ["Hello",["Hey"]]
]
chat=Chat(pairs)
chat.converse()