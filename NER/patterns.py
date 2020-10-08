
patterns = [
    {"label": "LOCATION", "pattern": [{"LOWER": "san"}, {"LOWER": "francisco"}]},
    {'label': 'DATE', 'pattern': [{'LOWER':'january'}, {'IS_DIGIT': True}, {'LEMMA':',', 'OP':'?'}, {'IS_DIGIT':True, 'LENGTH':4}]}
]
