from vendoasg.vendoasg import Vendo
import configparser
import datetime
config = configparser.ConfigParser()
config.read('settings.ini', encoding='utf-8')
vendoApi = Vendo(config['vendo']['set_api'])
vendoApi.logInApi(config['vendo']['login_api'], config['vendo']['pass_api'])
vendoApi.loginUser(config['vendo']['login_user'], config['vendo']['pass_user'])
data_dzis = datetime.date.today()
data_dzis = str(data_dzis)


def last_modyfi():
    towar_query = vendoApi.getJson(
        '/json/reply/Magazyn_Towary_Lista',
        {
            "Token": vendoApi.USER_TOKEN,
            "Model":
                {
                    "Aktywnosci": ["Aktywny"],
                    "Rodzaje1": ["Towar"],
                    "DataCzasModyfikacji": data_dzis,
                    "DataCzasModyfikacjiTyp": "Rekordu",
                    "Strona":
                        {
                            "Indeks": 0,
                            "LiczbaRekordow": 1000
                        }
                }
        }
    )
    towar_query = towar_query["Wynik"]["Rekordy"]
    print(len(towar_query))
    for towar in towar_query:
        print(towar["Kod"])


if __name__ == '__main__':
    last_modyfi()