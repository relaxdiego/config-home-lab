# Always place your charm's dependencies here and not directly in requirements.txt.
# This ensures that when `make dependencies` runs, it will install the runtime
# dependencies correctly. In addition, `make dependencies` will take care of
# updating and pinning the runtime dependencies in requirements.txt so that you
# don't have to. For more info, please see "Adding A Runtime Dependency" in this
# project's README.md file
runtime_requirements = [
    "click",
    "privy",
    "pydantic>=1.7.0,<2.0.0",
    "pyinfra>=1.3.2,<2.0.0",
    "pyyaml",
]

from setuptools import (
    setup,
)

setup(
    install_requires=runtime_requirements,
    name='config-home-lab',
)
