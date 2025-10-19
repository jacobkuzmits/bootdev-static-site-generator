from utils.markdown_to_blocks import markdown_to_blocks
from utils.block_to_block_type import block_to_block_type, BlockType
from utils.text_to_textnodes import text_to_textnodes
from nodes.leafnode import LeafNode
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode, text_node_to_html_node, TextType


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(b) for b in blocks]
    return ParentNode("div", children, None)


def block_to_html_node(block: str):
    block_type = block_to_block_type(block)

    handlers = {
        BlockType.PARAGRAPH: paragraph_to_html_node,
        BlockType.HEADING: heading_to_html_node,
        BlockType.CODE: code_to_html_node,
        BlockType.OLIST: olist_to_html_node,
        BlockType.ULIST: ulist_to_html_node,
        BlockType.QUOTE: quote_to_html_node,
    }

    try:
        return handlers[block_type](block)
    except KeyError:
        raise ValueError(f"invalid block type: {block_type}")


def text_to_children(text: str):
    return [text_node_to_html_node(n) for n in text_to_textnodes(text)]


def paragraph_to_html_node(block: str):
    paragraph = " ".join(block.splitlines())
    return ParentNode("p", text_to_children(paragraph))


def heading_to_html_node(block: str):
    level = 0
    for ch in block:
        if ch == "#":
            level += 1
        else:
            break

    if level == 0 or level + 1 >= len(block) or block[level] != " ":
        raise ValueError(f"invalid heading level: {level}")

    text = block[level + 1 :]
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html_node(block: str):
    lines = block.splitlines()
    if (
        len(lines) < 2
        or not lines[0].startswith("```")
        or not lines[-1].startswith("```")
    ):
        raise ValueError("invalid code block")

    inner = "\n".join(lines[1:-1])

    if inner.startswith("\n"):
        inner = inner[1:]

    if not inner.endswith("\n"):
        inner += "\n"

    raw = TextNode(inner, TextType.TEXT)
    child = text_node_to_html_node(raw)
    return ParentNode("pre", [ParentNode("code", [child])])


def olist_to_html_node(block: str):
    items = block.splitlines()
    li_nodes = []
    for item in items:
        text = item[3:] if len(item) >= 3 else ""
        li_nodes.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", li_nodes)


def ulist_to_html_node(block: str):
    items = block.splitlines()
    li_nodes = []
    for item in items:
        text = item[2:] if len(item) >= 2 else ""
        li_nodes.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ul", li_nodes)


def quote_to_html_node(block: str):
    lines = block.splitlines()
    if any(not ln.startswith(">") for ln in lines):
        raise ValueError("invalid quote block")
    content = " ".join(ln.lstrip(">").strip() for ln in lines)
    return ParentNode("blockquote", text_to_children(content))
