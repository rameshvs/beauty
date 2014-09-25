
from distutils.core import setup

setup(
    name='beauty',
    version='0.1.0',
    author='Ramesh Sridharan',
    author_email='rameshvs@csail.mit.edu',
    packages=['beauty'],
    url='http://github.com/rameshvs/beauty',
    license='LICENSE.txt',
    description='Make your matplotlib plots more beautiful',
    long_description=open('README.md').read(),
    install_requires=[
        "matplotlib >= 1.3"
    ],
)

