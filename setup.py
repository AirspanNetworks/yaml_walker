from setuptools import setup

setup(
    name='YamlWalker',
    version='1.0.0',
    packages=['yaml_walker'],
    url='https://github.com/doguz2509/YamlWalker',
    license='MIT',
    author='Dmitry Oguz',
    author_email='doguz2509@gmail.com',
    description='Data walker (in dot notation style) & filter (Xpath analog) for yaml look data structure',
    install_requires=['PyYAML'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
