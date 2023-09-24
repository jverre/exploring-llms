import json
import requests
import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.session_state.prompt_response = ""

def get_model_list():
    response = requests.get('http://0.0.0.0:8080/models')
    
    return response.json()

def get_model_parameters(models, model_type, model_name):
    return models[model_type][model_name]['parameters']

def create_sidebar(models):
    with st.sidebar:
        st.header('Models')

        options = []
        for model_type in models.keys():
            options += [(model_type, model_name) for model_name in models[model_type].keys()] 
        
        model = st.selectbox(
            label="Select a model",
            format_func=lambda x: f"{x[0]} - {x[1]}",
            options=options)
    return model

def create_page_layout():
    col1, col2 = st.columns([0.7, 0.3], gap="large")
    with col1:
        st.header("Prompt")

    with col2:
        st.header("Parameters")
    
    return col1, col2


def get_column_for_parameter(parameter_value, col1, col2):
    if parameter_value.get('required', False):
        return col1
    else:
        return col2

def populate_parameters(models, model, col1, col2):
    parameters = {}

    model_type, model_name = model
    model_parameters = get_model_parameters(models, model_type, model_name)
    
    for parameter, value in model_parameters.items():
        parameter_type = value['type']
        col = get_column_for_parameter(value, col1, col2)

        with col:
            if parameter_type == "prompt_message":
                parameters[parameter] = st.text_area(
                    label="prompt",
                    value=value['default'])
            
            elif parameter_type == 'integer':
                parameters[parameter] = st.slider(
                    label=parameter,
                    min_value=value['min'],
                    max_value=value['max'],
                    value = value['default'])
            
            elif parameter_type == 'float':
                parameters[parameter] = st.slider(
                    label=parameter,
                    min_value=value['min'],
                    max_value=value['max'],
                    value = value['default'])
            
            else:
                raise ValueError(f"type {parameter_type} not support for parameter: {parameter}")
    return parameters

def submit_prompt(model, parameters):
    model_type, model_name = model

    response = requests.post(
        f'http://0.0.0.0:8080/models/{model_type}/{model_name}',
        json=parameters)

    prompt_response = response.json()
    return prompt_response

with st.spinner('Loading list of supported models'):
    models = get_model_list()

# Create sidebar
model = create_sidebar(models)

# Create layout
col1, col2 = create_page_layout()

# Populate App with paramters
parameters = populate_parameters(models, model, col1, col2)

with col1:
    if st.button(label='Submit'):
        response = submit_prompt(model, parameters)
        st.divider()
        st.write('**Prompt response**')
        st.write(response)