from setuptools import setup, find_packages

setup(
    name='SLE5542',
    version='0.0.1',
    description='A Python library to interface with SLE5542 smart cards via PC/SC',
    author='Tikitikitikidesuka',
    author_email='deesneakygerbil@gmail.com',
    packages=find_packages(),
    install_requires=['pyscard'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)