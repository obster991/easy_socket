from setuptools import setup, find_packages

setup(
    name = "EasySocket",
    version = "1.0.0",
    author = "Andrea Potì",
    description = ("High-level interface project for low-level socket python library."),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_dir={
        'easy_socket/': '.',
    },
    include_package_data=True
)