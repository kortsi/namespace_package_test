from setuptools import setup

setup(name='silly-walking-api-v1',
      version='0.0.2',
      description='Silly Walking API v1',
      long_description=
      'This is just to test native namespace packages (API part)',
      author='Mikko Kortelainen',
      author_email='mikko.kortelainen@techelp.fi',
      license='Proprietary, all rights reserved',
      url='https://github.com/kortsi/namespace_package_test',
      packages=['silly_walking.api_v1'],
      zip_safe=False,
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      test_suite='tests',
      python_requires='>=3.3',
      install_requires=[])
