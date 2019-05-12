import libs.etree.ElementTree as ETree
from libs.json import dump as jsdump
from libs.glob import glob as gglob
from source.cleanup_xml import remove_incorrect


def main():
    # listing all xml files
    xml_files = gglob('*.xml')

    for xml_file in xml_files:
        with open(xml_file, 'r') as infile:
            try:
                tree_root = ETree.parse(xml_file)
            except ETree.ParseError:
                # for files with no root element
                try:
                    tree_root = ETree.fromstringlist(['<imaginaryroot>', infile.read(), '</imaginaryroot>'])
                except ETree.ParseError:
                    print("File badly constructed, cannot convert")
                    continue
        # converting to Element, if needed
        if type(tree_root) is ETree.ElementTree:
            tree_root = tree_root.getroot()
        new_tree = remove_incorrect(tree_root)
        # creating output file with the same name as input file
        json_file = xml_file[:-4] + '.json'
        with open(json_file, 'w') as outfile:
            jsdump(new_tree, outfile, indent=4)


main()
