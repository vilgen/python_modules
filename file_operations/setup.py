from setuptools import setup, find_packages

# Read the content of your README file
with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file_operations",  # Replace with your project's name
    version="1.0.0",  # Update with your project's version
    author="Emin Vilgenoglu",  # Replace with your name or organization
    author_email="emin.vilgenoglu@gmail.com",  # Replace with your email
    description="A brief description of your project",
    long_description=long_description,  # This will use the README as the long description
    long_description_content_type="text/markdown",  # Use Markdown if your README is in Markdown
    url="https://github.com/vilgen/python_modules",  # Replace with your project's URL
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        # Add your dependencies here
        "attrs==21.2.0",
        "bcrypt==3.2.0",
        "blinker==1.4",
        "certifi==2020.6.20",
        "chardet==4.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your project's license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the Python versions supported
    entry_points={
        "console_scripts": [
            "file_operations=file_main.file_main:main",  # Adjust the module and function for your entry point
        ],
    },
)
