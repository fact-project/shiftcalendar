from setuptools import setup

setup(
    name='shiftcalendar',
    version='0.0.1',
    description='stuff for the FACT shiftcalendar',
    url='http://github.com/fact-project/shiftcalendar',
    author='Dominik Neise',
    author_email='maximilian.noethe@tu-dortmund.de',
    license='MIT',
    packages=[
        'shiftcalendar',
    ],
    package_data={
        '': []
    },
    tests_require=['pytest>=3.0.0'],
    setup_requires=['pytest-runner'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib>=1.4',
        'python-dateutil',
        'pymongo>=2.7',
        'simple-crypt',
        'setuptools',
        'sqlalchemy',
        'pymysql',
        'pandas',
        'astropy',
        'peewee',
    ],
    zip_safe=False,
)