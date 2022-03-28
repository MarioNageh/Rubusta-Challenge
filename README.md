[TOC]
# Rubusta Challenge

# First You go to
> InitData/init_data.py
# Run This Script To Insert First Admin
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




