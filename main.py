import xml.etree.ElementTree as ETree
import json


def recursive(tree):
    for child in tree:
        print(child)
        recursive(child)


def remove_incorrect(tree):
    # checking objects
    for object in tree.findall('object'):
        no_name = object.find('obj_name') is None
        empty_name = not (object.findtext('obj_name') and object.findtext('obj_name').strip())
        no_fields = object.find('field') is None
        if no_name or empty_name or no_fields:
            tree.remove(object)
        # checking object fields
        for element in object:
            tag = element.tag
            if not (tag == 'obj_name' or tag == 'field')
                object.remove(element)
            # checking fields
    return ETree.ElementTree(tree)



def main():
    with open('input.xml', 'r') as infile:
        tree_root = ETree.fromstringlist(['<imaginaryroot>', infile.read(), '</imaginaryroot>'])
    # tree = ETree.ElementTree(tree_root)
    recursive(tree_root)
    print('\n\n')
    new_tree = remove_incorrect(tree_root)
    print('\n\nNew tree:\n\n')
    # recursive(new_tree)
    print(new_tree)
    new_tree.write('output.xml')

main()

# with open('output.json', 'w') as file:
#     json.dump(something, file)