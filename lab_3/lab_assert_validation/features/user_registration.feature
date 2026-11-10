Feature: Реєстрація користувача

  Scenario: Коректні дані користувача
    Given користувач вводить email "student@example.com"
    And користувач вводить пароль "password1"
    And користувачу 20 років
    When система перевіряє реєстраційні дані
    Then реєстраційні дані повинні бути прийняті

  Scenario: Email без частини після символу @
    Given користувач вводить email "student@"
    And користувач вводить пароль "password1"
    And користувачу 20 років
    When система перевіряє реєстраційні дані
    Then система повинна відхилити дані з помилкою "Email is invalid"

  Scenario: Пароль занадто короткий
    Given користувач вводить email "student@example.com"
    And користувач вводить пароль "pass1"
    And користувачу 20 років
    When система перевіряє реєстраційні дані
    Then система повинна відхилити дані з помилкою "Password must contain at least 8 characters"

  Scenario: Вік занадто малий
    Given користувач вводить email "student@example.com"
    And користувач вводить пароль "password1"
    And користувачу 17 років
    When система перевіряє реєстраційні дані
    Then система повинна відхилити дані з помилкою "Age must be between 18 and 120"