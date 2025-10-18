import unittest
from utils.split_nodes_link import split_nodes_link
from nodes.textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):

    def test_one_node_one_link(self):
        # with pre and post text
        node = TextNode("pre-text [link_text](url/1.jpg) post-text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("link_text", TextType.LINK, "url/1.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

        # with post text
        node = TextNode("[link_text](url/1.jpg) post-text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link_text", TextType.LINK, "url/1.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

        # with pre text
        node = TextNode("pre-text [link_text](url/1.jpg)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("link_text", TextType.LINK, "url/1.jpg"),
            ],
            new_nodes,
        )

    def test_one_node_two_links(self):
        node = TextNode(
            "pre-text [link_text1](url/1.jpg) mid-text [link_text2](url/2.jpg) post-text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("link_text1", TextType.LINK, "url/1.jpg"),
                TextNode(" mid-text ", TextType.TEXT),
                TextNode("link_text2", TextType.LINK, "url/2.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_one_node_two_touching_links(self):
        # directly touching links
        node = TextNode(
            "pre-text [link_text1](url/1.jpg)[link_text2](url/2.jpg) post-text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("link_text1", TextType.LINK, "url/1.jpg"),
                TextNode("link_text2", TextType.LINK, "url/2.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

        # with space between links
        node = TextNode(
            "pre-text [link_text1](url/1.jpg) [link_text2](url/2.jpg) post-text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("pre-text ", TextType.TEXT),
                TextNode("link_text1", TextType.LINK, "url/1.jpg"),
                TextNode(" ", TextType.TEXT),
                TextNode("link_text2", TextType.LINK, "url/2.jpg"),
                TextNode(" post-text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_two_nodes_one_link_each(self):
        nodes = [
            TextNode("pre-text1 [link_text1](url/1.jpg) post-text1", TextType.TEXT),
            TextNode("pre-text2 [link_text2](url/2.jpg) post-text2", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("pre-text1 ", TextType.TEXT),
                TextNode("link_text1", TextType.LINK, "url/1.jpg"),
                TextNode(" post-text1", TextType.TEXT),
                TextNode("pre-text2 ", TextType.TEXT),
                TextNode("link_text2", TextType.LINK, "url/2.jpg"),
                TextNode(" post-text2", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
