import os
import json
from dotenv import load_dotenv
from lagent.llms import (
    GPTAPI,
    INTERNLM2_META,
    HFTransformerCasualLM,
    LMDeployClient,
    LMDeployServer,
)
# 使用环境变量读取配置文件路径
config_path_env = os.getenv('CONFIG_PATH')
if config_path_env:
    config_path = config_path_env
else:
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    
# 读取配置文件
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

SILICON_API_KEY = config.get('SILICON_API_KEY')
SILICON_MODEL = config.get('SILICON_MODEL')
OPENAI_API_KEY = config.get('OPENAI_API_KEY')
SILICON_API_URL = config.get('SILICON_API_URL')
QWEN_API_URL = config.get('QWEN_API_URL')
OPENAI_API_URL = config.get('OPENAI_API_URL')
QWEN_API_KEY = config.get('QWEN_API_KEY')
LOCAL_API_URL = config.get('LOCAL_API_URL')

internlm_server = dict(
    type=LMDeployServer,
    path="internlm/internlm2_5-7b-chat",
    model_name="internlm2_5-7b-chat",
    meta_template=INTERNLM2_META,
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

internlm_client = dict(
    type=LMDeployClient,
    model_name="internlm2_5-7b-chat",
    url=LOCAL_API_URL,
    meta_template=INTERNLM2_META,
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

internlm_hf = dict(
    type=HFTransformerCasualLM,
    path="internlm/internlm2_5-7b-chat",
    meta_template=INTERNLM2_META,
    top_p=0.8,
    top_k=None,
    temperature=1e-6,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)
# openai_api_base needs to fill in the complete chat api address
gpt4 = dict(
    type=GPTAPI,
    model_type="gpt-4-turbo",
    key=OPENAI_API_KEY,
    api_base=OPENAI_API_URL,
)


qwen = dict(
    type=GPTAPI,
    model_type="qwen-max-longcontext",
    key=QWEN_API_KEY,
    api_base=QWEN_API_URL,
    meta_template=[
        dict(role="system", api_role="system"),
        dict(role="user", api_role="user"),
        dict(role="assistant", api_role="assistant"),
        dict(role="environment", api_role="system"),
    ],
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=4096,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

internlm_silicon = dict(
    type=GPTAPI,
    model_type=SILICON_MODEL,
    key=SILICON_API_KEY,
    api_base=SILICON_API_URL,
    meta_template=[
        dict(role="system", api_role="system"),
        dict(role="user", api_role="user"),
        dict(role="assistant", api_role="assistant"),
        dict(role="environment", api_role="system"),
    ],
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)
