# Trabalho de Compiladores - Universidade Estadual de Maringá

Este repositório contém o trabalho de Compiladores realizado na disciplina de Compiladores na Universidade Estadual de Maringá. Neste trabalho, foi desenvolvido o analisador léxico e sintático de uma linguagem similar a linguagem C.

## Dependências
A única dependência para executar o projeto é instalar o PLY. Para instalar o PLY, você pode utilizar o gerenciador de pacotes pip. Para instalar o PLY, execute o seguinte comando:

```sh
pip install ply
```

## Execução
Para executar o analisador léxico e sintático, siga as instruções abaixo:

1. Abra o terminal e navegue até a pasta raiz do projeto.
2. Escreva o código que você deseja analisar em um arquivo `arquivo.txt`.
3. Execute o seguinte comando para rodar o analisador léxico:
```
python .\lex.py
```
4. Em seguida, execute o seguinte comando para rodar o analisador sintático:
```
python .\parsers.py
```
5. Por fim, execute o seguinte comando para compilar o código:
```
python .\compiler.py <arquivo>
```
6. Será gerado um arquivo `arquivo.cpp` com o código convertido para cpp. Após isso, basta usar o compilador GCC para executá-lo.
