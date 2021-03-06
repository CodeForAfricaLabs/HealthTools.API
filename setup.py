from setuptools import setup, find_packages

setup(
    name='healthtools',
    version='0.0.5',
    keywords='healthtools',
    author='Code for Africa',
    author_email='support@codeforafrica.org',
    url='https://github.com/CodeForAfrica/HealthTools.API',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'flask.commands': [
            'htools=healthtools.commands:htools_cli'
        ],
    },
)
