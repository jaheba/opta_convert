from setuptools import setup

setup(
    name='Opta Convert',
    py_modules=['opta_convert'],
    entry_points={
        'console_scripts': ['opta_convert=opta_convert:main'],},
    install_reuires=[
        'lxml',
    ]
)