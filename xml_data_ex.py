import xml.etree.ElementTree as ET

xml_data = "<root><child>data</child></root>"
root = ET.fromstring(xml_data)
print(root.tag)                                                      