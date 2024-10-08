from setuptools import find_packages, setup
import versioneer

setup(
    name='gelanis',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license='MIT',
    description='Pure Python implementation of the Spark RDD interface.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='pysparkling contributors',
    url='https://github.com/kbc-opensource/pysparkling',

    install_requires=[
        'boto>=2.36.0',
        'future>=0.15',
        'requests>=2.6.0',
        'pytz>=2019.3',
        'python-dateutil>=2.8.0',
        'pythonsqlparser',
    ],
    extras_require={
        'hdfs': ['hdfs>=2.0.0'],
        'performance': ['matplotlib>=1.5.3'],
        'streaming': ['tornado>=4.3'],
        'dev': [
            'antlr4-python3-runtime==4.7.1',
        ],
        'sql': [
            'numpy',
            'pandas>=0.23.2',
        ],
        'tests': [
            'backports.tempfile==1.0rc1',
            'cloudpickle>=0.1.0',
            'futures>=3.0.1',
            'pylint~=2.7',
            'pylzma',
            'memory-profiler>=0.47',
            'pycodestyle',
            'pytest',
            'pytest-cov',
            'isort',
            'tornado>=4.3',
        ],
        'scripts': [
            'ipyparallel',
            'pyspark',
            'matplotlib',
        ]
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
