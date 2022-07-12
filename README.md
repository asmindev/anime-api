# Otakudesu API

API anime dari scrap otakudesu yang tidak offcial
[https://otakudesu-restfull.herokuapp.com](https://otakudesu-restfull.herokuapp.com)


## API Reference


| Path | Parameter | Type     | Required | Description                |
| :-------- | :-------- | :-------- | :------- | :------------------------- |
| [/home](https://otakudesu-restfull.herokuapp.com/home)| `page` | `number` | no | page number |
| [/search](https://otakudesu-restfull.herokuapp.com/search)| `query` | `string` | yes | query |
| [/ongoing](https://otakudesu-restfull.herokuapp.com/ongoing)  | `page` | `number` | no | page number |
| [/listanime](https://otakudesu-restfull.herokuapp.com/listanime)| `page` | `number` | no | page number |
| [/movielist](https://otakudesu-restfull.herokuapp.com/movielist)| `page` | `number` | no | page number |
| [/detail](https://otakudesu-restfull.herokuapp.com/detail)| `slug` | `string` | yes | slug of anime |
| [/detail](https://otakudesu-restfull.herokuapp.com/getvideo) | `slug` | `string` | yes | slug of episode |
|  | `id` | `number` | yes | id of episode |




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
    
