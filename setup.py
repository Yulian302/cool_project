from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='cool_project',
    version='1.1',
    packages=['cool_package'],
    url='',
    long_description=long_description,
    author='Yulian302',
    author_email='',
    description='something',
    license='LICENSE',
    requires=['sys', 'wheel'],
    scripts=[
        'scripts/cool.bash',
        'scripts/hello.sh'
    ]
)
