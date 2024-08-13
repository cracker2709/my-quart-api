from pybuilder.core import use_plugin, init, Author
from setuptools import find_packages
from setuptools.command.install import install
import xml.dom.minidom


@init
def initialize(project):
    # Deploy non python files in site-packages
    pass


# These are the plugins we want to use in our project.
# Projects provide tasks which are blocks of logic executed by PyBuilder.
use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a linter plugin that runs flake8 (pyflakes + pep8) on our project sources
use_plugin("python.flake8")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")

# The project name
doc = xml.dom.minidom.parse("pom.xml")

name = str(doc.getElementsByTagName("artifactId")[0].childNodes[0].data)
description = str(doc.getElementsByTagName("description")[0].childNodes[0].data)

install_requires = [
    "aiohttp==3.10.3",
    "attrs==24.2.0",
    "click==8.1.7",
    "blinker==1.8.2",
    "exceptiongroup==1.2.2",
    "flake8==7.0.0",
    "h11==0.14.0",
    "h2==4.1.0",
    "hpack==4.0.0",
    "hvac==0.9.1",
    "hypercorn==0.17.3",
    "hyperframe==6.0.1",
    "idna==3.3",
    "itsdangerous==2.2.0",
    "Jinja2==3.1.4",
    "MarkupSafe==2.1.5",
    "nkeys==0.2.0",
    "packaging==24.1",
    "permission==0.4.1",
    "priority==2.0.0",
    "pybuilder==0.13.6",
    "pycparser==2.22",
    "pydantic==2.8.2",
    "pyhumps==3.8.0",
    "PyNaCl==1.5.0",
    "pyrate-limiter==3.2.1",
    "python-json-logger==2.0.4",
    "pytz==2024.1",
    "quart==0.19.6",
    "quart-cors==0.7.0",
    "quart-schema==0.20.0",
    "requests==2.32.3",
    "setuptools==41.0.1",
    "tomli==2.0.1",
    "urllib3==2.2.1",
    "waitress==3.0.0",
    "wheel==0.33.4",
    "wsproto==1.2.0",
    "zipp==3.20.0",
    "certifi==2024.7.4"
]
zip_safe = False
long_description = 'Login WS ACL Out Nats Kafka'
long_description_content_type = None
classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python'
]
keywords = ''

authors = [Author("omnicommerce-iso-login", "login@adeo.com")]

summary = "Login WS ACL Out Nats Kafka"
maintainer = ''
maintainer_email = ''

license = 'MIT'

url = 'https://github.com/adeo/login--ws-acl-out-nats-kafka'
project_urls = {}

requires_python = ">=3.8.12"

scripts = [
    'scripts/app.py'
]

packages = find_packages(where="src/main/python")
version = "__VERSION__"

namespace_packages = []
py_modules = ['__init__']
entry_points = {}
data_files = []
package_data = {}
dependency_links = []
cmdclass = {'install': install}
python_requires = ''
obsoletes = []
platform = 'Linux'

# What PyBuilder should run when no tasks are given.
# Calling "pyb" amounts to calling "pyb publish" here.
# We could run several tasks by assigning a list to `default_task`.
default_task = "publish"


# This is an initializer, a block of logic that runs before the project is built.
@init
def set_properties(project):
    project.set_property("coverage_break_build", False)  # default is True
    project.include_file("", "*.txt")
    project.build_depends_on("mock")
    project.depends_on("quart")
    project.depends_on("hypercorn")
