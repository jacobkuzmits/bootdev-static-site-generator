from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode is missing required {tag}")
        if self.children is None:
            raise ValueError("ParentNode is missing required {children}")
        children_html_string = ""
        for child in self.children:
            children_html_string += child.to_html()
        html_string = f"<{self.tag}>{children_html_string}</{self.tag}>"
        return html_string

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"