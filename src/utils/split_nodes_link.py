from nodes.textnode import TextNode, TextType
from utils.extract_markdown_links import extract_markdown_links


def split_nodes_link(nodes):
    out = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            out.append(node)
            continue

        for link_text, link_url in links:
            markdown_text = f"[{link_text}]({link_url})"
            parts = text.split(markdown_text, 1)

            if len(parts) != 2:
                raise ValueError(
                    "invalid markdown, link section not closed or mismatched"
                )

            if parts[0]:
                out.append(TextNode(parts[0], TextType.TEXT))

            out.append(TextNode(link_text, TextType.LINK, link_url))
            text = parts[1]

        if text:
            out.append(TextNode(text, TextType.TEXT))

    return out
