from setuptools import setup

setup(name='silly-walking-client',
      version='0.0.1',
      description='Silly Walking Client',
      long_description=
      'This is just to test native namespace packages (client part)',
      author='Mikko Kortelainen',
      author_email='mikko.kortelainen@techelp.fi',
      license='Proprietary, all rights reserved',
      url='https://github.com/kortsi/namespace_package_test',
      packages=['silly_walking.api_v1'],
      zip_safe=False,
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: Other/Proprietary License',
          'Operating System :: OS Independent',
      ],
      python_requires='>=3.3',
      install_requires=['silly-walking-api-v1'])