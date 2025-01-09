# 使用 Python 3.9 作为基础镜像
FROM python:3.9-slim

# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 设置环境变量（可以在运行时覆盖）
ENV API_KEY=""

# 使用 uvicorn 启动应用
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"] 