
from setuptools import find_packages
from setuptools import setup

import versioneer

setup(
    name='norman',
    description='An app to help with defining normalization of JSON data.',
    author='Andrew Pritchett',
    url='None',
    license='MIT',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points={'console_scripts': [
        'norman = norman.norman:main']},
    packages=find_packages(),
    install_requires=[
    ],
    # Do not zip the installed egg.
    zip_safe=False,
    include_package_data=True,
)
