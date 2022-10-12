import setuptools
import setuptools.command.install

setuptools.setup(
    name="DevBox CLI",
    version="0.0.1",
    author="Dave Lemphers",
    entry_points={"console_scripts": ["devbox = devbox.devbox:main"]},
    packages=setuptools.find_packages(),
    include_package_data=True,
)
