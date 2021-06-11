import web

render = web.template.render("mvc/views/herramientas/", base="template")

class Docker():

    def GET(self):
        try:
            return render.docker() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            form = web.input()
            print(form)
        except Exception as e:
            return "Error"