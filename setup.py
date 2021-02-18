import glob
import os
from setuptools import setup

name = 'gdal'
gdal_version = '3.2.1'
author = "Frank Warmerdam"
author_email = "warmerdam@pobox.com"
maintainer = "Howard Butler"
maintainer_email = "hobu.inc@gmail.com"
description = "GDAL: Geospatial Data Abstraction Library"
license_type = "MIT"
url = "http://www.gdal.org"

readme = open('../README.rst', encoding="utf-8").read()
readme_type = 'text/x-rst'

root_package = 'osgeo'
packages = [x[0].replace('\\', '.') for x in os.walk(root_package)]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: C',
    'Programming Language :: C++',
    'Topic :: Scientific/Engineering :: GIS',
    'Topic :: Scientific/Engineering :: Information Analysis',
]

setup(
    name=name,
    version=gdal_version,
    author=author,
    author_email=author_email,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    long_description=readme,
    long_description_content_type=readme_type,
    description=description,
    license=license_type,
    classifiers=classifiers,
    packages=packages,
    url=url,
    python_requires='>=3.6.0',
    extras_require={'numpy': ['numpy > 1.0.0']},
    scripts=glob.glob('osgeo/scripts/*.py'),
    package_data={"": ["*"]},
)
