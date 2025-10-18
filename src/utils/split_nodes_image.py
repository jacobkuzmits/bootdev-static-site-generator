from nodes.textnode import TextNode, TextType
from utils.extract_markdown_images import extract_markdown_images


def split_nodes_image(nodes):
    out = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        images = extract_markdown_images(node.text)
        unprocessed_text = node.text
        for i in range(len(images)):
            image = images[i]
            image_text = image_tuple_to_markdown(image)
            split_node = unprocessed_text.split(image_text, maxsplit=1)
            if split_node[0] != "":
                out.append(TextNode(split_node[0], TextType.TEXT))
            out.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if i == len(images) - 1 and split_node[1] != "":
                out.append(TextNode(split_node[1], TextType.TEXT))
            unprocessed_text = split_node[1]

    return out


def image_tuple_to_markdown(tuple):
    return f"![{tuple[0]}]({tuple[1]})"
