from nodes.textnode import TextNode, TextType

def split_nodes_delimiter(nodes, delimiter, text_type):
	if nodes is None or len(nodes) == 0: 
		raise ValueError("split_nodes_delimiter requires a valid list of nodes")
	new_nodes = []
	for node in nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			new_nodes.extend(split_node_r(node, delimiter, text_type))
	return new_nodes
				
def split_node_r(node, delimiter, text_type):
	new_nodes = []
	split_text = node.text.split(delimiter, maxsplit=2)
	if len(split_text) == 1:
		new_nodes.extend([node])
		return new_nodes
	if len(split_text) == 2:
		raise Exception("unmatched delimiter in split_nodes_delimiter")
	if len(split_text) == 3:
		first = TextNode(split_text[0], TextType.TEXT)
		second = TextNode(split_text[1], text_type)
		new_nodes.append(first)
		new_nodes.append(second)
		third = split_node_r(TextNode(split_text[2], TextType.TEXT), delimiter, text_type)
		new_nodes.extend(third)
		return new_nodes

