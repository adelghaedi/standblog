# StandBlog

StandBlog is a Django-based blog application that provides a complete content management system for articles, categories, comments, likes, and contact messages. It's designed to be simple, clean, and easily extendable.

## Features

- **Articles** – Full CRUD for blog posts.
- **Categories** – Organize articles by topic.
- **Likes** – Users can like/unlike articles.
- **Comments** – Users can leave comments on articles.
- **Contact Messages** – A "Contact Us" section to receive messages from visitors.
- **Homepage** – Displays a list of recent articles and a preview of selected articles.
- **Article Details** – Full article view with comments and likes.
- **Recent Articles Section** – Shows latest posts on the homepage.

## Installation & Run

1.**Clone the repository**

```bash
git clone https://github.com/adelghaedi/standblog.git
```

2.**Install dependencies**

```bash
pip install -r requirements.txt
```
3.**Run the server:**

```bash
python manage.py runserver
```

4.**Open the browser at**

```
http://127.0.0.1:8000/
```

## Technologies

- Python 3.12
- Django (latest stable version)
- SQLite (default, can be replaced with PostgreSQL/MySQL)
- HTML/CSS (Bootstrap or custom styling)

## Contributing

Feel free to fork the project, make your changes, and submit a Pull Request.

## License

This project is licensed under the **MIT License**.