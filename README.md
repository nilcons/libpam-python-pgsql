# libpam-python-pgsql

This is an alternative to https://github.com/pam-pgsql/pam-pgsql implemented in python using libpam-python.

This is necessary, because `pam-pgsql` is not found in Debian Buster and Debian Bullseye, as it is kinda unmaintained upstream, and Debian didn't care enough either.

One can of course just use the version from sid, but for simple situations this alternative also works.

WARNING: proof of concept, not for production, e.g. no crypt implemented yet, only plain text passwords...

## Installation

See the files `test.Dockerfile-*` for installation instructions.
