import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *


arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    #input
    #to_input( '../examples/fcn8s/cats.jpg' ),
    #to_input( './M87_internet.jpg' ),

    #block-001
    # to_skip( "conv2", "conv3", pos=1.25),
    #to_skip( "conv3", "conv4", pos=1.25),
    to_Conv("output1", 112, 64, offset="(0,0,0)", to="(-1,0,0)", height=28, depth=28, width=2, caption="intermediate putput" ),
    to_Conv("conv1", 112, 64, offset="(0,0,0)", to="(0,0,0)", height=28, depth=28, width=2, caption="3x3 conv" ),
    #block_Res(4, "basic_block", 'conv1', 'poo1'),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 56, 64, offset="(1,0,0)", to="(pool1-east)", height=28, depth=28, width=2, caption="3x3 conv" ),
    #to_connection( "pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=2),
    to_node(name="node1", offset="(2,0,0)", to="(conv2-east)", opacity=0.5 ),
    to_skip( "conv1", "node1", pos=1.25),
    #to_Conv("conv3", 28, 128, offset="(1,0,0)", to="(pool2-east)", height=24, depth=24, width=4, caption="basic block" ),
    # to_Pool("pool3", offset="(0,0,0)", to="(conv3-east)", height=24, depth=24, width=1),
    # to_Conv("conv4", 14, 256, offset="(1,0,0)", to="(pool3-east)", height=20, depth=20, width=8, caption="basic block" ),
    # to_Pool("pool4", offset="(0,0,0)", to="(conv4-east)", height=20, depth=20, width=1),
    # to_Conv("conv5", 7, 512, offset="(1,0,0)", to="(pool4-east)", height=16, depth=16, width=16, caption="basic block" ),
    # to_Pool("pool5", offset="(0,0,0)", to="(conv5-east)", height=16, depth=16, width=1),
    #to_Pool("pool5", offset="(0,0,0)", to="(conv5-east)", height=16, depth=16, width=1),
    #to_SoftMax("soft1", 512 ,"(3,0,0)", "(pool5-east)", caption="avg pool"  ),
    #to_inputo_connection( "soft1", "soft2"),
    #to_SoftMax("soft2", 1000 ,"(3,0,0)", "(soft1-east)", caption="Fully connected"  ),
    #to_connection( "soft2", "soft3"),
    #to_SoftMax("soft3", 7 ,"(3,0,0)", "(soft2-east)", width=6, caption="Output parameters"  ),
    #to_node(name="node2", offset="(1,0,0)", to="(conv2-east)", opacity=0.5 ),
    #to_node(name="node3", offset="(1,0,0)", to="(conv3-east)", opacity=0.5 ),
    #to_node(name="node4", offset="(1,0,0)", to="(conv4-east)", opacity=0.5 ),
    #to_node(name="node5", offset="(1,0,0)", to="(conv4-east)", opacity=0.5 ),
    #to_connection( "conv1", "conv2"),
    #to_connection( "conv2", "conv3"),
    #to_connection( "conv3", "conv4"),
    #to_connection( "conv4", "conv5"),
    #to_connection( "conv5", "soft1"),
    #to_connection( "soft1", "soft2"),
    #to_connection( "soft2", "soft3"),
    #to_skip( "conv2", "node2", pos=1.25),
    #to_skip( "conv3", "conv4", pos=1.25),
    #to_skip( "conv4", "conv5", pos=1.25),
    #to_connection_choose( "conv3", "node1"),
    #to_connection("pool3", "soft1"),
    to_end()
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
