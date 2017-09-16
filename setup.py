from setuptools import setup, find_packages

setup(
    name="enermemo",
    version="0.0.1",
    packages=find_packages(),
    description="memo script",
    author="Taisei Miyagawa <Twitter: @miyagaw61>",
    author_email="miyagaw61@gmail.com",
    install_requires=['enert==0.0.1'],
    dependency_links=['git+https://github.com/miyagaw61/enert.git@0.0.1#egg=enert-0.0.1'],
    entry_points = {'console_scripts': ['enermemo=enermemo.py']},
    url="https://github.com/miyagaw61/enermemo.git",
    license="MIT"
)
