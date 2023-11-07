from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='cool_project',
    version='1.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
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
