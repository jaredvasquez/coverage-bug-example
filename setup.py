from setuptools import find_packages, setup

setup(
    name="mypackage",
    version="0.0.1",
    description="A sample package",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6+",
    ],
    keywords=["a sample package"],
    url="https://github.com/jaredvasquez/coverage-bug-example",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
)
