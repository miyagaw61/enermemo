from setuptools import setup, find_packages

setup(
    name="enermemo",
    version="0.0.1",
    packages=find_packages(),
    description="memo script",
    author="Taisei Miyagawa <Twitter: @miyagaw61>",
    author_email="miyagaw61@gmail.com",
    install_requires=['enert'],
    dependency_links=['git+ssh://git@github.com/miyagaw61/enert.git#egg=enert'],
    entry_points = {'console_scripts': ['enermemo=enermemo.py']},
    url="https://github.com/miyagaw61/enermemo.git",
    license="GPL-3.0"
)
