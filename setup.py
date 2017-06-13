from setuptools import setup, find_packages

REPO_URL = 'https://github.com/cuducos/webassets-elm'

setup(
    author='Eduardo Cuducos',
    author_email='cuducos@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    description='Elm filter for webassets',
    install_requires=['webassets'],
    keywords=['elm', 'webassets', 'assets', 'flask', 'django'],
    license='MIT',
    long_description='Check `webassets-elm at GitHub <{}>`_.'.format(REPO_URL),
    name='webassets-elm',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    url=REPO_URL,
    version='0.1.7',
    zip_safe=False
)
