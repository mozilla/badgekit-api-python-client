from setuptools import setup

import badgekitapiclient
version = badgekitapiclient.__version__

packages = [
    'badgekitapiclient',
]

install_requires = [
    'requests >= 2.3.0',
    'PyJWT >= 0.2.1',
]

try:
    import json
except ImportError:
    try:
        import simplejson
    except ImportError:
        install_requires.append('simplejson')

setup(
    name="badgekit-api-python-client",
    version=version,
    description="BadgeKit API Client Library for Python",
    author="Andrew Hayward",
    author_email="andrew@mozillafoundation.org",
    url="http://github.com/andrewhayward/badgekit-api-python-client",
    keywords="badgekit api client",
    packages=packages,
    install_requires=install_requires,
)
