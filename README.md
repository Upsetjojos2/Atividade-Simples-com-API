# My_project

Visão geral
-----------

Projeto simples contendo um notebook com atividades e um script de exemplo que consulta a API do GitHub.

Principais arquivos
-------------------

- [Atividades.ipynb](Atividades.ipynb) — notebook principal com as atividades.
- [Atividade.py](Atividade.py) — script de exemplo que busca dados de usuário do GitHub.
- [README.md](README.md) — este arquivo.

Requisitos
----------

- Python 3.8+
- `pip`

Instalação rápida
-----------------

Crie um ambiente virtual e instale dependências (se houver):

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt  # se existir
```

Como executar
-------------

Abra o notebook:

```bash
pip install jupyterlab
jupyter lab
```

Execute o script de exemplo:

```bash
python Atividade.py
```

Estrutura do repositório
------------------------

- Atividades.ipynb
- Atividade.py
- README.md

Contribuições
-------------

- Faça fork e abra um Pull Request.
- Formate o código e execute testes locais antes de enviar PRs (se houver testes).

Comandos Git úteis
------------------

```bash
# Verificar status
git status

# Verificar remotes
git remote -v

# Ver o último commit
git log -1 --pretty=fuller
```

Licença
-------

Adicione um arquivo `LICENSE` com a licença desejada (por exemplo MIT). Posso adicionar uma licença se quiser.

Contato
-------

Abra uma issue para perguntas, pedidos de recurso ou reportar bugs.

Próximos passos que posso ajudar
-------------------------------

- Gerar `requirements.txt` a partir das importações detectadas.
- Adicionar um `LICENSE` (por exemplo MIT).
- Aceitar argumentos de linha de comando em `Atividade.py` para escolher o `username`.
