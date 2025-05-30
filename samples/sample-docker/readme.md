# Sample Docker

## Run Docker Image

- Build image

  ```shell
    docker build . -t image_name
  ```

  > you can rename the `image_name` with a custom name.

- Run image

  ```shell
    docker run -dp 8000:80 -e DB_NAME=neondb -e DB_USER=neondb_owner -e DB_PASSWORD=npg_sLfVg8iW4EwO -e DB_HOST=ep-steep-water-a102fmjl-pooler.ap-southeast-1.aws.neon.tech my_image
  ```

- Visit <https://localhost:8000> on your browser.

## Run Docker Compose

```shell
docker compose up -d
```
