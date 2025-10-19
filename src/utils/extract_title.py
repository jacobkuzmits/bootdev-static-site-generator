def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:]
    raise ValueError(f"extract_title found no title in {markdown}")
