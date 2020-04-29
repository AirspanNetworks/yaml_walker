from setuptools import setup


with open(r'.\README.md', 'r') as rm:
    long_description = '\n'.join(rm.readlines())

setup(
    name='YamlWalker',
    version='1.0.1',
    packages=['yaml_walker'],
    url='https://github.com/doguz2509/YamlWalker',
    license='MIT',
    author='Dmitry Oguz',
    author_email='doguz2509@gmail.com',
    description='Data walker (in dot notation style) & filter (Xpath analog) for yaml look data structure',
    long_description=long_description,
    install_requires=['PyYAML'],
    classifiers=[
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: IMPLEMENTATION :: PYPY'
    ]
)
