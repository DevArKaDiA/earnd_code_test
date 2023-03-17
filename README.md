# <p align="center">Earnd Code Test</p>

A little sub sections api management code excercise

## API Reference

#### Get all documents:

```http
  GET /document/
```

#### Get documents sections:

```http
  GET /document/<document_name>/sections/<?path>/
```

| Parameter       | Type     | Description                         |
| :-------------- | :------- | :---------------------------------- |
| `document_name` | `string` | **Required**. Name of root document |

| Body(JSON) | Type     | Description                                   |
| :--------- | :------- | :-------------------------------------------- |
| `path`     | `string` | camel_case dot notation path for sub sections |

#### Post documents sections:

```http
  GET /document/<document_name>/sections/<?path>/
```

| Parameter       | Type     | Description                         |
| :-------------- | :------- | :---------------------------------- |
| `document_name` | `string` | **Required**. Name of root document |

| Body (JSON) | Type                      | Description                                                  |
| :---------- | :------------------------ | :----------------------------------------------------------- |
| `path`      | `string`                  | **Required** camel_case dot notation path for sub sections   |
| `name`      | `string`                  | **Required**. name of the sub-section@Document               |
| `text`      | `string`                  | **Required** Text for the sectin                             |
| `sections`  | `Dict[str, self@Section]` | **Required** Dict for more sub section could be a empty Dict |

### Notes:

## 🧑🏻‍💻 Usage

```bash
  python3 -m venv ./env
  activate env
  pip3 install -r requirements.txt
  python3 python3 src/app.py
```
