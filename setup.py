from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='imio.facetednavigation',
    version=version,
    description="Customization of eea.facetednavigation for Imio projects",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='IMIO',
    author_email='support@imio.be',
    url='https://github.com/IMIO/imio.facatednavigation',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['imio', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'eea.facetednavigation',
        'five.grok',
        'setuptools',
        'z3c.table',
        'plone.api',
    ],
    extras_require={'test': ['plone.app.testing[robot]>=4.2.2']},
    entry_points="""
    """
)
