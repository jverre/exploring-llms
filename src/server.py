from fastapi import FastAPI, Request
import utils
import openai
import comet_llm
import time

app = FastAPI()

def log_prompt_to_comet(prompt, response, parameters, tags = None, duration=None):
    import os
    if 'COMET_API_KEY' in os.environ:
        comet_llm.log_prompt(
            project='blog-post',
            tags=tags,
            prompt=prompt,
            output=response,
            metadata=parameters,
            duration=duration,
        )
    
@app.get("/")
async def health_check():
    return "Running ..."


@app.get("/models")
async def get_models():
    return utils.supported_models


@app.post("/models/{model_type}/{model_name}")
async def query_model(model_type, model_name, request: Request):
    parameters = await request.json()
    model = utils.supported_models[model_type][model_name]
    
    if model_type == 'OpenAI':
        
        if model['type'] == 'chat':
            prompt_message = parameters['prompt']
            del parameters['prompt']
            start_time = time.time()
            completion = openai.ChatCompletion.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt_message}],
                **parameters
            )
            duration = time.time() - start_time

            response = completion.choices[0].message
            
            
        elif model['type'] == 'completions':
            prompt_message = parameters['prompt']
            del parameters['prompt']
            completion = openai.Completion.create(
                model=model_name,
                prompt=prompt_message,
                **parameters
            )

            response = completion.choices[0].text
        else:
            raise ValueError(f"model type = {model['type']} is not supported")

        log_prompt_to_comet(
                prompt=prompt_message,
                response=response,
                duration=duration,
                tags = [model_type, model_name],
                parameters = {
                    "usage": {**completion.usage},
                    **parameters
                }
            )
            
        return response