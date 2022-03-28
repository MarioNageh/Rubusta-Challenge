# Rubusta Challenge
# Setup run this commads
> -> python -m venv env 
->  activae the env
-> pip install -r req.txt
-> here in setting file there two Connection To DataBase mysql,SqlLite , if you need mysql un comment code and  fill your credential 
-> python manage.py makemigrations
-> python manage.py migrate

# For Testing 
> python manage.py test

# First You go to
>  InitData/init_data.py
# Run This Script To Insert First Admin and create 5 employee if you need real test
> Admin@Rubusta.com 
> 1234
# I Have Attach Postman Collection
>Rubosta.postman_collection.json 
to Test Login Request In This Commit
in tesing via post man we send password as Plain Text
until Build the Fornt Will Hash it and Send it to backend



## Login
- Method: POST

- URI

  > /login/

- Parameters

  | Field      | Type   | Description                   |
  | ---------- | ------ | ----------------------------- |
  | email      | String | Admin Email.              |
  | password   | String | The Plain Password As Text  |
 
- Response

  - Success

    | Field   | Type    | Description                |
    | ------- | ------- | -------------------------- |
    | code      | String  | Response code              |
    | MessageEn | String  | Response message           |
    | MessageAr | String  | Response message            |
    | Token    | String | Token  |

    Example
  
    ```
    {
    "Code": 200,
    "MessageEn": "Successful Login",
    "MessageAr": "تم تسجيل الدخول بنجاح",
    "Token": "eyJTaWduZWRCeSI6ICJNYXJpbyJ9.eyJJZEFkbWluIjogMiwgIlVzZXJOYW1lIjogIlJ1YnVzdGEgQWRtaW4iLCAiRmlyc3ROYW1lIjogIlJ1YnVzdGEiLCAiTGFzdE5hbWUiOiAiQWRtaW4iLCAiTWFpbCI6ICJBZG1pbkBSdWJ1c3RhLmNvbSIsICJFeHBpcmVkIjogMTY1MTA1NDQ1MC4wMDQ0NTF9.2221d95a5c70bdb9bf81bd8a6205b43fd3a910549fa6df180e711f6eacaf5e09"
}
    ```
  
    Note
  
    > Token String in JWT format.
  
  - Failed
  
    | Field   | Type    | Description                |
    | ------- | ------- | -------------------------- |
    | code      | String  | Response code              |
    | MessageEn | String  | Response message           |
    | MessageAr | String  | Response message            |
  
    Example
  
    ```{
    "Code": 401,
    "MessageEn": "Wrong Username or Password try again",
    "MessageAr": "عفوا يوجد خطا في اسم المستخدم او كلمة السر"
}
    ```



## Salary
- Method: GET

- URI

  > /salary/
- example /salary/?month=12a&year=2022
- Parameters Url Params

  | Field      | Type   | Description                   |
  | ---------- | ------ | ----------------------------- |
  | month      | String | A Month Number As 6              |
  | year       | String | A Year Number As 2022  |
 
- Response

  - Success

    | Field   | Type    | Description                |
    | ------- | ------- | -------------------------- |
    | code      | String  | Response code              |
    | MessageEn | String  | Response message           |
    | MessageAr | String  | Response message            |
    | Month    | String | Month   |
    | Salaries_payment_day    | String | Salaries_payment_day  |
    | Bonus_payment_day    | String | Bonus_payment_day  |
    | Salaries_total    | String | Salaries_total  |
    | Bonus_total    | String | Bonus_total  |
    | Payments_total    | String | Payments_total  |

    Example
  
    ```{
    "Code": 200,
    "MessageEn": "Successful Generated Report",
    "MessageAr": "تم نجهيز التقرير بنجاح",
    "Month": "June",
    "Salaries_payment_day": "30",
    "Bonus_payment_day": "15",
    "Salaries_total": "$10030.0",
    "Bonus_total": "$1003.0",
    "Payments_total": "$11033.0"
}
    ```
  

  
  - Failed
  
    | Field   | Type    | Description                |
    | ------- | ------- | -------------------------- |
    | code      | String  | Response code              |
    | MessageEn | String  | Response message           |
    | MessageAr | String  | Response message            |
  
    Example
  
    ```{
    "Code": 403,
    "MessageEn": "You Must Pass Invalid Month,Year",
    "MessageAr": "يجب ان يكون الشهر و السنة صحيح"
}
    ```
    




