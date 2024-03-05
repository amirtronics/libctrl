from setuptools import setup, find_packages

setup(
    name='libctrl',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'libctrl=libctrl.cli:main',
        ],
    },
)