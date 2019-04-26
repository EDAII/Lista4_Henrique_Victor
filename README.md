# LISTA 4 - ESTRUTURA DE DADOS 2 - 2019/1

### Henrique Martins de Messias - 17/0050394
### Victor Rodrigues Silva - 16/0019516

<br>

### Instalações necessárias
- No teminal, digite os seguinte comando para instalar as dependências:
  ```bash
    $ pip3 install -r requirements.txt
    $ sudo apt-get install python3-tk
  ```


### Instruções de uso

- No terminal, vá até o diretório do exercício, que contém, além de arquivos como o README, a pasta "src"
- Digite o seguinte comando:

  ```bash
    $ cd src
  ```

- Para executar o código, digite:

  ```bash
    $ python3 main.py
  ```

### Detalhes da Lista 4

O software deste repositório é de uma <b>Fila de Pacientes</b> de um hospital.

Cada paciente possui as seguintes informações:
 - Nome
 - Sexo
 - Idade
 - Gravidade (1 a 5, sendo 1 significando "menor urgência" e 5 significando "urgência máxima")

O usuário pode criar uma quantidade determinada de pacientes aleatórios, ou criar um paciente individual, ao inserir os dados necessários.

A partir do momento em que houver pacientes na fila, o usuário pode ordená-los com:
 - Heap Sort Recursivo
 - Heap Sort Interativo

O usuário pode visualizar todos os pacientes, quandou houver algum para ver. Ele pode ver em ordem de chegada ou ordenado com base no critério de ordenação do hospital, que é:
 1. Gravidade
 2. Idosos (quanto mais velho, maior prioridade)
 3. Crianças e Adolescentes (quanto mais novo, maior prioridade)
 4. Adultos (quanto mais velho, maior prioridade)

Se quiser, o usuário pode comparar os métodos de ordenação de duas maneiras diferentes:
 - Comparar o tempo que cada método leva para ordenar a fila atuail
 - Comparar o tempo que cada método leva para ordenar filas aleatórias de tamanhos diferentes

O usuário pode também salvar a fila em um arquivo e carregar os dados de um arquivo no programa.