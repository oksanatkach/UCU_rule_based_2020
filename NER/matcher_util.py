import os
from .patterns import patterns

gaz_path = os.path.dirname(os.path.realpath(__file__))

def add_gaz_to_patterns():
    config_path = gaz_path + '/gazetteers/lists.def'
    rows = open(config_path, 'r').read().strip().split('\n')
    for row in rows:
        row = row.split(':')
        file = row[0]
        label = row[1]
        words = open(gaz_path + '/gazetteers/' + file, 'r').read().strip().split('\n')
        for word in words:
            patterns.append({'label':label, 'pattern':word})
    return patterns
