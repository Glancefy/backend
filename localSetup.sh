# postgres db
docker run --name glancefy-postgres -e POSTGRES_DB=glancefy_db -e POSTGRES_USER=glancefy_user -e POSTGRES_PASSWORD=glancefy_password -p 5432:5432 -d postgres:14

# redis
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest

# celery worker
celery -A core worker -l info

# celery beat
celery -A core beat -l info