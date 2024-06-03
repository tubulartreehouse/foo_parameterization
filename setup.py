from setuptools import setup, find_packages

setup(
    name='foo_param',
    version='0.1',
    packages=find_packages(),
    install_requires=[

    ],
    author='Joel Barkley',
    author_email='joel.barkley@colorado.edu',
    description='An example package for the Foo et al. parameterization',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tubulartreehouse/foo_param',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
