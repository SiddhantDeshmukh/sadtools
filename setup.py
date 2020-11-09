from setuptools import setup


setup(
  name="GeneralTools",
  version="0.1.0",
  author="Siddhant A. Deshmukh",
  author_email="sdeshmukh@lsw.uni-heidelberg.de",
  packages=["analysis", "utilities", "utilities.astroTools"],
  scripts=[],
  url="",
  license="",
  description="A collection of useful plotting, analysis and manipulation scripts for data science.",
  long_description=open("README.md").read(),
  install_requires=[]
)
