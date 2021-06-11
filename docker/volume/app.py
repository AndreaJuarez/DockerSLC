import web

urls = (
    '/', 'mvc.controllers.index.Index',

    '/insert', 'mvc.controllers.herramientas.docker.Docker',
    '/list', 'mvc.controllers.herramientas.ubuntu.List',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()