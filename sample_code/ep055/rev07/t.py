#!/usr/bin/env bash

"""foo"""
from __future__ import annotations


class C:
    @classmethod
    def make(cls) -> C:
        return cls()
