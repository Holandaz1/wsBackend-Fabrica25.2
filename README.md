# Sistema de Cadastro de Produtos com Categorias

Projeto feito em Django para a disciplina de programação.  
A ideia foi criar um sistema que permitisse:

- Cadastrar produtos  
- Listar os produtos já cadastrados  
- Relacionar cada produto a uma categoria


# Como rodar

1. Clone o repositório:
   git clone https://github.com/seu-usuario/seu-repo.git
2. cd projeto
3. python manage.py migrate
4. python manage.py runserver
5. Depois é só acessar no navegador: http://127.0.0.1:8000/


# Observação importante

- Durante o desenvolvimento, tive um problema:
o Django não reconheceu o template em um dos testes, e acabei não conseguindo resolver a tempo.
Mesmo assim, resolvi subir o código aqui porque pode ser útil para análise, revisão ou até para alguém me apontar onde está o erro.

- Preferi deixar isso registrado para mostrar exatamente o ponto em que fiquei “travado”, em vez de simplesmente entregar sem nada ou tentar esconder o erro.


# Tecnologias usadas

- Python
- Django
- SQLite (banco de dados padrão do Django)

# Conclusão

- O foco não foi entregar algo perfeito, mas sim praticar Django e aprender na prática como funcionam apps, urls, models e templates.