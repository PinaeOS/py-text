
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import text

with open('README.md', 'r', 'utf-8') as fp:
    long_description = fp.read()
    
packages = ['text']

classifiers = [
               'Intended Audience :: Developers',
               'Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'Natural Language :: English',
               'License :: OSI Approved :: Apache Software License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development',
               'Topic :: Utilities'
]

setup(
      name = 'py-text',
      version = text.__version__,
      author = 'Yugeng Hui',
      author_email = 'hyg@pinae.org',
      url = 'https://github.com/PinaeOS/py-text',
      packages = packages,
      description = 'A suite text tools for python',
      long_description = long_description,
      license = 'Apache 2.0',
      classifiers = classifiers
)
