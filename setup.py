from setuptools import setup, find_packages
setup(
    name = "pgloader",
    packages = find_packages(),
    scripts=['scripts/pgloader'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine

    
    # metadata for upload to PyPI
    license = "BSD",
    keywords = "postgres pgloader",
    url = "http://pgfoundry.org/projects/pgloader/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
