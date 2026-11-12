# ECS Demo

Приложение читает настройки из переменных окружения. Их можно менять в AWS ECS без пересборки Docker-образа.

## Переменные окружения

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `APP_TITLE` | `ECS Demo` | Заголовок страницы |
| `APP_MESSAGE` | `Hello from AWS ECS!` | Сообщение на странице |
| `APP_VERSION` | `v1` | Версия приложения |
| `APP_ENVIRONMENT` | `local` | Название окружения, например `dev` или `production` |
| `APP_OWNER` | `not set` | Владелец или команда |
| `AWS_REGION` | `local` | Регион AWS; в ECS обычно задаётся платформой |
| `PORT` | `80` | Внутренний порт контейнера |

## Локальная проверка

```bash
docker build -t ecs-demo .

docker run --rm -p 8888:80 \
  -e APP_TITLE="My ECS Application" \
  -e APP_MESSAGE="Environment variables work" \
  -e APP_VERSION="v2" \
  -e APP_ENVIRONMENT="development" \
  -e APP_OWNER="Platform Team" \
  ecs-demo
```

После запуска откройте http://127.0.0.1:8888.

## Настройка в AWS ECS Console

1. Откройте **ECS → Task definitions**.
2. Выберите семейство Task Definition и нажмите **Create new revision**.
3. Откройте настройки контейнера.
4. В разделе **Environment variables** добавьте нужные пары `Key` / `Value`.
5. Сохраните новую revision.
6. Обновите ECS Service, выберите новую revision и запустите deployment.

Переменные из Task Definition имеют приоритет над значениями `ENV`, записанными в Dockerfile.
