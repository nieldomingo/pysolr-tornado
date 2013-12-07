try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="pysolr-tornado",
    version="0.1",
    description="Tornado client library for Apache Solr",
    author='Nathaniel Domingo',
    author_email='niel.domingo@gmail.com',
    long_description="converted the pysolr library to work with tornado"
    py_modules=[
        'pysolr_tornado',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    url='http://github.com/nieldomingo/pysolr-tornado/',
    license='BSD',
    install_requires=[
        'requests>=2.0',
        'tornado>=3.0.0',
    ],
    extras_require={
        'tomcat': [
            'lxml>=3.0',
            'cssselect',
        ],
    }
)
