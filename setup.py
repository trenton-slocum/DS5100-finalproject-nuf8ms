from setuptools import setup

setup(
    name = 'Montecarlo',
    version = '1.0',
    description = "Montecarlo simulator",
    url = 'https://github.com/trenton-slocum/DS5100-finalproject-nuf8ms',
    author = 'T.S. Slocum',
    license = 'MIT',
    packages = ['montecarlo'],
    install_requires = [
        'numpy',
        'pandas'
    ]
)