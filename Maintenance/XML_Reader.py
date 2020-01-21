import xml.etree.ElementTree as ET


def get(path):
    tree = ET.parse(path)
    root = tree.getroot()

    qalist = []
    for child in root.findall('question'):
        qalist.append({'group': (child.get('qgroup')), 'question': (child.get('qtext')), 'answer': (child.get('qanswer'))})
    return qalist
