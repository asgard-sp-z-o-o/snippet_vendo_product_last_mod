# Ostatnia modyfikacja towaru

### Zasady działania


**Ogólne zasady:** Skrypt pobiera listę produktów, które zostały ostatnio zmodyfikowane - pomija zmianę stanu magazynowego.
### Przed uruchomieniem

**Wymagane pliki:** Przed uruchomieniem należy utworzyć plik "settings.ini" i uzupełnić dane do logowania Vendo i poczty:

```ini
[vendo]
set_api = http://vendo_adres:port
set_api_test = http://vendo_adres_test:port
login_api = api_login
pass_api = api_password
login_user = user_login
pass_user = user_password

```
