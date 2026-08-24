FROM python:3.12-slim

WORKDIR /app

# 先复制依赖清单
COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# 复制全部项目代码
COPY . ./

# 启动命令，online_image项目，gunicorn
# CMD ["gunicorn","online_image:app","--bind","0.0.0.0:${PORT}"]
CMD gunicorn online_image:app --bind 0.0.0.0:${PORT}
