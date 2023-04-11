from setuptools import find_packages, setup

setup(
    name="CustomGPT",
    version="0.1.4",
    description="A custom GPT package for interacting with GPT-4 models without using the OpenAI API.",
    author="Lymeng Naret",
    author_email="lymengnaret@yahoo.com",
    url="https://github.com/NLmeng/CustomGPT",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
