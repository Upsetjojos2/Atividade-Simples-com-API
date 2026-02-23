import requests


def get_user(username: str) -> dict:
	"""Retorna os dados do usuário GitHub como um dicionário."""
	url = f"https://api.github.com/users/{username}"
	resp = requests.get(url)
	resp.raise_for_status()
	return resp.json()


if __name__ == "__main__":
	username = "Upsetjojos2"
	user = get_user(username)

	nome = user.get('name')
	nome_usuario = user.get('login')
	repositorios = user.get('public_repos')
	data_criacao_dados = user.get('created_at')

	print(f'Nome: {nome}')
	print(f'Nome de usuário: {nome_usuario}')
	print(f'Número de repositórios públicos: {repositorios}')
	print(f'Data de criação dos dados: {data_criacao_dados}')
