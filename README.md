# Projeto GitHub API - Atividades

Este projeto utiliza a API do GitHub para extrair e processar informações sobre usuários, repositórios e seguidores.

## 📋 Descrição

O projeto utiliza a API GitHub para extrair repositórios e seguidores de um usuário com paginação.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- Biblioteca `requests`

### Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd My_project
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install requests
```

### Executar o Projeto

**Script principal:**
```bash
python Atividade2.py
```

**Notebook com análises:**
```bash
jupyter notebook Atividades.ipynb
```

## 📝 Detalhes do Projeto

### Funcionalidades Principais
Busca repositórios e seguidores do usuário 'amzn':
- Lista todos os repositórios com paginação (5 páginas)
- Extrai dados de todos os seguidores usando `while True` com paginação dinâmica
- Exibe o número total de seguidores coletados

## 🔑 Autenticação

O projeto utiliza um token de autenticação GitHub para aumentar os limites de requisições e acessar dados privados. O token é configurado nos headers das requisições:

```python
headers = {
    'Authorization': 'Bearer <seu_token>',
    'X-GitHub-Api-Version': '2022-11-28'
}
```

**⚠️ Nota**: Não compartilhe tokens em repositórios públicos. Use variáveis de ambiente para dados sensíveis.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Requests** - Biblioteca para requisições HTTP
- **GitHub API v3** - API REST do GitHub
- **Jupyter Notebook** - Para análise interativa

## 📊 Estrutura do Projeto

```
My_project/
├── Atividade2.py         # Script principal
├── Atividades.ipynb      # Notebooks com código interativo
├── README.md             # Este arquivo
└── venv/                 # Ambiente virtual Python
```

## 🔗 Links Úteis

- [Documentação GitHub API](https://docs.github.com/en/rest)
- [Biblioteca Requests](https://docs.python-requests.org/)
- [GitHub CLI](https://cli.github.com/)

## 📄 Licença

Este projeto é de uso educacional.

---

**Abgs**: Desenvolvido para fins de aprendizado com a API do GitHub
