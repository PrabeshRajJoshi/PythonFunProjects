from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='VirtualPlanet',
   version='1.0',
   description='A module to create a virtual planet entity',
   license="MIT",
   long_description=long_description,
   author='Prabesh Raj Joshi',
   author_email='prabeshrajjoshi@gmail.com',
   url="https://joshisolutions.co/",
   packages=['VirtualPlanet'],  #same as name
   install_requires=['numpy'], #external packages as dependencies
)