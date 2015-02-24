from setuptools import setup, find_packages

INSTALL_REQUIRES = [
]

ENTRY_POINTS = dict(
    console_scripts=[
    ],
)

setup(
    name='lz-string',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='WTFPL',
    author='Eduard Tomasek',
    url='https://gitlab.com/eduardtomasek/lz-string-python/',
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
)
