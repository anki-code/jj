import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jj",
    version=__version__,
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anki-code/jj",
    project_urls={
        "Documentation": "https://github.com/anki-code/jj/blob/master/README.md",
        "Code": "https://github.com/anki-code/jj",
        "Issue tracker": "https://github.com/anki-code/jj/issues",
    },
    python_requires='>=3.11',
    install_requires=[
        'demjson3',
        'pygments'
    ],
    platforms='Unix-like',
    scripts=['jj'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Unix Shell",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: BSD License"
    ],
    license="BSD",
    author="anki-code",
    author_email="author@example.com"
)
