## **Rodando o projeto pela primeira vez**

### Criando arquivo .env

Crie na raiz do projeto um arquivo .env, o mesmo não será, e não deve ser comitado, e adicionar as seguintes informações:

```
SECRET_KEY='RANDOM_SECRET_KEY'
```

### 1) Criando Ambiente Virtual

Em um terminal na raiz do projeto crie o ambiente virtual para instalação das dependências:

```
uv venv
```

### 2) Restaurando Dependências

```
uv sync
```