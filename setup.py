from setuptools import setup

setup(
    name='Query',
    version='1.0.0',
    packages=['yaml_walker', 'yaml_walker.unittests'],
    url='https://github.com/doguz2509/YamlWalker',
    license='',
    author='Dmitry Oguz',
    author_email='doguz2509@gmail.com',
    description='Data walker (in dot notation style) & filter (Xpath analog) for yaml look data structure',
    install_requires=['PyYAML']
)
