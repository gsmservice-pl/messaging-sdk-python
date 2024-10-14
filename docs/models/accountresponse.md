# AccountResponse

An object containing information about the User's account and balance


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `login`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | User Login                                               | some_login                                               |
| `account_type`                                           | [Optional[models.AccountType]](../models/accounttype.md) | :heavy_minus_sign:                                       | Account type                                             | PRE-PAID                                                 |
| `limit`                                                  | *Optional[float]*                                        | :heavy_minus_sign:                                       | Acount limit                                             | 0                                                        |
| `credit`                                                 | *Optional[float]*                                        | :heavy_minus_sign:                                       | Current account balance                                  | 130.44                                                   |
| `subcredit`                                              | *OptionalNullable[float]*                                | :heavy_minus_sign:                                       | Subaccount credit balance (null if unlimited)            | 65.32                                                    |
| `currency`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | Account currency                                         | PLN                                                      |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | User name and surname                                    | Andrzej Nowak                                            |
| `is_main`                                                | *Optional[bool]*                                         | :heavy_minus_sign:                                       | Is main account?                                         | true                                                     |