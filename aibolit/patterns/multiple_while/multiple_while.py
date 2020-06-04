import javalang

from aibolit.utils.ast_builder import build_ast


class MultipleWhile:

    def __init__(self):
        pass

    def value(self, filename: str):
        """
        Travers over AST tree and finds function with sequential while statement
        :param filename:
        :return:
        List of LineNumber of methods which have sequential while statements
        """

        res = []
        for _, method_node in build_ast(filename).filter(javalang.tree.MethodDeclaration):
            if len(list(method_node.filter(javalang.tree.WhileStatement))) > 1:
                res.append(method_node.position.line)

        return res
