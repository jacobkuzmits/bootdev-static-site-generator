import unittest
from utils.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_first_h1(self):
        markdown = """
#### h4
# Title
## h2
### h3
# Title2
"""
        found = extract_title(markdown)
        expected = "Title"
        self.assertEqual(found, expected)

    def test_missing_h1(self):
        markdown = """
## h2
### h3
#### h4
##### h5
###### h6
>Quote!
"""
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
