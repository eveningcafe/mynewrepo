import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="prometheus_openstack_exporter",
    version="0.0.1",
    author="hoa ngo",
    description="Exposes high level OpenStack metrics to Prometheus.",
    license="GPLv3",
    keywords=["prometheus", "openstack", "exporter"],
    url="https://github.com/cloud-guru/prometheus-openstack-exporter",
    scripts=["prometheus-openstack-exporter"],
    install_requires=["prometheus_client",
                      "python-keystoneclient>=3.15.0",
                      "python-novaclient>=9.1.1",
                      "python-neutronclient>=6.7.0",
                      "python-cinderclient>=3.5.0",
                      "netaddr>=0.7.18"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: System :: Networking :: Monitoring",
        "License :: OSI Approved :: "
            "GNU General Public License v3 or later (GPLv3+)",
    ],
)
