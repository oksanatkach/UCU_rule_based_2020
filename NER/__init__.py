import spacy
from spacy.pipeline import EntityRuler
from .matcher_util import add_gaz_to_patterns

nlp = spacy.load('en_core_web_sm')
#@todo: replace the original NER model in the nlp pipeline with the ruler
