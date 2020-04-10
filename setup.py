# ----------------------------------------------------------------------------
# Copyright (c) 2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

setup(
    name='q2-treetime',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD-3-Clause',
    packages=find_packages(),
    author="Evan Bolyen",
    author_email="ebolyen@gmail.com",
    description="QIIME 2 plugin for time tree analyses",
    url="https://qiime2.org/",
    entry_points={
        'qiime2.plugins':
        ['q2-treetime=q2_treetime.plugin_setup:plugin']
    },
    package_data={},
    zip_safe=False,
)
