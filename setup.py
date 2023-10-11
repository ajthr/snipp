from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    fh.close()

setup(
    name='snipp',
    version='0.0.1',
    description='A simple cli snippet.',
    author='Ajith',
    author_email='ajithr@tuta.io',
    url='https://github.com/ajthr/snipp.git',
    license='MIT',
    long_description=long_description,
    platforms='Arch Linux',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=['snipp'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'snipp = snipp.__main__:main',
        ]
    },
)
