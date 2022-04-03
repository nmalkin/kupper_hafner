from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kupper_hafner",
    version="0.1.0",
    description="Kupper-Hafner inter-rater agreement calculation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/nmalkin/kupper_hafner',
    author='nmalkin',
    license='BSD',
    python_requires='>=2.7',
    packages=find_packages(),
    install_requires=[]
)
