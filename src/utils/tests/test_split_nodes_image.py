import unittest
from utils.split_nodes_image import split_nodes_image
from nodes.textnode import TextNode, TextType


class TestSplitNodesImage(unittest.TestCase):

    def test_one_node_one_image(self):
        # with pre and post text
        node = TextNode("pre-text ![alt_text](url/1.jpg) post-text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("alt_text", TextType.IMAGE, "url/1.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

        # with post text
        node = TextNode("![alt_text](url/1.jpg) post-text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt_text", TextType.IMAGE, "url/1.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

        # with pre text
        node = TextNode("pre-text ![alt_text](url/1.jpg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("alt_text", TextType.IMAGE, "url/1.jpg"),
            ],
            new_nodes,
        )

    def test_one_node_two_images(self):
        node = TextNode(
            "pre-text ![alt_text1](url/1.jpg) mid-text ![alt_text2](url/2.jpg) post-text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("alt_text1", TextType.IMAGE, "url/1.jpg"),
                TextNode(" mid-text ", TextType.TEXT),
                TextNode("alt_text2", TextType.IMAGE, "url/2.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_one_node_two_touching_images(self):
        # directly touching images
        node = TextNode(
            "pre-text ![alt_text1](url/1.jpg)![alt_text2](url/2.jpg) post-text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("alt_text1", TextType.IMAGE, "url/1.jpg"),
                TextNode("alt_text2", TextType.IMAGE, "url/2.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

        # with space between images
        node = TextNode(
            "pre-text ![alt_text1](url/1.jpg) ![alt_text2](url/2.jpg) post-text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("alt_text1", TextType.IMAGE, "url/1.jpg"),
                TextNode(" ", TextType.TEXT),
                TextNode("alt_text2", TextType.IMAGE, "url/2.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_two_nodes_one_image_each(self):
        nodes = [
            TextNode("pre-text1 ![alt_text1](url/1.jpg) post-text1", TextType.TEXT),
            TextNode("pre-text2 ![alt_text2](url/2.jpg) post-text2", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("pre-text1 ", TextType.TEXT),
                TextNode("alt_text1", TextType.IMAGE, "url/1.jpg"),
                TextNode(" post-text1", TextType.TEXT),
                TextNode("pre-text2 ", TextType.TEXT),
                TextNode("alt_text2", TextType.IMAGE, "url/2.jpg"),
                TextNode(" post-text2", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
