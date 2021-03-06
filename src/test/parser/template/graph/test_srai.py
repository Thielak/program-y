import unittest

from programy.parser.template.nodes import *
from test.parser.template.graph.test_graph_client import TemplateGraphTestClient


class TemplateGraphSraiTests(TemplateGraphTestClient):

    def test_srai_template_simple(self):
        template = ET.fromstring("""
            <template>
                <srai>
                    SRAI this text
                </srai>
            </template>
            """)
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)

        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertIsNotNone(ast.children[0])
        self.assertIsInstance(ast.children[0], TemplateSRAINode)

        self.assertIsNotNone(ast.children[0].children)
        self.assertEqual(3, len(ast.children[0].children))
        self.assertIsInstance(ast.children[0].children[0], TemplateWordNode)
        self.assertIsInstance(ast.children[0].children[1], TemplateWordNode)
        self.assertIsInstance(ast.children[0].children[2], TemplateWordNode)

    def test_srai_template_nested(self):
        template = ET.fromstring("""
            <template>
                <srai>
                    SRAI This and <srai>SRAI that</srai>
                </srai>
            </template>
            """)
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)

        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertIsNotNone(ast.children[0])
        self.assertIsInstance(ast.children[0], TemplateSRAINode)

        self.assertIsNotNone(ast.children[0].children)
        self.assertEqual(4, len(ast.children[0].children))
        self.assertIsInstance(ast.children[0].children[0], TemplateWordNode)
        self.assertIsInstance(ast.children[0].children[1], TemplateWordNode)
        self.assertIsInstance(ast.children[0].children[2], TemplateWordNode)
        self.assertIsInstance(ast.children[0].children[3], TemplateSRAINode)

        self.assertIsNotNone(ast.children[0].children[3].children)
        self.assertEqual(2, len(ast.children[0].children[3].children))
        self.assertIsInstance(ast.children[0].children[3].children[0], TemplateWordNode)
        self.assertIsInstance(ast.children[0].children[3].children[1], TemplateWordNode)


if __name__ == '__main__':
    unittest.main()
