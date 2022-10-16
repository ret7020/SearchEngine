from flask import Flask


class WebUI:
    def __init__(self, name, host='0.0.0.0', port='8080'):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
    
        @self.app.route('/')
        def __index():
            return self.index()
    
    def index(self):
        return "WebUI works!"

    
    def run(self):
        self.app.run(host=self.host, port=self.port)


if __name__ == "__main__":
    pass