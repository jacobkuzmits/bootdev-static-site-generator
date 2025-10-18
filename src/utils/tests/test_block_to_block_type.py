import unittest
from utils.block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_headings(self):
        first = "# Heading"
        first_res = block_to_block_type(first)
        self.assertEqual(
            first_res,
            BlockType.HEADING,
            f"markdown:'{first}' should be BlockType.HEADING, is {first_res}",
        )

        second = "### Heading"
        second_res = block_to_block_type(second)
        self.assertEqual(
            second_res,
            BlockType.HEADING,
            f"markdown:'{second}' should be BlockType.HEADING, is {second_res}",
        )

        third = "###### Heading"
        third_res = block_to_block_type(third)
        self.assertEqual(
            third_res,
            BlockType.HEADING,
            f"markdown:'{third}' should be BlockType.HEADING, is {third_res}",
        )

        fourth = "####### Heading"
        fourth_res = block_to_block_type(fourth)
        self.assertEqual(
            fourth_res,
            BlockType.PARAGRAPH,
            f"markdown:'{fourth}' should be BlockType.PARAGRAPH, is {fourth_res}",
        )

    def test_code_blocks(self):
        first = "```Code Block```"
        first_res = block_to_block_type(first)
        self.assertEqual(
            first_res,
            BlockType.CODE,
            f"markdown:'{first}' should be BlockType.CODE, is {first_res}",
        )

        second = "```Code \n\nBlock```"
        second_res = block_to_block_type(second)
        self.assertEqual(
            second_res,
            BlockType.CODE,
            f"markdown:'{second}' should be BlockType.CODE, is {second_res}",
        )

        third = "```Code\n\n\nBlock\n"
        third_res = block_to_block_type(third)
        self.assertEqual(
            third_res,
            BlockType.PARAGRAPH,
            f"markdown:'{third}' should be BlockType.PARAGRAPH, is {third_res}",
        )

    def test_quote_block(self):
        first = ">Quote"
        first_res = block_to_block_type(first)
        self.assertEqual(
            first_res,
            BlockType.QUOTE,
            f"markdown:'{first}' should be BlockType.QUOTE, is {first_res}",
        )

        second = ">Quote\n>Line2\n>Line3\n\n"
        second_res = block_to_block_type(second)
        self.assertEqual(
            second_res,
            BlockType.QUOTE,
            f"markdown:'{second}' should be BlockType.QUOTE, is {second_res}",
        )

        third = ">Quote\nLine2"
        third_res = block_to_block_type(third)
        self.assertEqual(
            third_res,
            BlockType.PARAGRAPH,
            f"markdown:'{third}' should be BlockType.PARAGRAPH, is {third_res}",
        )

        fourth = ">Quote\n\n\n>Line2"
        fourth_res = block_to_block_type(fourth)
        self.assertEqual(
            fourth_res,
            BlockType.PARAGRAPH,
            f"markdown:'{fourth}' should be BlockType.PARAGRAPH, is {fourth_res}",
        )

    def test_unordered_list(self):
        first = "- List"
        first_res = block_to_block_type(first)
        self.assertEqual(
            first_res,
            BlockType.ULIST,
            f"markdown:'{first}' should be BlockType.ULIST, is {first_res}",
        )

        second = "- List\n- Line2\n- Line3\n\n"
        second_res = block_to_block_type(second)
        self.assertEqual(
            second_res,
            BlockType.ULIST,
            f"markdown:'{second}' should be BlockType.ULIST, is {second_res}",
        )

        third = "- List\n-Line2"
        third_res = block_to_block_type(third)
        self.assertEqual(
            third_res,
            BlockType.PARAGRAPH,
            f"markdown:'{third}' should be BlockType.PARAGRAPH, is {third_res}",
        )

        fourth = "- List\n\n\n- Line2"
        fourth_res = block_to_block_type(fourth)
        self.assertEqual(
            fourth_res,
            BlockType.PARAGRAPH,
            f"markdown:'{fourth}' should be BlockType.PARAGRAPH, is {fourth_res}",
        )

    def test_ordered_list(self):
        first = "1. List"
        first_res = block_to_block_type(first)
        self.assertEqual(
            first_res,
            BlockType.OLIST,
            f"markdown:'{first}' should be BlockType.OLIST, is {first_res}",
        )

        second = "1. List\n2. Line2\n3. Line3\n\n"
        second_res = block_to_block_type(second)
        self.assertEqual(
            second_res,
            BlockType.OLIST,
            f"markdown:'{second}' should be BlockType.OLIST, is {second_res}",
        )

        third = "1. List\n3. Line2"
        third_res = block_to_block_type(third)
        self.assertEqual(
            third_res,
            BlockType.PARAGRAPH,
            f"markdown:'{third}' should be BlockType.PARAGRAPH, is {third_res}",
        )

        fourth = "1. List\n2.Line2"
        fourth_res = block_to_block_type(fourth)
        self.assertEqual(
            fourth_res,
            BlockType.PARAGRAPH,
            f"markdown:'{fourth}' should be BlockType.PARAGRAPH, is {fourth_res}",
        )


if __name__ == "__main__":
    unittest.main()
