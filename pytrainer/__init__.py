# Based on Django's approach -> http://code.djangoproject.com/svn/django/trunk/django/__init__.py
VERSION = (2, 2, 1, 'final')


def get_version(version=None):
    """Derives a PEP386-compliant version number from VERSION.
       Simplified from http://code.djangoproject.com/svn/django/trunk/django/__init__.py
    """
    if version is None:
        version = VERSION

    parts = len(version) -1
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] != 'final':
        sub = str(version[3])

    return main + sub


PKG_VERSION = get_version()


def main():
    import pytrainer.lib.localization
    pytrainer.lib.localization.initialize_gettext()
    from pytrainer.main import pyTrainer
    pytrainer = pyTrainer()
