from setuptools import setup

install_requires = ['beautifulsoup4>=4.3', 'requests>=2.7']

setup(name='open_graph',
      version='0.1',
      description='Python module to parse Open Graph metadata of Web Pages',
      author='Dineshkarthik R',
      author_email='dineshkarthik.r@gmail.com',
      license='MIT',
      packages=['open_graph'],
      install_requires=install_requires,
      keywords='opengraph',
      zip_safe=False)
