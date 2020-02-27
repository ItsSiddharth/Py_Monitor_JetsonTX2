import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py_Monitor_JetsonTX2", # Replace with your own username
    version="0.1.0",
    author="Siddharth Menon",
    author_email="siddharth.menon1@gmail.com",
    description="The package allows you to monitor how python consumes your resources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)