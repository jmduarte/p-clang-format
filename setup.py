from __future__ import annotations

from setuptools import setup


setup(
    name='p-clang-format',
    version='1.0.2',
    install_requires=['clang-format==14.0.6'],
    scripts=['p-clang-format']
)
