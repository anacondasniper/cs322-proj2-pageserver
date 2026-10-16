# CS 322 Project 2: Page Server

A small Flask app, run in Docker, that serves HTML pages from `web/templates/`.

- Existing page (e.g. `/index.html`): 200 and the page
- Missing page: 404 with `404.html`
- URL containing `..`, `//`, or `~`: 403 with `403.html`

## Run

    cd web
    docker build -t uocis-flask-demo .
    docker run -d --rm -p 5000:5000 uocis-flask-demo

Then visit http://localhost:5000/index.html

Author: Milo Reynolds
