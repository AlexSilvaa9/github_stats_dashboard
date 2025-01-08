import random
import pandas as pd
import requests
import os
from datetime import datetime, timedelta


# Función para obtener la cantidad de commits de un repositorio
def get_commit_count(username, repo_name, token=None):
    url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
    headers = {'Authorization': f'token {token}'} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching commits for repo {repo_name}: {response.status_code}")
    commits = response.json()
    return len(commits)

# Función para obtener los colaboradores de un repositorio
def get_collaborators(username, repo_name, token=None):
    url = f'https://api.github.com/repos/{username}/{repo_name}/collaborators'
    headers = {'Authorization': f'token {token}'} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching collaborators for repo {repo_name}: {response.status_code}")
    collaborators = response.json()
    return len(collaborators)

# Función para obtener métricas de GitHub
def get_github_metrics(username, token=None):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching GitHub data: {response.status_code}")
    repos = response.json()

    # Listas para almacenar las métricas generales y los lenguajes
    repo_metrics = []
    language_metrics = []

    for repo in repos:
        repo_name = repo['name']
        repo_url = repo['url']
        languages_url = repo['languages_url']

        # Obtener lenguajes del repositorio
        languages_response = requests.get(languages_url, headers=headers)
        languages = languages_response.json() if languages_response.status_code == 200 else {}

        # Obtener más detalles del repositorio
        repo_details = requests.get(repo_url, headers=headers).json()
        stars = repo_details.get('stargazers_count', 0)
        forks = repo_details.get('forks_count', 0)
        watchers = repo_details.get('watchers_count', 0)
        open_issues = repo_details.get('open_issues_count', 0)
        size = repo_details.get('size', 0)
        created_at = repo_details.get('created_at', 'N/A')
        updated_at = repo_details.get('updated_at', 'N/A')

        # Obtener la cantidad de commits y colaboradores
        commit_count = get_commit_count(username, repo_name, token)
        collaborator_count = get_collaborators(username, repo_name, token)

        # Añadir una fila para el repositorio con métricas generales
        repo_metrics.append({
            'Repo': repo_name,
            'Stars': stars,
            'Forks': forks,
            'Watchers': watchers,
            'Open_Issues': open_issues,
            'Size (KB)': size,
            'Created_At': created_at,
            'Updated_At': updated_at,
            'Commits': commit_count,
            'Collaborators': collaborator_count
        })

        # Añadir métricas por lenguaje
        for language, _ in languages.items():
            language_metrics.append({
                'Repo': repo_name,
                'Language': language,
                'Commits_in_Language': commit_count  # O cualquier métrica relevante
            })

    return repo_metrics, language_metrics

# Guardar datos en un CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Archivo CSV guardado como {filename}")

# Configuración del usuario de GitHub
GITHUB_USERNAME = 'alexsilvaa9'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Configura tu token en las variables de entorno

# Obtener métricas de GitHub
repo_metrics, language_metrics = get_github_metrics(GITHUB_USERNAME, GITHUB_TOKEN)

# Guardar las tablas en CSV
save_to_csv(repo_metrics, 'repo_metrics.csv')
save_to_csv(language_metrics, 'language_metrics.csv')
