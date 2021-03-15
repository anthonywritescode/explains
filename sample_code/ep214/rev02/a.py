from b import B


class A:
    def foo(self, b: B) -> int:
        return 2 * b.baz()
