# Sistema de Locadora 
## Resumo:
  O sistema permite cadastrar clientes e itens, fazer a listagem dos mesmos, alugar por CPF e devolver, além da listagem dos alugados, que também realiza a consulta por CPF. 
  O projeto funciona utilizando o paradigma de programação Orientação a objeto. 

### Funções
* **Cadastro**:
    Ambas as funções que envolvem cadastro tem seus objetos definidos em suas respectivas classes (Clientes e Itens)
    Itens são divididos entre Filmes e Jogos, por meio do atributo tipo, que futuramente será útil para realizar listagens, deixando o código mais organizado.
  
* **Listagens**:
    As listagens são feitas por meio de um laço for que percorre todos os obejtos da cadastrados, no caso de itens, é requisitado qual tipo (filme ou jogo) você quer consultar.
    A listagem de alugados, busca por cliente, ou seja, quais são os itens que estão alugados naquele CPF.

* **Alugar**:
    Para alugar um item, você precisa digitar o código que corresponde e informar seu CPF, para que assim depois do item ser marcado como disponível, o cliente receba no atributo itens alugados.

* **Devolver**:
  A devolução ocorre utilizando a mesma estratégia, tirando a marca de emprestado do item e posteriormente desassociando o cliente do item. 
