# 基本操作

## 启动所有的容器

```
 docker-compose up -d
```

## 进入 web server 的容器，启动 web server

```
docker-compose exec blog bash
```

### 进入 `src/management` 目录, 创建数据库结构

````
python rsyncdb.py
```
### 进入`src` 目录，启动 web server

```
python server.py
```
