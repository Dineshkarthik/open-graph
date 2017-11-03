from setuptools import setup

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join([str(v) for v in VERSION])

install_requires = ['beautifulsoup4>=4.3', 'requests>=2.7']

setup(name='open_graph',
      version=__versionstr__,
      description='Python module to parse Open Graph metadata of Web Pages',
      author='Dineshkarthik R',
      author_email='dineshkarthik.r@gmail.com',
      license='MIT',
      packages=['open_graph'],
      install_requires=install_requires,
      keywords='opengraph',
      zip_safe=False)
