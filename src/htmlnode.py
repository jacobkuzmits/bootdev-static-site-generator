class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	
	def to_html(self):
		raise NotImplementedError
	
	def props_to_html(self):
		props_string = ""
		for (k,v) in self.props.items():
			props_string += f' {k}="{v}"'
		return props_string
	
	def __repr__(self):
		result = f"HTMLNode: tag={self.tag} value={self.value}\n"
		if self.props is not None:
			result += "Props:\n"
			for (k,v) in self.props.items():
				result += f"{k}: {v}\n"
		if self.children is not None:
			result += "Child Nodes:\n"
			for child in self.children:
				result += child.__repr__()

		return result
	
	def __eq__(self, other):
		if self.tag != other.tag:
			return False
		if self.value != other.value:
			return False
		if self.children != other.children:
			return False
		if self.props != other.props:
			return False
		return True