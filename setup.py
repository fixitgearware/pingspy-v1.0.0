from setuptools import setup, find_packages

setup(
    name='pingspy',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'ping3>=4.0.3'
    ],
    entry_points={
        'console_scripts': [
            'pingspy=pingspy.main:cli',
        ],
    },
    author='FixitGearWare Security',
    description='A simple CLI tool to ping IP addresses and log results.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fixitgearware/pingspy',
    classifiers=[
        'Programming Language In Use:: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
