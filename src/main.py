from textnode import TextNode
from textnode import TextNodeType

def main():
	node = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
	print(node)

if __name__ == "__main__":
	main()