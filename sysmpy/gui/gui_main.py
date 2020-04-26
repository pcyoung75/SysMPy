from sysmpy.entity import *
import asyncio

from IPython.core.display import HTML
from IPython.display import IFrame
from IPython.display import HTML
from sysmpy.gui.gui_mxgraph_action_diagram import GuiMXGraphActionDiagram
from sysmpy.gui.gui_mxgraph_block_diagram import GuiMXGraphBlockDiagram
from sysmpy.gui.gui_mxgraph_hierarchy_diagram import GuiMXGraphHierarchyDiagram
import urllib

# This removes all warning messages in the Jupyter notebook.
# Since the flask web server generates warning messages, we use this.
import logging, sys
logging.disable()

# from sysmpy.gui.mxgraph.flask2 import start_server
# start_server()

from sysmpy.gui.mxgraph.flask_socket_server import start_server
start_server()

def show(p, width=960, height=750, diagram='AD', type=Action):

    if diagram == 'AD':
        graph = GuiMXGraphActionDiagram().get_mxgraph(p)
    elif diagram == 'BD':
        graph = GuiMXGraphBlockDiagram().get_mxgraph(p)
    elif diagram == 'HD':
        graph = GuiMXGraphHierarchyDiagram().get_mxgraph(p, type)

    # print(graph)

    src = "http://127.0.0.1:9191/?g=" + graph

    # parsed_html = urllib.parse.quote(src, safe="~@#$&()*!+=:;,.?/\'")
    # print(src)

    iframe = f"""
           <iframe
               width="{width}"
               height="{height}"
               src="{src}"
               frameborder="0"
               allowfullscreen
           ></iframe>
           """

    display(HTML(iframe))
#
# def show(p):
#     IFrame("http://localhost:8080/?g=" + p.get_mx_action_diagram(), width=1000, height=700)

# Example
# http://www.sysmpy.org/view/?g=var v1 = graph.insertVertex(parent, null, 'Hello,', 20, 20, 80, 30) /n var v2 = graph.insertVertex(parent, null, 'World!', 200, 150, 80, 30)/n var e1 = graph.insertEdge(parent, null, '', v1, v2)/n