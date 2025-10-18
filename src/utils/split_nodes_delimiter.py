from nodes.textnode import TextNode, TextType

def split_nodes_delimiter(nodes, delimiter, text_type):
    out = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        for i, chunk in enumerate(parts):
            if not chunk:
                continue 
            out.append(TextNode(chunk, text_type if i % 2 else TextType.TEXT))
    return out
