supported_models = {
    "OpenAI": {
        "gpt-4": {
            "type": "chat",
            "parameters": {
                "prompt": {
                    "type": "prompt_message",
                    "required": True,
                    "default": "This is a test prompt."
                },
                "max_tokens": {
                    "type": "integer",
                    "required": False,
                    "min": 1,
                    "max": 8192,
                    "default": 16
                },
                "temperature":  {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 2.0,
                    "default": 1.0
                },
                "top_p": {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 1.0,
                    "default": None
                }
            }
        },
        "gpt-3.5-turbo": {
            "type": "chat",
            "parameters": {
                "prompt": {
                    "type": "prompt_message",
                    "required": True,
                    "default": "This is a test prompt."
                },
                "max_tokens": {
                    "type": "integer",
                    "required": False,
                    "min": 1,
                    "max": 4097,
                    "default": 16
                },
                "temperature":  {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 2.0,
                    "default": 1.0
                },
                "top_p": {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 1.0,
                    "default": None
                }
            }
        },
        "babbage-002": {
            "type": "completions",
            "parameters": {
                "prompt": {
                    "type": "prompt_message",
                    "required": True,
                    "default": "This is a test prompt."
                },
                "max_tokens": {
                    "type": "integer",
                    "required": False,
                    "min": 1,
                    "max": 16384,
                    "default": 16
                },
                "temperature":  {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 2.0,
                    "default": 1.0
                },
                "top_p": {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 1.0,
                    "default": None
                }
            }
        },
        "davinci-002": {
            "type": "completions",
            "parameters": {
                "prompt": {
                    "type": "prompt_message",
                    "required": True,
                    "default": "This is a test prompt."
                },
                "max_tokens": {
                    "type": "integer",
                    "required": False,
                    "min": 1,
                    "max": 16384,
                    "default": 16
                },
                "temperature":  {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 2.0,
                    "default": 1.0
                },
                "top_p": {
                    "type": "float",
                    "required": False,
                    "min": 0.0,
                    "max": 1.0,
                    "default": None
                }
            }
        },
    }
}