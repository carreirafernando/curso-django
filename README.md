# Curso-Django

Tópicos aprendidos:

- Adcionando .gitignore;
  > **_.gitignore pego na internet_**
- Criando ambiente virtual;
  > _python -m venv venv_
- Baixando o Django;
  > _pip install django_
- Criando o Projeto;
  > _django-admin startproject_
- Criando o app recipes;
  > _python manage.py startapp recipes_
- Colocar o nome do app no arquivo _settings.py_;
  
  ![](imagens/configuracao-settings.png)

- Criado pasta _base_templates_ e adicionado o caminha no arquivo _settings.py_;

  ![](imagens/configuracao-base_templates.png)

- Separando o _Head_ da página e incluindo na _index.html_;
  > _{% include "recipes/partials/head.html" %}_

  ![](imagens/incluindo-head.png)

  -Incluindo o contaúdo do _index.html_ com _include_;
   > _{% include "endereço" %}_

   ![](imagens/incluindo-paginas.png)