from __future__ import annotations
"""foo"""


class C:
    @classmethod
    def make(cls) -> C:
        return cls()
