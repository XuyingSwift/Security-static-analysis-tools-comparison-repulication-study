from lxml import etree

doc = etree.parse('rats-putty-0.61.xml')


for elem in doc.xpath('.//name'):
    parent = elem.getparent()
    parent.remove(elem)

for elem in doc.xpath('.//message'):
    parent = elem.getparent()
    parent.remove(elem)

doc.write('new-rats-putty-0.61.xml')
