import spacy

def extract_customs_fields(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return {ent.label_: ent.text for ent in doc.ents}
