import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Test Text", None, None)
        node2 = HTMLNode("p", "Test Text")
        self.assertEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "test.com", "target": "_blank"})
        props_string = node.props_to_html()
        expected_string = ' href="test.com" target="_blank"'
        self.assertEqual(props_string, expected_string)
        
if __name__ == "__main__":
    unittest.main()