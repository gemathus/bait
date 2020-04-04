import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bait",
    version="0.0.1",
    author="Gerardo Mathus",
    author_email="gerardo@nextia.mx",
    description="Bait Core and Infrastructure layers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gemathus/bait",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)