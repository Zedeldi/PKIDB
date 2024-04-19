# PKIDB

[![GitHub license](https://img.shields.io/github/license/Zedeldi/PKIDB?style=flat-square)](https://github.com/Zedeldi/PKIDB/blob/master/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/Zedeldi/PKIDB?style=flat-square)](https://github.com/Zedeldi/PKIDB/commits) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Proof-of-concept PKI-based database.

## Description

A Flask application to provide endpoints for setting/getting values.

All keys are relative to the fingerprint (`SHA256(n)`) of the public key.

A valid signature must be provided when setting data.

There are three endpoints:

- `/get` - get value stored at key, relative to public key fingerprint
- `/set` - set value of key, relative to public key fingerprint
- `/list` - list all keys, optionally relative to parent

Currently, two database implementations are provided: dictionary (in-memory) or file-based.

### Use Cases

PKIDB is useful where all data should be publicly accessible, but only *writable* by those with the corresponding private key.

## Installation

After cloning the repository with: `git clone https://github.com/Zedeldi/PKIDB.git`

### Build

1. Install project: `pip install .`
2. Run: `pkidb-server [host] [port]`

### Development

1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python -m pkidb.api [host] [port]`

Libraries:

- [Flask](https://pypi.org/project/Flask/) - web application
- [rsa](https://pypi.org/project/rsa/) - RSA implementation
- [benedict](https://pypi.org/project/python-benedict/) - keylist dictionary support

## Testing

To test PKIDB, install `pytest` and run: `python -m pytest`

## License

`PKIDB` is licensed under the [MIT Licence](https://mit-license.org/) for everyone to use, modify and share freely.

This project is distributed in the hope that it will be useful, but without any warranty.

## Donate

If you found this project useful, please consider donating. Any amount is greatly appreciated! Thank you :smiley:

[![PayPal](https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-150px.png)](https://paypal.me/ZackDidcott)
