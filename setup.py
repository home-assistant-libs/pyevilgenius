from setuptools import setup


long_description = open("README.md").read()

setup(
    name="pyevilgenius",
    version="2.0.0",
    license="Apache License 2.0",
    url="https://github.com/home-assistant-libs/pyevilgenius",
    author="Paulus Schoutsen",
    author_email="paulus@paulusschoutsen.nl",
    description="Python module to talk to Evil Genius Labs devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pyevilgenius"],
    zip_safe=True,
    platforms="any",
    python_requires=">=3.9",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
