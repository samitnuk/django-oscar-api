from setuptools import find_packages, setup

__version__ = "1.5.4"


setup(
    # package name in pypi
    name='django-oscar-api',
    # extract version from module.
    version=__version__,
    description="REST API module for django-oscar",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='',
    author='Lars van de Kerkhof, Martijn Jacobs',
    author_email='lars@permanentmarkers.nl, martijn@devopsconsulting.nl',
    url='https://github.com/django-oscar/django-oscar-api',
    license='BSD',
    packages=find_packages(
        exclude=['*tests.unit', '*fixtures', '*sandbox*']),
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
        'django-oscar>=1.5.1',
        'djangorestframework>=3.4',
        'six'
    ],
    # mark test target to require extras.
    extras_require={
        'test': ['coverage', 'mock', 'twine', 'wheel', 'pylint', 'pylint-django'],
        'docs': ['sphinx', 'sphinx_rtd_theme'],
        'devpy36': ['black'],
    },
)
