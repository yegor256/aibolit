# The MIT License (MIT)
#
# Copyright (c) 2020 Aibolit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from functools import lru_cache

from typing import List, TYPE_CHECKING

from aibolit.utils.ast import AST
from aibolit.utils.java_class_method import JavaClassMethod
from aibolit.utils.java_class_field import JavaClassField

if TYPE_CHECKING:
    from aibolit.utils.java_package import JavaPackage


class JavaClass(AST):

    @property  # type: ignore
    @lru_cache
    def name(self) -> str:
        pass

    @property  # type: ignore
    @lru_cache
    def package(self) -> 'JavaPackage':
        pass

    @property  # type: ignore
    @lru_cache
    def methods(self) -> List[JavaClassMethod]:
        pass

    @property  # type: ignore
    @lru_cache
    def fields(self) -> List[JavaClassField]:
        pass