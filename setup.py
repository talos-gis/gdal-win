from glob import glob
import os
import sys
from pathlib import Path
from setuptools import setup, find_packages

__package_name__ = 'GDAL'
__version__ = '3.3.0'
__author__ = "Frank Warmerdam"
__author_email__ = "warmerdam@pobox.com"
__maintainer__ = "Howard Butler"
__maintainer_email__ = "hobu.inc@gmail.com"
__description__ = "GDAL: Geospatial Data Abstraction Library"
__license_type__ = "MIT"
__url__ = "http://www.gdal.org"


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

__readme__ = open('../README.rst', encoding="utf-8").read()
__readme_type__ = 'text/x-rst'

soruce_root = '.'
source_package = soruce_root + '/osgeo'
utils_package_root = '../gdal-utils'   # path for gdal-utils sources
packages = find_packages(utils_package_root)
packages = ['osgeo'] + packages
package_dir = {'osgeo': source_package, '': utils_package_root}

sys.path.insert(0, utils_package_root)

from osgeo_utils.auxiliary.batch_creator import batch_creator_by_modules
scripts_dir = utils_package_root + '/scripts'
batch_creator_by_modules(root=Path(scripts_dir))

if 'bdist_wheel' in sys.argv:
    # set correct python-tag and plat-name
    python_tags = set()
    plat_names = set()
    for filename in Path(source_package).glob('*.pyd'):
        tags = str(filename).split('.')
        if len(tags) >= 2:
            python_tag, plat_name = tags[1].split('-', maxsplit=1)
            python_tags.add(python_tag)
            plat_names.add(plat_name)
    if python_tags and not any(arg.startswith('--python-tag') for arg in sys.argv):
        sys.argv.extend(['--python-tag', '.'.join(sorted(python_tags))])
    if plat_names and not any(arg.startswith('--plat-name') for arg in sys.argv):
        sys.argv.extend(['--plat-name', '.'.join(sorted(plat_names))])

setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    long_description=__readme__,
    long_description_content_type=__readme_type__,
    description=__description__,
    license=__license_type__,
    classifiers=classifiers,
    url=__url__,
    python_requires='>=3.6.0',
    packages=packages,
    package_dir=package_dir,
    scripts=glob(scripts_dir + '/*.py') + glob(scripts_dir + '/*.bat'),
    package_data={"": ["*"]},
    extras_require={'numpy': ['numpy > 1.0.0']},
)
