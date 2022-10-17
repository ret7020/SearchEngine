from flask import Flask, render_template, request
import engine

class WebUI:
    def __init__(self, name, host='0.0.0.0', port='8080'):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/search')
        def __search():
            return self.search()
    
    def index(self):
        return render_template("index.html")

    def search(self):
        query = request.args.get("query")
        #results = engine.search(query)
        results = []
        return render_template("results_page.html", query=query, links=results)
    
    def run(self):
        self.app.run(host=self.host, port=self.port)


if __name__ == "__main__":
    app = WebUI(__name__)
    app.run()