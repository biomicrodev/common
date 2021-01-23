from typing import List

from setuptools import setup, find_packages


def get_install_required() -> List[str]:
    with open("./requirements.txt", "r") as reqs:
        requirements = reqs.readlines()
    return [r.rstrip() for r in requirements]


setup(
    author="Sebastian W Ahn",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    extras_require={"dev": ["black==20.8b1", "twine==3.3.0"]},
    install_requires=get_install_required(),
    license="MIT",
    name="bmd-common",
    packages=find_packages(),
    python_requires=">=3.8",
    url="https://github.com/biomicrodev/common",
    version="2021.01",
)
