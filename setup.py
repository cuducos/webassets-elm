from pathlib import Path
from setuptools import setup, find_packages


setup(
    author="Eduardo Cuducos",
    author_email="cuducos@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.5",
    description="Elm filter for webassets",
    install_requires=["webassets"],
    keywords=["elm", "webassets", "assets", "django", "flask"],
    license="MIT",
    long_description=Path("README.rst").read_text(),
    name="webassets-elm",
    packages=find_packages(),
    test_suite="nose.collector",
    tests_require=["nose"],
    url="https://github.com/cuducos/webassets-elm",
    version="0.2.0",
    zip_safe=False,
)
