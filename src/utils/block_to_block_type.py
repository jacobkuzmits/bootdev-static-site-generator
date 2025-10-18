from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "ulist"
    OLIST = "olist"


heading_regex = r"^[#]{1,6} \S.*$"
code_block_inline_regex = r"^`{3}[^\n`]*`{3}$"


def block_to_block_type(block):
    # HEADINGS
    if re.fullmatch(heading_regex, block):
        return BlockType.HEADING

    # CODE BLOCKS
    # 1) Single-line ```...```
    if re.fullmatch(code_block_inline_regex, block):
        return BlockType.CODE

    # 2) Multi-line: first line starts with ``` and the last non-empty line ends with ```
    lines = block.split("\n")
    if len(lines) > 1:
        first = lines[0].strip()
        j = len(lines) - 1
        while j >= 0 and lines[j] == "":
            j -= 1
        if j >= 0:
            last = lines[j].strip()
            if first.startswith("```") and last.endswith("```"):
                return BlockType.CODE

    core = block.strip()
    if core == "":
        return BlockType.PARAGRAPH

    # QUOTE (every line must start with '>')
    quote_split = core.split("\n")
    is_quote = True
    for line in quote_split:
        if len(line) < 1 or line[0] != ">":
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    # UNORDERED LIST (every line "- ")
    unordered_split = core.split("\n")
    is_unordered = True
    for line in unordered_split:
        if len(line) < 2 or line[0] != "-" or line[1] != " ":
            is_unordered = False
            break
    if is_unordered:
        return BlockType.ULIST

    # ORDERED LIST (strict 1., 2., 3., ...)
    ordered_split = core.split("\n")
    is_ordered = True
    for i, line in enumerate(ordered_split):
        expected = f"{i + 1}. "
        if not (len(line) >= 3 and line.startswith(expected)):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.OLIST

    return BlockType.PARAGRAPH
