import webbrowser


def get_access_token(client_id: int, scope: int) -> None:
    assert isinstance(client_id, int), 'clinet_id must be positive integer'
    assert isinstance(scope, str), 'scope must be string'
    assert client_id > 0, 'clinet_id must be positive integer'
    url = """\
    https://oauth.vk.com/authorize?client_id={client_id}&\
    redirect_uri=https://oauth.vk.com/blank.hmtl&\
    scope={scope}&\
    &response_type=token&\
    display=page\
    """.replace(" ", "").format(client_id=client_id, scope=scope)
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    print('Введите идентификатор вашего standalone приложения вк')
    client_id = int(input())

    get_access_token(client_id, 'friends')
    print('''Из окна браузера скопируйте токен в директорию .env,
    сохраните его как переменную TOKEN''')