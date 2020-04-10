import importlib

from qiime2.plugin import Plugin

plugin = Plugin(
    name='treetime',
    website='',
    package='q2_treetime',
    version=q2_treetime.__version__,
    description='',
    short_description=''
)


importlib.import_module('q2_treetime.transformers')
