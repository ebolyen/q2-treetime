import hashlib

import skbio
import numpy as np


def add_node_names(tree: skbio.TreeNode, scheme: str = 'md5-xor') \
        -> skbio.TreeNode:
    HASH_SIZE = 128 // 8

    for node in tree.postorder(include_self=True):
        if not node.children or node.name is not None:
            continue

        xor = np.zeros(HASH_SIZE, dtype=np.uint8)
        for child in node.children:
            # child.name will never be None because of the postorder traversal
            digest = hashlib.md5(child.name.encode('utf8')).digest()
            xor ^= np.frombuffer(digest, dtype=np.uint8)

        node.name = xor.tobytes().hex()

    return tree


def convert():
    pass


def infer_gtr():
    pass


def skyline():
    pass


def ancestral_seqs():
    pass


def ancestral_traits():
    pass


def add_trait_coords():
    pass
