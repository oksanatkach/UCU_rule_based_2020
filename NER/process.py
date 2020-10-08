from NER import nlp

def get_NERs(text):
    doc = nlp(text)
    return doc, doc.ents

if __name__ == '__main__':
    # print(get_NERs('Lviv'))
    print(get_NERs('January 5, 2021'))
