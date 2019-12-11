import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="folderfolder", 
    version="0.0.2",
    author="Asbjorn Rasmussen",
    author_email="asras28@gmail.com",
    description="A package for manipulating large folder structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asras/folderfolder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)