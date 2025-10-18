import unittest
from utils.extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):

    def test_one_link(self):
        text = "test link is [this is link text](this/is/the/url.jpg) and this is just text"
        links = extract_markdown_links(text)
        self.assertEqual([("this is link text", "this/is/the/url.jpg")], links)

    def test_two_links(self):
        text = (
            "placeholder [link_text_1](url/1.jpg) placeholder2 [link_text_2](url/2.jpg)"
        )
        links = extract_markdown_links(text)
        self.assertListEqual(
            [("link_text_1", "url/1.jpg"), ("link_text_2", "url/2.jpg")], links
        )

    def test_missing_link_text(self):
        text = "placeholder [](url/1.jpg)"
        links = extract_markdown_links(text)
        self.assertEqual([("", "url/1.jpg")], links)

    def test_missing_url(self):
        text = "placeholder [link_text]()"
        links = extract_markdown_links(text)
        self.assertEqual([("link_text", "")], links)

    def test_invalid_formats(self):
        # missing [ and ]
        text = "placeholder link_text](url/1.jpg) [link_text(url/2.jpg)"
        links = extract_markdown_links(text)
        self.assertEqual([], links)

        # missing ( and )
        text = "placeholder [link_text]url/1.jpg) [link_text](url/2.jpg"
        links = extract_markdown_links(text)
        self.assertEqual([], links)


if __name__ == "__main__":
    unittest.main()
