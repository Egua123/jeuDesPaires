# Un serveur simple qui retourne reçoit un chemin et retourne le texte
# contenu dans le fichier correspondant dans "documents"

import http.server

count = 0

def readFile(path):
    return open(path, 'rb').read().decode('utf-8')


def obtenirDocument(path):

    # Si aucun chemin n'est donné, on redirige vers index.html
    if path == "/":
        path = "/index.html"

    return readFile('documents' + path)


class ServeurWeb(http.server.BaseHTTPRequestHandler):
    # do_GET est exécuté à chaque requête GET
    def do_GET(self):
        global count

        doc = obtenirDocument(self.path)
        self.send_response(200)
        self.end_headers()

        # on imprime la requête dans la console
        print(count, self.path)
        count += 1

        # Lorsque do_GET retourne, le texte passé
        # à self.wfile.write est envoyé au client
        self.wfile.write(doc.encode('utf-8'))

    def log_message(self, format, *args):
        pass


http.server.HTTPServer(('localhost', 8000), ServeurWeb).serve_forever()
