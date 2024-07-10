from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello, World!'}


@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}
