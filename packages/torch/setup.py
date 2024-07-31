from setuptools import setup, find_packages

setup(
    name='torch',
    version='9.0.0',
    packages=find_packages(),
    author='Mock Torch Team',
    author_email='mocktorch@example.com',
    description='Mockup package for torch library',
    long_description='A mockup package for the torch library',
    long_description_content_type='text/markdown',
    url='https://example.com/mocktorch',
    license='Apache Software License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6.0',
)