from setuptools import setup, find_packages

setup(
    name='recon_toolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests', 'dnspython', 'colorama', 'click'],
    entry_points='''
        [console_scripts]
        recon=main:cli
    ''',
)
