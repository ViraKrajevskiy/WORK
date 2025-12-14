
Проект автоматизирует тестирование логина на сайте [https://www.saucedemo.com/](https://www.saucedemo.com/).

Проверяются 5 сценариев:
1. Успешный логин (standard_user)
2. Неверный пароль
3. Заблокированный пользователь (locked_out_user)
4. Пустые поля
5. Performance glitch user (performance_glitch_user)

## Установка

1. Клонировать репозиторий:
```bash
git clone <repo_url>
cd aqa_saucedemo
