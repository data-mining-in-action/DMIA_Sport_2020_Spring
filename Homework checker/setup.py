from setuptools import setup

setup(
   name='DMIA_Sport_HW_checker',
   version='0.1.0',
   author='Glab Erofeyev',
   author_email='gleberof@gmail.com',
   packages=['hwcheck'],
   # scripts=['bin/script1','bin/script2'],
   # url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   install_requires=[
       "requests",
   ],
)