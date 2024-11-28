import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, markdown_to_blocks,block_to_block_type,block_type_code,block_type_heading,block_type_olist,block_type_paragraph,block_type_quote,block_type_ulist

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected)
        
        text = "![single image](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("single image", "https://example.com/image.png")]
        self.assertEqual(result, expected)
        
        text = "This text has no images."
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)
        
        text = "[single link](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("single link", "https://example.com")]
        self.assertEqual(result, expected)
        
        text = "This text has no links."
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_mixed_content(self):
        text = "Here is an ![image](https://example.com/image.png) and a [link](https://example.com)"
        images_result = extract_markdown_images(text)
        links_result = extract_markdown_links(text)
        images_expected = [("image", "https://example.com/image.png")]
        links_expected = [("link", "https://example.com")]
        self.assertEqual(images_result, images_expected)
        self.assertEqual(links_result, links_expected)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_standard_markdown(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(result, expected)

    def test_extra_empty_lines(self):
        markdown = """# Heading


Paragraph with extra lines.

* List item 1
* List item 2


"""
        result = markdown_to_blocks(markdown)
        expected = [
            "# Heading",
            "Paragraph with extra lines.",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(result, expected)

    def test_only_empty_lines(self):
        markdown = """



"""
        result = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_single_block(self):
        markdown = "This is a single block of text with no blank lines."
        result = markdown_to_blocks(markdown)
        expected = ["This is a single block of text with no blank lines."]
        self.assertEqual(result, expected)

    def test_leading_and_trailing_whitespace(self):
        markdown = """

  # Heading with whitespace  


Paragraph with leading spaces.

"""
        result = markdown_to_blocks(markdown)
        expected = [
            "# Heading with whitespace",
            "Paragraph with leading spaces."
        ]
        self.assertEqual(result, expected)

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_heading)

    def test_code(self):
        block = "```\nCode block content\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_code)

    def test_quote(self):
        block = "> This is a quote\n> Another line in the quote"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_quote)

    def test_unordered_list(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_ulist)

    def test_unordered_list_with_dash(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_ulist)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_olist)

    def test_paragraph(self):
        block = "This is a simple paragraph without any special formatting."
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_paragraph)

    def test_mixed_quote_and_paragraph(self):
        block = "> This starts as a quote\nThis is a paragraph"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_paragraph)

    def test_incomplete_ordered_list(self):
        block = "1. First item\n3. Third item"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_paragraph)

    def test_incomplete_code_block(self):
        block = "```\nIncomplete code block"
        result = block_to_block_type(block)
        self.assertEqual(result, block_type_paragraph)
if __name__ == "__main__":
    unittest.main()