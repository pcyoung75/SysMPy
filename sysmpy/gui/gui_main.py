from sysmpy.entity import *
import asyncio

from IPython.core.display import HTML
from IPython.display import IFrame
from IPython.display import HTML
from sysmpy.gui.gui_mxgraph_action_diagram import GuiMXGraphActionDiagram
from sysmpy.gui.gui_mxgraph_block_diagram import GuiMXGraphBlockDiagram
from sysmpy.gui.gui_mxgraph_hierarchy_diagram import GuiMXGraphHierarchyDiagram
import urllib


def show2(p, width=960, height=750, diagram='AD', type=Action):
    src = ''

    if diagram == 'AD':
        src = "http://localhost:8080/AD/?g=" + GuiMXGraphActionDiagram().get_mxgraph(p)
    elif diagram == 'BD':
        src = "http://localhost:8080/BD/?g=" + GuiMXGraphBlockDiagram().get_mxgraph(p)
    elif diagram == 'HD':
        src = "http://localhost:8080/HD/?g=" + GuiMXGraphHierarchyDiagram().get_mxgraph(p, type)

    # parsed_html = urllib.parse.quote(view_html, safe="~@#$&()*!+=:;,.?/\'")
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


def show(p, width=960, height=750, diagram='AD', type=Action):
    src = ''
    graph = GuiMXGraphActionDiagram().get_mxgraph(p)
    # print(graph)
    src = "http://www.sysmpy.org/view/?g=" + graph
    # parsed_html = urllib.parse.quote(src, safe="~@#$&()*!+=:;,.?/\'")
    # print(parsed_html)

    # parsed_html = urllib.parse.quote(view_html, safe="~@#$&()*!+=:;,.?/\'")
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