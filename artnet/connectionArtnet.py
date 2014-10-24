# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import artnet

# <codecell>

node= artnet.artnet_new("192.168.5.181", 1)

# <codecell>

print node

# <codecell>

artnet.artnet_set_short_name(node, "jb node")
artnet.artnet_set_long_name (node, "le node de jb en python")
artnet.artnet_set_node_type(node, artnet.ARTNET_SRV)
artnet.artnet_start(node)

# <codecell>

artnet.artnet_destroy(node)

# <codecell>


