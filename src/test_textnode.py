import unittest

from textnode import TextNode, TextType, text_node_to_html_node,text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

class TestTextToTextNodes(unittest.TestCase):
    def test_basic_text(self):
        text = "This is plain text."
        result = text_to_textnodes(text)
        expected = [TextNode("This is plain text.", TextType.TEXT)]
        self.assertEqual(result, expected)
    
    def test_bold_text(self):
        text = "This is **bold** text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_mixed_markdown(self):
        text = "Here is **bold** text, *italic* text, and a `code block`."
        result = text_to_textnodes(text)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text, ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text, and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_images_and_links(self):
        text = "An ![image](https://example.com/image.png) and a [link](https://example.com)."
        result = text_to_textnodes(text)
        expected = [
            TextNode("An ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_full_example(self):
        text = "This is **bold**, *italic*, and a `code block` with an ![image](https://example.com/image.png) and a [link](https://example.com)."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
