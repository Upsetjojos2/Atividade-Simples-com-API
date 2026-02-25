import requests

# Configurar headers
headers = {'X-GitHub-Api-Version': '2022-11-28'}

# Configurar base URL e owner
api_base_url = 'https://api.github.com'
owner = 'amzn'
url = f'{api_base_url}/users/{owner}/repos'

# Configurar token de acesso (use variável de ambiente)
import os
access_token = os.getenv('GITHUB_TOKEN', 'seu_token_aqui')
headers = {'Authorization': 'Bearer ' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}

# Buscar repositórios por página
repos_list = []
for page_num in range(1, 6):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
        
    except:
        repos_list.append(None)

print(f'URL: {url}')
print(f'Número de páginas de repositórios: {len(repos_list)}')

# Buscar seguidores
username = 'amzn'
url = f"https://api.github.com/users/{username}/followers"

response = requests.get(url, headers=headers)
followers = response.json()

# Buscar todos os seguidores com paginação
page_num = 1
followers_list = []

while True:
    try:
        url_page = f"{url}?page={page_num}&per_page=100"
        response = requests.get(url_page, headers=headers)
        
        if response.status_code != 200:
            break
            
        followers_page = response.json()
        
        if not followers_page:
            break
        
        followers_list.extend(followers_page)
        page_num += 1
        print(f'Página {page_num - 1} processada. Total de seguidores: {len(followers_list)}')
         
    except Exception as e:
        print(f"Error fetching page {page_num}: {e}")
        break

print(f'\nNúmero total de seguidores: {len(followers_list)}')

