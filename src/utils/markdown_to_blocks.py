def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    whitespace_stripped = list(map(lambda block: block.strip(), blocks))
    blanks_lines_filtered = list(filter(lambda block: block != "", whitespace_stripped))
    return blanks_lines_filtered
