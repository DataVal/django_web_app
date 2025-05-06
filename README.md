# django_web_app
Aprendendo a usar o framework python Django para criação de aplicações web.

## Objetivo principal
- Aprender uma nova tecnologia, sem depender de qualquer assistente IA pra isso, ou seja, aprender algo na marra.

---

### Objetivos secundários
1. Aprender a sintaxe/comandos do framework django;
2. Entender como funciona nos bastidores;
3. Aprender como criar funcionalidades básicas de CRUD;
4. Entender como adicionar funcionalidades baseadas em permissão (nível de usuário);
5. Aprender como adicionar segurança na aplicação.

### Detalhes / Configurações
1. Crie o diretório com `mkdir django_web_app`;
2. Acesse o diretório com `cd django_web_app`;
3. É legal criar um ambiente virtual pro python tbm `python -m venv venv`, mas nesse caso vamos usar o python pipenv então `pip install pipenv`;
4. Ativar o venv `source venv/bin/activate` ou no Windows `venv\Scripts\activate`;
5. Instalar dependencias com `pip install requirements.txt` ou manualmente.

### Códigos
`pipenv install django` -> Instala o framework django no venv, que caso não existe é criado um pro diretório.
`pipenv shell` -> Ativa o ambiente virtual.
`django-admin startproject nomedoprojeto` -> Cria um novo projeto django. É necessário estar com o venv ativado pra isso funcionar.
`python manage.py startapp nomedoapp` -> Cria um app, que é basicamente um conjunto de funcionalidades que dizem respeito a algo específico do serviço como segurança, gerenciamento, visualização e etc. É de bom tom fazer com que cada app seja único e independente.
`selecione o interpretador que você definiu no venv` vai em views.py e dá um quick fix, aí é só escolher o último interpretador da lista.

### Anotações

- Um web framework é um modo estruturado de construir aplicações web, as vezes sendo confundido com uma biblioteca. A diferença é que uma biblioteca é um conjunto de funcionalidades que cumprem uma tarefa específica, React por ex. é uma biblioteca com várias funcionalidades usadas para desenvolvimento web. Um framework web não te dá nenhuma funcionalidade específica, somente nos define uma estrutura para que escrevamos nosso código em cima.

- MVT (Model View Template) é um conceito que explica como uma aplicação web funciona e interage com o cliente.
1. O Model/Modelo é a parte responsável pelo processamento dos dados. Representa como nossos dados são estruturados, guardados e devolvidos. De forma simplificada, ele lida com a parte de banco de dados da nossa aplicação. = gerenciamento dos dados
2. A parte View é responsável por manipular as interações do usuário com a aplicação. É onde nós recebemos as solicitações (requests) dos usuários, processamos e devolvemos uma resposta. Simplificando, lida com a parte lógica da aplicação. = parte lógica
3. Template lida com a interface, ou seja, a parte que o usuário de fato vê. Inclui o HTML com marcadores de posição para diferentes componentes dinâmicos que podemos adicionar a partir das visualizações da aplicação. = = renderização da interface do usuário

- No django tem dois tipos de views que podemos criar: uma view baseada em função e outra em classe. Primeiro vamos criar uma baseada em função. O próximo é vincular as funções e views em endereços.

- Eu precisei ir no `primeiroapp\views.py` e lá eu criei uma view de função e outra de classe, sendo que ambas pegavam uma request retornavam pra mim uma resposta que eu defini.

- Aí pra mapear essas views eu precisei acessar a pasta `urls.py` do mesmo diretório e criar o caminho urlpatterns e aí eu defini em forma de lista os dois caminhos `path(function, views = nomedafuncview), path(class, views = nomedaclassview.as_view())`

## Objetos de Request e Response
- Eles são usados para comunicar o usuário com o nosso app.
- Com o objeto Request nós podemos obter diferentes informações sobre o usuário. O método `request.method` nos da o metodo HTTP enviado pelo usuario que pode ser GET, PUT, PATCH, POST ou DELETE e usando isso podemos criar operações condicionadas. 
- O objeto Response é o que enviamos de volta pro usuário. 
- Uma migration é um processo que converte qualquer alteração no model.py para o nosso banco de dados real. Pra isso faremos `python manage.py makemigrations` e `python manage.py migrate`

- Crio um admin com `python manage.py createsuperuser` e crie as credenciais de admin