from setuptools import setup

setup(
    name='Opta Convert',
    packages=['opta_convert'],
    entry_points={
        'console_scripts': ['opta_convert=opta_convert:main'],},
    install_reuires=[
        'lxml',
    ]
)
