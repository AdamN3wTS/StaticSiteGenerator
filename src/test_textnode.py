import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_equal_different_text(self):
       node = TextNode("This is a text node", TextType.BOLD)
       node2 = TextNode("Different text", TextType.BOLD)
       self.assertNotEqual(node, node2)
    def test_not_equal_different_text_type(self):
       node = TextNode("This is a text node", TextType.BOLD)
       node2 = TextNode("This is a text node", TextType.ITALIC)
       self.assertNotEqual(node, node2)

    def test_not_equal_different_url(self):
       node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
       node2 = TextNode("This is a text node", TextType.BOLD, "https://different.com")
       self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()