import xml.etree.ElementTree as ETree
import json


def recursive(tree):
    for child in list(tree):
        print(child)
        recursive(child)


def remove_incorrect(tree):
    # checking objects
    for treeObject in tree.findall('object'):
        no_name = treeObject.find('obj_name') is None
        empty_name = not treeObject.findtext('obj_name')
                          # and treeObject.findtext('obj_name').strip())
        no_fields = treeObject.find('field') is None
        if no_name or empty_name or no_fields:
            tree.remove(treeObject)
            continue
        # checking object fields
        for element in list(treeObject):
            tag = element.tag
            if not (tag == 'obj_name' or tag == 'field'):
                treeObject.remove(element)
                continue
            # checking fields
            if tag == 'field':
                incomplete_field = (element.find('name') is None
                                    or element.find('type') is None
                                    or element.find('value') is None)
                wrong_type = not (element.findtext('type') == 'string'
                                  or element.findtext('type') == 'int')
                if incomplete_field or wrong_type:
                    treeObject.remove(element)
                    continue
                element.remove(element.find('type'))
    return ETree.ElementTree(tree)


def main():
    with open('input.xml', 'r') as infile:
        tree_root = ETree.fromstringlist(['<imaginaryroot>', infile.read(), '</imaginaryroot>'])
    # tree = ETree.ElementTree(tree_root)
    new_tree = remove_incorrect(tree_root)
    new_tree.write('output.xml')
    # with open('output.json', 'w') as file:
    #     json.dump(new_tree.getroot().attrib, file)


main()
