import spacy
from spacy.pipeline import EntityRuler
from .matcher_util import add_gaz_to_patterns

nlp = spacy.load('en_core_web_sm')
ruler = EntityRuler(nlp)
ruler.add_patterns(add_gaz_to_patterns())
nlp.add_pipe(ruler)
nlp.remove_pipe('ner')
