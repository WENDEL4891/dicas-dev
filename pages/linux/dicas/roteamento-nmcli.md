### Roteamento com nmcli

#### [Home](../../../index.md) | [Linux](../index.md)


Abra o modo interativo nmcli para a conexão example:

```$ sudo nmcli connection edit <nome_da_conexao>```
Acrescente a rota estática:

```nmcli> set ipv4.routes <ip_da_rede/CIDR> <id_de_destino>```

Ex.

```nmcli> set ipv4.routes 192.0.2.0/24 198.51.100.1```

Opcionalmente, verificar se as rotas foram adicionadas corretamente à configuração:

```
nmcli> print
...
ipv4.routes:        { ip = 192.0.2.1/24, nh = 198.51.100.1 }
...
```

O atributo ip exibe a rede para rotear e o atributo nh atribui o gateway (próximo salto).

Salvar a configuração:

```nmcli> save persistent```

Reiniciar a conexão de rede:

```nmcli> activate example```

**ATENÇÃO**
**Quando você reiniciar a conexão, todas as conexões que atualmente utilizam esta conexão serão temporariamente interrompidas.**

Deixe o modo interativo nmcli:

```nmcli> quit```

Opcionalmente, verificar se a rota está ativa:

```
$ ip route
...
192.0.2.0/24 via 198.51.100.1 dev example proto static metric 100
```

As informações sobre a nova rota pode ser vista no arquivo de configuração da conexão do NetworkManager:

```etc/NetworkManager/system-connections```

**Recursos adicionais**

Para obter a lista de comandos disponíveis no modo interativo, digite help na shell interativa.