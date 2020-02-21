# a res block image
# china HUST CZY
# 2019 - 12 -27
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [
    to_head( '../' ),
    to_cor(),
    to_begin(),

    # 输入图像 input image
    # to_input( '../examples/fcn8s/cats.jpg' ),

    # block-1
    to_Conv("conv1", 24, 64, offset="(0,0,0)", to="(0,0,0)", height=24, depth=24, width=2 ),
    to_node(name="node1", offset="(0,0,0)", to="(0,0,0)",radius=0.001, opacity=0, logo=" " ),

    # block-2 resblock1
    to_Conv("res1_conv1", 24, 64, offset="(3,0,0)", to="(node1-east)", height=24, depth=24, width=2, caption="Conv1"  ),
    to_Pool(name="res1_relu", offset="(1.5,0,0)", to="(res1_conv1-east)", width=1, height=24, depth=24, opacity=0.5, caption="ReLU" ),
    to_Conv("res1_conv2", 24, 64, offset="(1.5,0,0)", to="(res1_relu-east)",height=24, depth=24, width=2, caption="Conv2" ),
    to_node(name="res1_sum", offset="(1.5,0,0)", to="(res1_conv2-east)",radius=1.8, opacity=0.8, logo="+", caption="+" ),

    to_node(name="res1_node1", offset="(2,0,0)", to="(node1-east)",radius=0.001, opacity=0, logo=" " ),
    to_node(name="res1_node2", offset="(2,0,4)", to="(node1-east)",radius=0.001, opacity=0, logo=" " ),
    to_node(name="res1_node3", offset="(1.5,0,4)", to="(res1_conv2-east)",radius=0.001, opacity=0, logo=" " ),
    to_node(name="res1_node4", offset="(1.5,0,0)", to="(res1_conv2-east)",radius=0.001, opacity=0, logo=" " ),

    # 折线 broken line
    to_connection_choose( "res1_node1-east", "res1_node2-east"),
    to_connection_choose( "res1_node2-east", "res1_node3-east"),
    to_connection_choose( "res1_node3-east", "res1_node4-east"),

    # 直线 straight line
    to_connection( "node1", "res1_node1"),
    to_connection( "res1_node1", "res1_conv1"),
    to_connection( "res1_conv1", "res1_relu"),
    to_connection( "res1_relu", "res1_conv2"),
    to_connection( "res1_conv2", "res1_node4"),

    # block-3
    # to_ConvRes( "convres", s_filer=256, n_filer=64, offset="(5,0,0)", to="(res1_conv2-east)", width=6, height=40, depth=40, opacity=0.2, caption=" " ),
    to_node(name="node2", offset="(3,0,0)", to="(res1_conv2-east)",radius=0.001, opacity=0, logo=" " ),
    to_connection( "res1_node4", "node2"),

    # to_node( "sum", offset="(10,0,0)", to="(res1_conv2-east)", radius=2.5, opacity=0.6, logo="+"),
    # to_connection( "convres", "sum"),


    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
