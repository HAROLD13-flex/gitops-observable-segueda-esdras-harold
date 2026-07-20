# Étape 1 : Build et installation des dépendances
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Étape 2 : Image finale légère et sécurisée
FROM python:3.11-slim AS final

WORKDIR /app

# Copier les dépendances installées depuis l'étape builder
COPY --from=builder /root/.local /home/appuser/.local
COPY app.py .

# Création d'un utilisateur non-root pour la sécurité
RUN useradd -u 10001 appuser && chown -R appuser:appuser /app
USER appuser

# Ajouter le chemin des binaires python locaux au PATH
ENV PATH=/home/appuser/.local/bin:$PATH
EXPOSE 5000

CMD ["python", "app.py"]
