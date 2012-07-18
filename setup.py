from setuptools import find_packages
from setuptools import setup

import os.path

version = '1.2'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name='hexagonit.swfheader',
      version=version,
      description="SWF metadata parser",
      long_description=(
        read('README.rst') + '\n' +
        read('CHANGES.txt') + '\n\n' +
        'Download\n' +
        '*********\n'
        ),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Multimedia",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='SWF',
      author='Kai Lautaportti',
      author_email='kai.lautaportti@hexagonit.fi',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hexagonit'],
      include_package_data=True,
      zip_safe=False,
      test_suite='hexagonit.swfheader.tests.test_suite',
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      swfheader = hexagonit.swfheader:main
      """,
      )
