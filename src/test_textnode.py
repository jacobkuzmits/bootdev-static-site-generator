import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_type(self):
            node = TextNode("Text", TextType.BOLD)
            node2 = TextNode("Text", TextType.ITALIC)
            self.assertNotEqual(node, node2)

    def test_missing_type(self):
         node = TextNode("Text", TextType.TEXT)
         node2 = TextNode("Text")
         self.assertEqual(node, node2)
    
    def test_missing_url(self):
         node = TextNode("Text", TextType.TEXT, "https://test.com")
         node2 = TextNode("Text", TextType.TEXT)
         self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()