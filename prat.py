!pip install -U pip setuptools wheel
!pip install -U spacy
!python -m spacy download en_core_web_sm
!pip install spacytextblob

import pkg_resources, imp
imp.reload(pkg_resources)
#missao2
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
#missao3
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
#missao4
user_input = 'This is a wonderful campsite. I loved the serenity and the birds chirping in the morning.'
doc = nlp(user_input)
#missao5
input_polarity = doc._.polarity
sentiment = {'score': input_polarity}
print(sentiment)
#missao final
tweets = [
    "Bayer Leverkusen goalkeeper Bernd Leno will not be going to Napoli...",
    "@ChelseaFC Don't make him regret it and start him over Hoofiz...",
    # Adicione os outros tweets aqui
]
