
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code",
    version="0.0.1",
    author="Yaniv Cohen",
    author_email="yaniv92648@gmail.com",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/yaniv92648/package_test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
