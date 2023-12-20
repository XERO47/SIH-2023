import xml.etree.ElementTree as ET

def parse_xml(file_path):
    """Parse an XML file and return the root element."""
    tree = ET.parse(file_path)
    return tree.getroot()

def find_element(root, tag):
    """Find the first element with the given tag."""
    return root.find(tag)

def find_all_elements(root, tag):
    """Find all elements with the given tag."""
    return root.findall(tag)

def get_element_text(element):
    """Get the text content of an element."""
    return element.text

def get_element_attrib(element):
    """Get the attributes of an element."""
    return element.attrib

#  You can use these functions in your specific parsers to extract information from XML manifest files. 
# For example, in your Maven parser, you might use parse_xml to parse the pom.xml file, 
# find_element to find the <version> element, and get_element_text to get the version number.