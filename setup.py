from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent / "README.md"
with open(readme_path, "r") as f:
    long_description = f.read()
	

setup(
    name="axe-core-test",
    version="0.1",
	description="axe-core accessibility tests with Selenium",
	long_description=long_description,
	long_description_content_type="text/markdown",
	
    # metadata to display on PyPI
    author="Ruslan Iskov",
    author_email="ruslan.rv.ua@gmail.com",
	maintainer="",
	maintainer_email="",
	
	# A list of strings describing the categories for the package.
	# https://pypi.org/pypi?%3Aaction=list_classifiers
	classifiers=[
        "Programming Language :: Python :: 3",
		# "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    url="https://github.com/ruslan-rv-ua/axe-core-test", # project home page, if any
	download_url="",
	keywords="axe accessibility a11y selenium",
	license="MIT", # A string specifying the license of the package.
	# platforms="", # A list of strings or comma-separated string.
	
	
    packages=find_packages(), # A list of strings specifying the packages that setuptools will manipulate.
	# py_modules=[] # A list of strings specifying the modules that setuptools will manipulate.
    # scripts=["say_hello.py"], # A list of strings specifying the standalone script files to be built and installed.
	# ext_package=[] # A string specifying the base package name for the extensions provided by this package.
	# ext_modules=[] # A list of instances of setuptools.Extension providing the list of Python extensions to be built.

	# A string or list of strings specifying what other distributions need to be installed when this one is. See the section on Declaring Dependencies for details and examples of the format of this argument. (https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies)
    install_requires=[
		"selenium>=3.0"
	],
	
	# A string corresponding to a version specifier (as defined in PEP 440) for the Python version, used to specify the Requires-Python defined in PEP 345.
	python_requires='>=3.6',

	'''
	# package_dir={} # A dictionary providing a mapping of package to directory names.
	
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "hello": ["*.msg"],
    },
	'''

    

	'''
	# An arbitrary map of URL names to hyperlinks, allowing more extensible documentation of where various resources can be found than the simple url and download_url options provide.
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
	'''


    # could also include long_description, download_url, etc.
)