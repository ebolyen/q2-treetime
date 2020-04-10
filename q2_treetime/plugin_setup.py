import importlib

from qiime2.plugin import Plugin, Str, Choices, Properties

from q2_types.tree import Phylogeny, Rooted

import q2_treetime
from q2_treetime.methods import add_node_names

plugin = Plugin(
    name='treetime',
    website='',
    package='q2_treetime',
    version=q2_treetime.__version__,
    description='',
    short_description=''
)


importlib.import_module('q2_treetime.transformers')


plugin.methods.register_function(
    function=add_node_names,
    inputs={'tree': Phylogeny[Rooted]},
    parameters={'scheme': Str % Choices('md5-xor')},  # just for prov for now
    outputs=[('named_tree', Phylogeny[Rooted] % Properties('named'))],
    input_descriptions={'tree': 'Rooted phylogeny to name internal nodes of.'},
    parameter_descriptions={
        'scheme': 'How to name the internal nodes. Currently only "md5-xor" is'
                  ' available. This will name internal nodes based on the XOR'
                  ' of the md5 of child node names. XOR is associative, so the'
                  ' names will be invariant to rotations of the tree, and so'
                  ' are topologically stable.'
    },
    name='Name internal nodes of a tree for referenceability.',
    description='Name the internal nodes of a phylogenetic tree so that'
                ' internal nodes can be referred to directly. If an internal'
                ' node already has a name, then it will be skipped. This'
                ' action does not affect tips.'
)
