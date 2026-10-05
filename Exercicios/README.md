# Exercícios de Lógica e Python

Este repositório reúne exercícios desenvolvidos durante meus estudos de **lógica de programação, fundamentos de Python e desenvolvimento de APIs**.

A proposta foi começar pelos fundamentos da linguagem e evoluir gradualmente para conceitos utilizados em aplicações backend reais, praticando desde funções, estruturas de dados e orientação a objetos até programação assíncrona, tratamento de erros e construção de APIs com FastAPI.

Os exercícios foram inspirados principalmente em desafios realizados na plataforma **BeeCrowd**, mas também foram adaptados e desenvolvidos com foco nos conhecimentos necessários para projetos próprios.

Essa prática serviu como base para projetos maiores, incluindo a **API de Recargas e Pagamentos com Asaas**, desenvolvida posteriormente.

🔗 **Projeto relacionado:**
https://github.com/noahsvieira/API-de-recargas-e-pagamento-de-contas-com-Asaas

---

# Descrição dos exercícios

##  Nível 1 — Fundamentos de Python

Exercícios voltados para a construção da base da linguagem, sem utilização de FastAPI.

### 1.1 — Validação de telefone

Crie uma função chamada `validar_telefone(telefone)` que recebe um texto e retorna:

* `True` se possuir entre 10 e 11 caracteres e todos forem números;
* `False` caso contrário.

**Conceitos praticados:**

* Funções
* Strings
* `len()`
* `.isdigit()`
* Condições
* Validação de dados

---

### 1.2 — Classe `Pedido`

Crie uma classe chamada `Pedido`, com `__init__` recebendo `produto` e `valor`.

Adicione um método `resumo()` que retorne uma frase seguindo o modelo:

```text
Pedido de Recarga - R$ 20.00
```

**Conceitos praticados:**

* Classes
* `__init__`
* Atributos
* Métodos
* Programação Orientada a Objetos
* Formatação de strings

---

### 1.3 — Controle de IDs repetidos

Crie um `set()` vazio chamado `ids_vistos`.

Escreva um trecho de código que receba uma lista de IDs, contendo alguns valores repetidos, e:

1. Verifique se o ID já está no conjunto;
2. Imprima apenas os IDs que ainda não foram registrados;
3. Adicione cada ID ao conjunto após imprimi-lo.

**Conceitos praticados:**

* `set`
* Estruturas de repetição
* Condicionais
* Controle de valores duplicados
* Lógica de programação

---

#  Nível 2 — `async/await` e tratamento de erros

Nesta etapa, os exercícios começam a trabalhar conceitos importantes para aplicações backend, como programação assíncrona e tratamento adequado de exceções.

### 2.1 — Programação assíncrona

Escreva uma função `async def buscar_dado()` que aguarde 2 segundos utilizando `asyncio.sleep` e, depois, retorne:

```text
dado encontrado
```

Execute a função utilizando `await` dentro de outra função `async def main()`.

**Conceitos praticados:**

* `async def`
* `await`
* `asyncio`
* `asyncio.sleep`
* Programação assíncrona

---

### 2.2 — Exceção personalizada

Crie uma classe de erro personalizada chamada `SaldoInsuficienteError`, que herde de `Exception` e armazene:

* `valor_necessario`
* `valor_disponivel`

Depois, escreva uma função que verifique um saldo e utilize `raise` para disparar essa exceção quando o saldo disponível for insuficiente.

**Conceitos praticados:**

* Exceções
* `Exception`
* `raise`
* Classes personalizadas
* Validação de regras de negócio

---

### 2.3 — Tratamento de divisão por zero

Utilizando `try/except`, escreva uma função `dividir(a, b)` que tente realizar a divisão de `a` por `b`.

Caso `b` seja zero, trate o `ZeroDivisionError` e retorne uma mensagem amigável em vez de interromper o programa.

**Conceitos praticados:**

* `try`
* `except`
* `ZeroDivisionError`
* Tratamento de erros
* Validação de entradas

---

#  Nível 3 — Construindo uma Mini API

Nesta etapa, o objetivo é aplicar os conhecimentos anteriores na construção de uma aplicação backend independente.

A proposta é desenvolver, **do zero e de forma independente**, .

## API de Lista de Tarefas

Crie uma nova API chamada **API de Lista de Tarefas**, em um projeto separado.

### Requisitos

#### Schema `TarefaIn`

Crie um schema contendo:

```python
titulo: str
concluida: bool = False
```

#### `POST /tarefas`

Crie uma rota para receber uma nova tarefa e armazená-la em uma lista em memória.

Não é necessário utilizar banco de dados. Uma lista Python comum pode ser utilizada:

```python
tarefas = []
```

#### `GET /tarefas`

Crie uma rota que retorne todas as tarefas cadastradas.

#### `GET /tarefas/{indice}`

Crie uma rota que retorne uma tarefa específica utilizando sua posição na lista.

#### Autenticação

Proteja todas as rotas utilizando a mesma lógica de autenticação por `x-api-key` utilizada no projeto principal.

**Conceitos praticados:**

* FastAPI
* APIs REST
* Pydantic
* Schemas
* Métodos HTTP
* `POST`
* `GET`
* Path parameters
* Validação de dados
* Autenticação por API Key
* Estrutura de aplicações backend
* Integração entre os conceitos estudados

---

#  Objetivo do repositório

A ideia deste repositório é registrar minha evolução prática em Python, começando pelos fundamentos e avançando gradualmente para conceitos utilizados no desenvolvimento backend.

A progressão dos exercícios segue a lógica:

**Python básico → lógica → orientação a objetos → tratamento de erros → programação assíncrona → FastAPI → API REST**

O objetivo não é apenas resolver exercícios, mas **entender os fundamentos, praticá-los e posteriormente aplicá-los na construção de projetos maiores**.

Um exemplo dessa evolução é a:

🚀 **API de Recargas e Pagamentos com Asaas**
Python + FastAPI + APIs externas + autenticação + webhooks + validação + tratamento de erros.

🔗 https://github.com/noahsvieira/API-de-recargas-e-pagamento-de-contas-com-Asaas

Fique à vontade para utilizar os exercícios como material de estudo e prática.
