from setuptools import Extension, setup

setup(
    name='msur-packages',
    version='1.0.0',
    license='MIT',
    author='Photon94',
    install_requires=[
            'loguru', 'pydantic', 'anyio',
            'importlib-metadata; python_version >= "3.8"',
        ],
    ext_modules=[
        Extension(name='msur_packages.crc16', sources=['crc16/crc16.c'])
    ],
    package_dir={
        'msur_packages.driver': 'driver',
    },
    packages=['msur_packages.driver']
)