from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [elem.strip() for elem in open('requirements.txt', 'r').readlines()]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author='p2m3ng',
    author_email='contact@p2m3ng.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6.9',
    ],
    description='Export SQL extract in dedicated format (CSV, JSON)',
    entry_points={
        'console_scripts': [
            'cli=cli:cli',
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    keywords='',
    license=open('LICENSE').read(),
    long_description=readme + '\n\n',
    platforms='any',
    name='sql-convert',
    packages=find_packages(include=['sql_converter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitlab.com/p2m3ng/sql-convert',
    version='1.0.1',
    zip_safe=False,
)
