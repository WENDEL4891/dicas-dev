### Gerenciando o arquivo settings para ambientes diferentes

#### [Home](../../../index.md) | [Django](../index.md)

Para configurar o projeto, para ambientes diferentes, basta criar um diretório __settings/__, dentro do diretório raiz do projeto. Dentro deste diretório, devem ser criados os seguintes arquivos:

```
settings/
    __init__.py
    base.py
    local.py
    pro.py
```
- pro.py: conterá as definições para o ambiente de produção.
- local.py: conterá as definições para o ambiente local.
- base.py: conterá as definições gerais, válidas para todos os ambientes.

---

No arquivo base.py, deve-se substituir a definição da constante BASE_DIR. Antes, esta constante estava definida no arquivo settings.py. O arquivo base.py encontra-se dentro do diretório settings/, o qual está substituindo o arquivo settings.py. Desse modo, a constante deverá remeter ao __parent__ do arquivo base.py, que é o diretório settings/, do seguinte modo:

```
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```
__**Obs. A definição anterior era BASE_DIR = Path(__file__).resolve().parent.parent. Assim, a nova definição faz menção ao parent do arquivo base.py, que é o diretório settings.**__

---

O arquivo settings.py deve conter o seguinte:

```
from .base import *

DEBUG = True

SECRET_KEY = '<secret_key_generated_by_django>'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
_**Obs. Definições conforme cada projeto, é claro.**_

---

O arquivo pro.py deve conter o seguinte:

```
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<secret_key_generated_by_django>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
    ('<nome_do_administrador do projeto>', 'admin@gmail.com')
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        <definicoes_definidas_para_a_producao>
    }
}
```

---
### Após estas configurações, a ferramenta manage.py, para funcionar, precisará ser executada com a flag --settings, do seguinte modo:

```
python manage.py command --settings nome_do_projeto.settings.local
```
__**Obs. nome_do_projeto.settings.local, nome_do_projeto.settings.pro, ou outro, conforme cada ambiente.**__

Uma alternativa mais viável é definir uma variável de ambiente, DJANGO_SETTINGS_MODULE, com o valor nome_do_projeto.settings.pro (ou nome_do_projeto.settings.local; ou outro, conforme o caso).