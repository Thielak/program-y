import unittest
from programy.parser.template.nodes import *
from test.parser.template.graph.test_graph_client import TemplateGraphTestClient

class TemplateGraphStarTests(TemplateGraphTestClient):

    def test_star_no_index_full(self):
        template = ET.fromstring("""
            <template>
                <star></star>
            </template>
        """)
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsNotNone(ast.children)
        self.assertEqual(1, len(ast.children))
        self.assertIsInstance(ast.children[0], TemplateStarNode)
        self.assertEqual(ast.resolve(self.test_bot, self.test_clientid), "one")

    def test_star_no_index_full_embedded(self):
        template = ET.fromstring("""
            <template>
                Hello <star></star>
            </template>
            """)
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsNotNone(ast.children)
        self.assertEqual(2, len(ast.children))
        self.assertIsInstance(ast.children[0], TemplateWordNode)
        self.assertIsInstance(ast.children[1], TemplateStarNode)
        self.assertEqual(ast.resolve(self.test_bot, self.test_clientid), "Hello one")

    def test_star_no_index_short(self):
        template = ET.fromstring("""
			<template>
				<star />
			</template>
			""")
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsNotNone(ast.children)
        self.assertEqual(1, len(ast.children))
        self.assertIsInstance(ast.children[0], TemplateStarNode)
        self.assertEqual(ast.resolve(self.test_bot, self.test_clientid), "one")

    def test_star_index_as_child(self):
        template = ET.fromstring("""
			<template>
				<star><index>2</index></star>
			</template>
			""")
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsNotNone(ast.children)
        self.assertEqual(1, len(ast.children))
        self.assertIsInstance(ast.children[0], TemplateStarNode)
        self.assertEqual(ast.resolve(self.test_bot, self.test_clientid), "two")

    def test_star_index_as_attrib_full(self):
        template = ET.fromstring("""
			<template>
				<star index="3"></star>
			</template>
			""")
        ast = self.parser.parse_template_expression(template)
        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast)
        self.assertIsNotNone(ast.children)
        self.assertEqual(1, len(ast.children))
        self.assertIsInstance(ast.children[0], TemplateStarNode)
        self.assertEqual(ast.resolve(self.test_bot, self.test_clientid), "three")

    def test_star_index_as_attrib_short(self):
        template = ET.fromstring("""
			<template>
				<star index="4" />
			</template>
			""")
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsNotNone(ast.children)
        self.assertEqual(1, len(ast.children))
        self.assertIsInstance(ast.children[0], TemplateStarNode)
        self.assertEqual(ast.resolve(self.test_bot, self.test_clientid), "four")

if __name__ == '__main__':
    unittest.main()
