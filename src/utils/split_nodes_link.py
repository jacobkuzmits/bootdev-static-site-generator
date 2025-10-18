from nodes.textnode import TextNode, TextType
from utils.extract_markdown_links import extract_markdown_links


def split_nodes_link(nodes):
    out = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        links = extract_markdown_links(node.text)
        unprocessed_text = node.text
        for i in range(len(links)):
            link = links[i]
            link_text = link_tuple_to_markdown(link)
            split_node = unprocessed_text.split(link_text, maxsplit=1)
            if split_node[0] != "":
                out.append(TextNode(split_node[0], TextType.TEXT))
            out.append(TextNode(link[0], TextType.LINK, link[1]))
            if i == len(links) - 1 and split_node[1] != "":
                out.append(TextNode(split_node[1], TextType.TEXT))
            unprocessed_text = split_node[1]

    return out


def link_tuple_to_markdown(tuple):
    return f"[{tuple[0]}]({tuple[1]})"
