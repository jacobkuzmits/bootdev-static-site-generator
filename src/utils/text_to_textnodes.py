from nodes.textnode import TextNode, TextType
from utils.split_nodes_delimiter import split_nodes_delimiter
from utils.split_nodes_link import split_nodes_link
from utils.split_nodes_image import split_nodes_image


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    with_images = split_nodes_image([text_node])
    with_links = split_nodes_link(with_images)
    with_bolds = split_nodes_delimiter(with_links, "**", TextType.BOLD)
    with_italics = split_nodes_delimiter(with_bolds, "_", TextType.ITALIC)
    with_code = split_nodes_delimiter(with_italics, "`", TextType.CODE)
    return with_code
