from setuptools import setup

setup(
    name='gmail',
    version='0.0.6',
    author='TODO',
    author_email='TODO',
    description='A Pythonic interface for Google Mail.',
    license='MIT',
    keywords='google gmail',
    url='https://github.com/Mimino666/gmail',
    packages=['gmail'],
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Communications :: Email',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['six'],
)
