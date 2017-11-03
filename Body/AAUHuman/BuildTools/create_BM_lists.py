import xmltodict


with open('../BodyModel.define.xml') as fp:
    anyxdefs = xmltodict.parse(fp.read())['anyxdefs']


parameters = [
    e['@name']
    for e in anyxdefs['parameter']
]

constants = [
    e['@name']
    for e in anyxdefs['constant']
]

with open('bm-parameters.txt','w') as fp:
    fp.write(" ".join(parameters))

with open('bm-constants.txt','w') as fp:
    fp.write(" ".join(constants))



anyscript_highlighters = f"""
# VS code plugin
- name: support.variable
  match: '\\b({'|'.join(parameters)})\\b'

- name: support.constant
  match: '\\b({'|'.join(constants)})\\b'

# NPP plugin
            <Keywords name="Keywords5">{' '.join(parameters)}</Keywords>
            <Keywords name="Keywords6">{' '.join(constants)}</Keywords>

"""

with open('anyscript_highlighters.txt', 'w') as fp:
    fp.write(anyscript_highlighters)