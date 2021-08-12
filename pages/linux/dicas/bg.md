# Processos em background

## [Home](../../../index.md) | [Linux](../index.md)

Nas distribuições linux, quando executamos um processo pelo terminal, por padrão, ele fica atrelado a este terminal, exibindo as mensagens de log. 

Para executar um comando, deixando o processo desatrelado do terminal, ou seja, em background, basta digitar o caractere & após o comando:

Ex.:
```bash
$comando &
[1] 10588
$
```
A saída do comando ira exibir o PID do processo.

Para atrelar o processo em execução para o foreground, ou seja, atrelá-lo ao terminal, basta usar o comando fg:

Ex.:
```bash
$fg
[1] + 10588 running comando

```
A partir deste momento, os logs do processos passarão a ser exibidos no terminal.