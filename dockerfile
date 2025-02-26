# 使用官方的Python基础镜像
FROM python:3.11.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录

COPY mindsearch /app/mindsearch

# 安装依赖项

RUN pip install  --no-cache-dir --index-url https://pypi.tuna.tsinghua.edu.cn/simple \  
    duckduckgo_search==5.3.1b1 \
    einops \
    fastapi \
    janus \
    pyvis \
    sse-starlette \
    termcolor \
    uvicorn \
    griffe==0.48.0 \
    python-dotenv \ 
    lagent==0.5.0rc2 \
    matplotlib \
    pydantic==2.6.4 \
    schemdraw \
    transformers==4.41.0 \
    tenacity \
    gradio \
    gradio==5.7.1

# 暴露应用程序的端口
EXPOSE 8002

# 定义启动命令
CMD ["python3", "-m", "mindsearch.app", "--model_format", "internlm_silicon", "--search_engine", "GoogleSearch"]