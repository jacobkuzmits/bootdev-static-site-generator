from nodes.textnode import TextNode, TextType
from utils.extract_markdown_images import extract_markdown_images


def split_nodes_image(nodes):
    out = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            out.append(node)
            continue

        for alt_text, image_url in images:
            markdown_text = f"![{alt_text}]({image_url})"
            parts = text.split(markdown_text, 1)

            if len(parts) != 2:
                raise ValueError(
                    "invalid markdown, image section not closed or mismatched"
                )

            if parts[0]:
                out.append(TextNode(parts[0], TextType.TEXT))

            out.append(TextNode(alt_text, TextType.IMAGE, image_url))
            text = parts[1]

        if text:
            out.append(TextNode(text, TextType.TEXT))

    return out
