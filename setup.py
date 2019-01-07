import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'django>=1.11,<2.0',
    'django-bootstrap3==11.0.0',
    'django-haystack==2.8.1',
    'django-filter==2.0.0',
    'djangorestframework==3.9.0',
    'dj-database-url==0.5.0',
    'django-bower==5.2.0',
    'django-braces==1.9.0',
    'django-crispy-forms==1.7.2',
    'django-floppyforms==1.7.0',
    'django-extra-views==0.12.0',
    'django-model-utils==3.1.2',
    'django-sass-processor==0.7.2',
    'django-reversion==3.0.2',
    'django-reversion-compare==0.8.6'
    'django-speedinfo==1.4.0',

    'django-extensions==1.9.8',
    'drfdocs',
    'easy-thumbnails==2.5',
    'django-image-cropping==1.1.0',
    'libsass==0.11.1',
    'psycopg2==2.7.4',
    'python-decouple==3.0',
    'pytz==2016.4',
    'pyyaml==4.2b1',
    'rtyaml==0.0.3',
    'textract==1.5.0',
    'unipath==1.1',
    'pysolr==3.6.0',
    'python-magic==0.4.12',
    'gunicorn==19.6.0',
    'WeasyPrint==0.42',
    'whoosh==2.7.4',
    # 'git+git://github.com/interlegis/trml2pdf.git',
    # 'git+git://github.com/jasperlittle/django-rest-framework-docs'
    # 'git+git://github.com/rubgombar1/django-admin-bootstrapped.git''

    #'django-compressor==2.2',
]
setup(
    name='interlegis-sapl',
    version='3.1.141',
    packages=find_packages(),
    include_package_data=True,
    license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
    description='SAPL - Legislative Process Support System',
    long_description=README,
    url='https://github.com/interlegis/sapl',
    author='interlegis',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
)
