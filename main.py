import xml.etree.ElementTree as ETree
import json

def recursive(tree):
    for child in tree:
        print(child)
        recursive(child)

def main():
    with open('input.xml', 'r') as infile:
        tree = ETree.fromstringlist(['<imaginaryroot>', infile.read(), '</imaginaryroot>'])
    recursive(tree)

main()

# with open('output.json', 'w') as file:
#     json.dump(something, file)