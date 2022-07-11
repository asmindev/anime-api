# Otakudesu API

API anime dari scrap otakudesu yang tidak offcial
[https://otakudesu-restfull.herokuapp.com](https://otakudesu-restfull.herokuapp.com)


## API Reference

#### Get Home

```http
  GET /home
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `page` | `number` | **Optional**. page number |

#### Get anime by Search

```http
  GET /search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `query`      | `string` | **Required**. title anime |

#### Get Anime Ongoing

```http
  GET /ongoing
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page` | `number` | **Optional**. page number |

#### Get List Anime

```http
  GET /listanime
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page` | `number` | **Optional**. page number |

#### Get Movie List

```http
  GET /movielist
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page` | `number` | **Optional**. page number |

#### Get Movie List

```http
  GET /detail
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug` | `string` | **Required**. anime slug |


```http
  GET /getvideo
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug` | `string` | **Required**. anime slug |
| `id` | `number` | **Required**. anime slug |


## Authors

- [@asmindev](https://www.github.com/asmindev)


## Installation

Install this project use pip

```bash
  git clone https://github.com/asmindev/anime-api
  cd anime-api
  pip install -r requirement.txt
  python3 app.py
```
    
