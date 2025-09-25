from app import update_graph, app
from dash.development.base_component import Component
import pytest
from dash import dcc

def test_update_graph(): 
    fig = update_graph('north', 2020)
    assert fig.layout.title.text == '📈 Sales Data for North Region in 2020'
    assert fig.layout.xaxis.title.text == 'Date'
    assert fig.layout.yaxis.title.text == 'Sales ($)'
    assert len(fig.data) > 0
    assert fig.data[0].line.color == '#3498db'


def find_component_by_id(component: Component, target_id: str):
    """
    Recursively search Dash component tree for a component with the given id.
    """
    if getattr(component, "id", None) == target_id:
        return component

    if hasattr(component, "children"):
        children = component.children
        if not isinstance(children, (list, tuple)):
            children = [children]
        for child in children:
            if isinstance(child, Component):
                result = find_component_by_id(child, target_id)
                if result is not None:
                    return result
    return None


def test_radio_button_exists_in_layout():
    layout = app.layout
    radio = find_component_by_id(layout, "radio-selection")
    assert radio is not None, "Radio buttons with id='radio-selection' should be present"
    assert radio.__class__.__name__ == "RadioItems"