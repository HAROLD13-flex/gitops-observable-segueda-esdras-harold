from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    pod_name = socket.gethostname()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plateforme GitOps - Harold Segueda</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f6f9; }}
            h1 {{ color: #1e3a8a; }}
            .container {{ background: white; padding: 30px; display: inline-block; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            .footer {{ margin-top: 20px; font-size: 0.8em; color: #6b7280; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Projet Individuel : Plateforme GitOps</h1>
            <h2>Étudiant : Harold Segueda</h2>
            <p>L'application web est déployée avec succès de manière automatique et versionnée !</p>
            <p><strong>ID du Pod K8s :</strong> {pod_name}</p>
            <div class="footer">Statut : Sécurisé & Observable</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
