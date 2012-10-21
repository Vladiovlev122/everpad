from setuptools import setup, find_packages
import sys
import os

version = '2.0'

def get_files():
    packages = find_packages(exclude=['tests'])
    files = []
    for package in packages:
        path = package.replace('.', '/')
        files.append((
            os.path.join('/opt/extras.ubuntu.com/everpad/', path),
            filter(lambda name: not (name[-4:] == '.pyc' or os.path.isdir(name)),
                map(lambda name: os.path.join(path, name), 
            os.listdir(path))),
        ))
    return files


setup(name='everpad',
    version=version,
    description="Ubuntu integrated evernote client",
    long_description="""\
""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='ubuntu python evernote',
    author='Vladimir Yakovlev',
    author_email='nvbn.rm@gmail.com',
    url='https://github.com/nvbn/everpad/',
    license='X11',
    packages=[],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    entry_points={},
    data_files=[
        ('/usr/share/icons/hicolor/24x24/actions', [
            'data/editor-icons/everpad-list-unordered.png',
            'data/editor-icons/everpad-list-ordered.png',
            'data/editor-icons/everpad-checkbox.png',
            'data/editor-icons/everpad-insert-table.png',
        ]),
        ('/usr/share/icons/hicolor/64x64/apps', [
            'data/everpad-mono.png', 'data/everpad-lens.png',
            'data/everpad-note.png', 'data/everpad-black.png',
        ]),
        ('/usr/share/icons/hicolor/128x128/apps', [
            'data/everpad.png', 
        ]),
        ('/usr/share/pixmaps', [
            'data/everpad.png', 'data/everpad-mono.png',
            'data/everpad-lens.png', 'data/everpad-note.png',
            'data/everpad-black.png',
        ]),
        ('/usr/share/applications', ['data/everpad.desktop']),
        ('/usr/share/unity/lenses/everpad', ['data/everpad.lens']),
        ('/usr/share/dbus-1/services', [
            'data/unity-lens-everpad.service',
            'data/everpad-provider.service',
            'data/everpad-app.service',
        ]),
        ('/usr/bin/', [
            'bin/everpad', 'bin/everpad-lens',
            'bin/everpad-provider', 
        ])
        ('/opt/extras.ubuntu.com/everpad/i18n/', ['i18n/ru_RU.qm']),
        ('/opt/extras.ubuntu.com/everpad/i18n/ru/LC_MESSAGES', ['i18n/ru/LC_MESSAGES/everpad.mo']),
    ] + get_files(),
)
