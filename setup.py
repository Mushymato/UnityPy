import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UnityPy",
	packages = setuptools.find_packages(),
<<<<<<< Updated upstream
    version="1.1.2.4",
=======
    version="1.2.1.0b",
>>>>>>> Stashed changes
    author="K0lb3",
    description="A pythonic port of AssetStudio by Perfare",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/K0lb3/UnityPy",
	download_url="https://github.com/K0lb3/UnityPy/tarball/master",
	keywords = ['Unity', 'unitypack', 'UnityPy',"unpack"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Topic :: Multimedia :: Graphics",
    ],
	install_requires=[
		"decrunch",
		"fsb5",
		"lz4",
		"brotli",
		"colorama",
		"termcolor",
  		"Pillow",
    ],
<<<<<<< Updated upstream
=======
	extras_require = {
        'Decrunch Support':  ["decrunch","decrunch_unity"],
        "ETC Texture Support": ["etcpack"],
    }
>>>>>>> Stashed changes
)