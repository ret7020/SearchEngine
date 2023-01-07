from flask import Flask, render_template, request, jsonify
import engine



class WebUI:
    def __init__(self, name, host='0.0.0.0', port='8080'):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
        self.official_proxies = ["http://3.70.173.147:52084"]
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/search')
        def __search():
            return self.search()
        @self.app.route('/proxies')
        def __proxies():
            return self.get_search_proxies()

    
    def index(self):
        return render_template("index.html")

    def get_search_proxies(self):
        return jsonify(self.official_proxies)


    def search(self):
        query = request.args.get("query")
        #results = engine.search(query) # legacy
        results = engine.search_via_spr(query, "http://3.70.173.147:52084")
        #results = []
        return render_template("results_page.html", query=query, links=results, res_count=len(results))
    
    def run(self):
        self.app.run(host=self.host, port=self.port)


if __name__ == "__main__":
    app = WebUI(__name__)
    app.run()