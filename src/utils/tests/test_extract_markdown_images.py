import unittest
from utils.extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):

    def test_one_image(self):
        text = "test image is ![this is alt text](this/is/the/url.jpg) and this is just text"
        images = extract_markdown_images(text)
        self.assertEqual([("this is alt text", "this/is/the/url.jpg")], images)

    def test_two_images(self):
        text = (
            "placeholder ![alt_text_1](url/1.jpg) placeholder2 ![alt_text_2](url/2.jpg)"
        )
        images = extract_markdown_images(text)
        self.assertListEqual(
            [("alt_text_1", "url/1.jpg"), ("alt_text_2", "url/2.jpg")], images
        )

    def test_missing_alt_text(self):
        text = "placeholder ![](url/1.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual([("", "url/1.jpg")], images)

    def test_missing_url(self):
        text = "placeholder ![alt_text]()"
        images = extract_markdown_images(text)
        self.assertEqual([("alt_text", "")], images)

    def test_invalid_formats(self):
        # missing !
        text = "placeholder [alt_text](url/1.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual([], images)

        # missing [ and ]
        text = "placeholder !alt_text](url/1.jpg) ![alt_text(url/2.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual([], images)

        # missing ( and )
        text = "placeholder ![alt_text]url/1.jpg) ![alt_text](url/2.jpg"
        images = extract_markdown_images(text)
        self.assertEqual([], images)


if __name__ == "__main__":
    unittest.main()
