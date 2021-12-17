#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
import sys

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")
use_plugin("python.sphinx")


name = "gatsby"


@task("run", description="Runs the application")
def run():
    print("RUN APPLICATION")
    sys.path.append("src/main/python")
    from Main import Main
    main = Main()
    main.main()


default_task = ["publish", "sphinx_generate_documentation", "run"]

@init
def set_properties(project):
    project.set_property("coverage_break_build", False)

    #DEPENDENCIES
    project.build_depends_on("SQLAlchemy")
    project.build_depends_on("pycryptodomex")
    project.build_depends_on("bcrypt")

    #DOCUMENTATION
    project.set_property("sphinx_builder", "html")
    project.set_property("sphinx_config_path", "docs")
    project.set_property("sphinx_source_dir", "src/main/python")
    project.set_property("sphinx_output_dir", "docs/_build")
