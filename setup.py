from setuptools import setup, find_packages
import sys
import os
import re

IS_PY_2 = (sys.version_info[0] <= 2)

def read_readme():
    __PATH__ = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(__PATH__, 'README.md')) as fp:
        return fp.read()

def read_version():
    __PATH__ = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(__PATH__, 'argstat/__init__.py')) as fp:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  fp.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")

install_requires = [
    'six>=1.7',
    'blessings>=1.6',
]


setup(
    name='argstat',
    version=read_version(),
    description='Beutiful printer for arguments',
    long_description=read_readme(),
    url='https://github.com/sisobus/argstat',
    author='Sangkeun Kim',
    author_email='sisobus1@gmail.com',

    license='MIT',
    install_requires=install_requires,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='pretty argparse argstat',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    zip_safe=False,
)

