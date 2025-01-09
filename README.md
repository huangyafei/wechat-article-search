# 微信文章搜索 API

一个基于 FastAPI 构建的微信公众号文章搜索 API 服务。该服务提供了简单易用的接口，允许用户搜索微信公众号文章。

## 功能特点

- 支持关键词搜索微信公众号文章
- RESTful API 设计
- API 密钥认证保护
- Docker 支持
- 健康检查
- 可配置的搜索结果数量

## 快速开始

### 环境要求

- Python 3.7+
- Docker（可选）

### 安装方式

#### 方式一：使用 Docker（推荐）

1. 克隆仓库：
```bash
git clone https://github.com/[your-username]/wechat-article-search.git
cd wechat-article-search
```

2. 设置环境变量：
创建 `.env` 文件并设置 API 密钥：
```bash
echo "API_KEY=your_api_key_here" > .env
```

3. 使用 Docker Compose 启动服务：

首先确保你已经安装了 Docker 和 Docker Compose。然后运行：
```bash
# 拉取最新镜像
docker pull huangyafei/wechat-article-search:latest

# 启动服务
docker-compose up -d
```

#### 方式二：本地运行

1. 克隆仓库并安装依赖：
```bash
git clone https://github.com/[your-username]/wechat-article-search.git
cd wechat-article-search
pip install -r requirements.txt
```

2. 设置环境变量：
```bash
export API_KEY=your_api_key_here
```

3. 运行服务：
```bash
python run.py
```

### API 使用说明

服务启动后，API 将在 `http://localhost:8000` 运行。

#### API 端点

- **GET /search/**
  - 参数：
    - `query`: 搜索关键词（必需）
    - `top_num`: 返回结果数量，默认为10（可选）
  - 请求头：
    - `X-API-Key`: API 密钥（必需）

#### 示例请求

```bash
curl -X GET "http://localhost:8000/search/?query=人工智能&top_num=5" \
     -H "X-API-Key: your_api_key_here"
```

## 环境变量

- `API_KEY`: API 访问密钥（必需）

## License

[MIT License](LICENSE) 