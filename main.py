import xml.etree.ElementTree as ETree
import json
from glob import glob as gglob


def recursive(tree):
    for child in list(tree):
        print(child)
        recursive(child)


def remove_incorrect(tree):
    out_dict = dict()

    # checking objects
    for treeObject in tree.findall('object'):
        no_name = treeObject.find('obj_name') is None
        name = treeObject.findtext('obj_name')
        no_fields = treeObject.find('field') is None

        if no_name or (not name and not name.strip()) or no_fields:
            tree.remove(treeObject)
            continue

        inner_dict = dict()
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
                inner_dict[element.findtext('name')] = element.findtext('value')

        # saving to dictionary
        out_dict[name] = inner_dict

    # return ETree.ElementTree(tree)
    return out_dict


def main():
    xml_files = gglob('*.xml')

    for xml_file in xml_files:
        try:
            with open(xml_file, 'r') as infile:
                tree_root = ETree.fromstringlist(['<imaginaryroot>', infile.read(), '</imaginaryroot>'])
        except OSError:
            print("File not found")
            continue
        except ETree.ParseError:
            print("File badly constructed, cannot convert")
            continue
        else:
            new_tree = remove_incorrect(tree_root)
            json_file = xml_file[:-4] + '.json'
            with open(json_file, 'w') as outfile:
                json.dump(new_tree, outfile, indent=4)


main()
