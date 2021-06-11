import web

urls = (
    '/', 'mvc.controllers.index.Index',

    '/docker', 'mvc.controllers.herramientas.docker.Docker',
    '/ubuntu', 'mvc.controllers.herramientas.ubuntu.Ubuntu',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()