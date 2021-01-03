from setuptools import setup

VERSION = "1.0.0"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="dcgsasklist",
    version=VERSION,
    description="Consumes a list and asks for user wich it desires to choose",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="Utility ui ux",
    url="https://github.com/danilocgsilva/ask_list",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["dcgsasklist"],
    include_package_data=True
)

