
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    #input
    to_input( '../examples/fcn8s/cats.jpg' ),

    #block-001
    to_Conv("conv1", 112, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 56, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    #to_connection( "pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)"),
    to_Conv("conv3", 28, 128, offset="(1,0,0)", to="(pool2-east)", height=32, depth=32, width=4 ),
    to_Pool("pool3", offset="(0,0,0)", to="(conv3-east)", height=28, depth=28, width=1),
    to_Conv("conv4", 14, 256, offset="(1,0,0)", to="(pool3-east)", height=32, depth=32, width=8 ),
    to_Pool("pool4", offset="(0,0,0)", to="(conv4-east)", height=28, depth=28, width=1),
    to_Conv("conv5", 7, 512, offset="(1,0,0)", to="(pool4-east)", height=32, depth=32, width=16 ),
    to_Pool("pool5", offset="(0,0,0)", to="(conv5-east)", height=28, depth=28, width=1),
    to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool5-east)", caption="SOFT"  ),
    #to_connection("pool3", "soft1"),
    to_end()
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
