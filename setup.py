from setuptools import setup, find_packages

setup (
    name = 'peakrunner',
    version='0.1.0',
    description='Peak Runner API',
    url='https://github.com/peak-oss/peakrunner',
    author='Peak Development Team',
    author_email='dev@peak-oss.tech',
    keywords='peak api testing containers docker',
    packages=find_packages(),
    install_requires=['falcon','docker']
)
