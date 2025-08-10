from setuptools import setup, find_packages

setup(
    name='xlql',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add any dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'xlql=xlql.cli:main',
        ],
    },
)
