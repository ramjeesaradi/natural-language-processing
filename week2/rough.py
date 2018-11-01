doc = """This is the house that Jack built. This is the malt that lay in the house that Jack built. This is the rat that ate the malt that lay in the house that Jack built."""
doc.replace('.', '')
doc = doc.split(" ")
doc = [''] + doc + ['']
lay_that = 0.0
that_count = 0.0
for i in range(0, len(doc)-1):
    if(doc[i] == 'that'):
        that_count += 1
        if (doc[i+1]=='lay'):
            lay_that += 1
print(doc)
print(lay_that/that_count)

doc = "This is the rat that ate the malt that lay in the house that Jack built."
doc.replace('.', '')
doc = doc.split(" ")
doc = [''] + doc + ['']
sen = "This is the house that Jack built"
sen = sen.split(' ')
sen = [''] + sen + ['']
lay_that = 0.0
that_count = 0.0
for i in range(0, len(doc)-1):
    if(doc[i] == 'that'):
        that_count += 1
        if (doc[i+1]=='lay'):
            lay_that += 1
print(doc)
print(lay_that/that_count)
