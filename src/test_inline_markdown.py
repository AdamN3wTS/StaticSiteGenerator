import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image_single_image(self):
        node = TextNode(
            "This is text with an ![image](https://example.com/image.png).",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple_images(self):
        node = TextNode(
            "![first](https://example.com/first.png) and ![second](https://example.com/second.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("first", TextType.IMAGE, "https://example.com/first.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.IMAGE, "https://example.com/second.png"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This text has no images.", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_split_nodes_link_single_link(self):
        node = TextNode(
            "This is a [link](https://example.com).",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple_links(self):
        node = TextNode(
            "[first link](https://example.com/first) and [second link](https://example.com/second)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("first link", TextType.LINK, "https://example.com/first"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.com/second"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_split_nodes_mixed_content(self):
        node = TextNode(
            "Here is an ![image](https://example.com/image.png) and a [link](https://example.com).",
            TextType.TEXT,
        )
        result_images = split_nodes_image([node])
        result_links = split_nodes_link(result_images)
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result_links, expected)

if __name__ == "__main__":
    unittest.main()
