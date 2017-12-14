# Accounts

## Account Types

Group | Account Types
----- | -------------
`Cash`| checking, savings, money market
`Debt` | autos creditline home loan student_loans
`Investment` | investment
`Asset` | asset cd
`Credit card` | cards
`Bill` | bill

## Get Accounts

```shell
curl -X "GET" "http://partner.url/api/v2/users/:user_id:/accounts" -u "%geezeo-api-key%"
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts')
key = '%geezeo-api-key%'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth key,''

  response = http.request request

  puts response.body
end
```

```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id";
var sdk = new SDK(apiKey, url, userId);
var accounts = sdk.GetAccounts();
```

> Response payload

```json
{
  "accounts": [
    {
      "id": 42,
      "name": "eChecking",
      "balance": "300.54",
      "reference_id": "789274930",
      "aggregation_type": "cashedge",
      "state": "active",
      "harvest_updated_at": "2013-03-05T12:00:00Z",
      "account_type": "checking",
      "include_in_expenses": true,
      "include_in_budget": true,
      "include_in_cashflow": true,
      "include_in_dashboard": true,
      "include_in_goals": true,
      "include_in_networth": true,
      "fi": {
        "id": 2,
        "name": "CashEdge Test Bank (Agg) - Retail Non 2FA"
      },
      "error": {
        "message": "There was an error.",
        "code": "300",
        "actionable": true
      },
      "cashedge_account_type": {
        "name": "Savings",
        "acct_type": "SDA",
        "ext_type": "SDA",
        "group": "Cash"
      },
      "other_balances" : {
        "balance_type": "current",
        "balance" : "300.54"
      }
    }
  ]
}
```

Return a list of accounts for the given user (this will exclude non-classified CashEdge accounts).

`GET /api/v2/users/:user_id:/accounts`

###Status Codes

Status | Description
------ | -----------
200 OK | returned when successful
401 Not Authorized | returned when invalid credentials are provided
404 Not Found | returned when an invalid user is specified

## Get All Accounts

```shell
curl -X "GET" "http://partner.url/api/v2/users/:user_id:/accounts/all" -u "%geezeo-api-key%"
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts/all')
key = ':geezeo-aip-key:'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth key,''

  response = http.request request

  puts response.body
end

```

```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id"
var sdk = new SDK(apiKey, url, userId);
var accounts = sdk.GetAllAccounts();

```


> Response payload

```json
{
  "accounts": [
    {
      "id": 42,
      "name": "eChecking",
      "balance": "300.54",
      "reference_id": "789274930",
      "aggregation_type": "cashedge",
      "state": "active",
      "harvest_updated_at": "2013-03-05T12:00:00Z",
      "account_type": "checking",
      "include_in_expenses": true,
      "include_in_budget": true,
      "include_in_cashflow": true,
      "include_in_dashboard": true,
      "include_in_goals": true,
      "include_in_networth": true,
      "fi": {
        "id": 2,
        "name": "CashEdge Test Bank (Agg) - Retail Non 2FA"
      },
      "error": {
        "message": "There was an error.",
        "code": "300",
        "actionable": true
      },
      "cashedge_account_type": {
        "name": "Savings",
        "acct_type": "SDA",
        "ext_type": "SDA",
        "group": "Cash"
      }
    }
  ]
}
```

Return a list of accounts for the given user (this will exclude non-classified CashEdge accounts).

`GET /api/v2/users/:user_id:/accounts/all`

###Status Codes

Status | Description
------ | -----------
200 OK | returned when successful
401 Not Authorized | returned when invalid credentials are provided
404 Not Found | returned when an invalid user is specified

## Get Potential Cashflow Accounts

```shell
curl -X "GET" "http://partner.url/api/v2/users/:user_id:/accounts/potential_cashflow" -u "%geezeo-api-key%"
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts/potential_cashflow')
key = ':geezeo-aip-key:'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth key,''

  response = http.request request

  puts response.body
end

```

```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id";
var sdk = new SDK(apiKey, url, userId);
var accounts = sdk.GetPotentialCashflowAccounts();
```


> Response payload

```json
{
  "accounts": [
    {
      "id": 42,
      "name": "eChecking",
      "balance": "300.54",
      "reference_id": "789274930",
      "aggregation_type": "cashedge",
      "state": "active",
      "harvest_updated_at": "2013-03-05T12:00:00Z",
      "account_type": "checking",
      "include_in_expenses": true,
      "include_in_budget": true,
      "include_in_cashflow": true,
      "include_in_dashboard": true,
      "include_in_goals": true,
      "include_in_networth": true,
      "fi": {
        "id": 2,
        "name": "CashEdge Test Bank (Agg) - Retail Non 2FA"
      },
      "error": {
        "message": "There was an error.",
        "code": "300",
        "actionable": true
      },
      "cashedge_account_type": {
        "name": "Savings",
        "acct_type": "SDA",
        "ext_type": "SDA",
        "group": "Cash"
      }
    }
  ]
}
```

Return a list of accounts for the given user (this will exclude non-classified CashEdge accounts).

`GET /api/v2/users/:user_id:/accounts`

###Status Codes

Status | Description
------ | -----------
200 OK | returned when successful
401 Not Authorized | returned when invalid credentials are provided
404 Not Found | returned when an invalid user is specified


## Get Account

```shell
curl -X "GET" "http://partner.url/api/v2/users/:user_id:/accounts/:account_id:" -u "%geezeo-api-key%"
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts/:account_id:')
key = ':geezeo-aip-key:'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth key,''

  response = http.request request

  puts response.body
end

```


```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id";
int accountId = account_id;
var sdk = new SDK(apiKey, url, userId);
var accounts = sdk.GetAccountById(accountId);

```


> Response payload

```json
{
  "accounts": [
    {
      "id": 42,
      "name": "eChecking",
      "balance": "300.54",
      "reference_id": "789274930",
      "aggregation_type": "partner",
      "state": "active",
      "harvest_updated_at": "2013-03-05T12:00:00Z",
      "account_type": "checking",
      "include_in_expenses": true,
      "include_in_budget": true,
      "include_in_cashflow": true,
      "include_in_dashboard": true,
      "include_in_goals": true,
      "include_in_networth": true,
      "fi": {
        "id": 2,
        "name": "CashEdge Test Bank (Agg) - Retail Non 2FA"
      },
      "cashedge_account_type": {
        "name": "Savings",
        "acct_type": "SDA",
        "ext_type": "SDA",
        "group": "Cash"
      }
    }
  ]
}
```

Return a list of accounts for the given user (this will exclude non-classified CashEdge accounts).

`GET /api/v2/users/:user_id:/accounts/:account_id:`

###Status Codes

Status | Description
------ | -----------
200 OK | returned when successful
401 Not Authorized | returned when invalid credentials are provided
404 Not Found | returned when an invalid user is specified

## Get Account Investments

```shell
curl -X "GET" "http://partner.url/api/v2/users/:user_id:/accounts/:account_id:/investments" -u "%geezeo-api-key%"
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts/:account_id:/investments')
key = ':geezeo-aip-key:'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth key,''

  response = http.request request

  puts response.body
end

```

```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id";
int accountId = account_id;
var sdk = new SDK(apiKey, url, userId);
var accounts = sdk.GetInvestmentsByAccountId(accountId);

```

> Response payload

```json
{
  "other_balances": [
    {
      "balance_type": "Mmf",
      "description": "MMF",
      "balance": "234.12"
    }
  ],
  "positions": [
    {
      "shares": "1.0",
      "price": "485.63",
      "market_value": "485.63",
      "ticker": {
        "symbol": "AAPL",
        "name": "Apple Inc."
      }
    }
  ]
}
```


Return investment data for the given account.


`GET /api/v2/users/:user_id:/accounts/:account_id:/investments`

### Balance Types

| Type | Description |
|------|-------------|
| `TotalBrokerageAccountValue` | Total Brokerage Account Value |
| `Securities` | Securities |
| `Cash` | Cash |
| `Mmf` | MMF |
| `BuyingPower` | Buying Power |
| `MarginBalance` | Margin Balance |
| `CurrentVestedBalance` | Current Vested Balance |
| `TotalAmountOfCompanyMatch` | Company Matching Amount |
| `TotalAmountOfContributions` | Total Contributions |
| `DeferralPercentage` | Deferral Percentage |
| `LoanAmount` | Loan Amount |
| `DeathBenefit` | Death Benefit |
| `CashSurrenderValue` | Cash Surrender Value |
| `InsurancePremium` | Insurance Premium |
| `EmployerProfitsSharing` | Employer Profits Sharing |
| `DailyChange` | Daily Change |
| `PercentageChange` | Percentage Change |
| `ContinuousYears` | Continuous Years |
| `InterestRate` | Interest Rate |

###Status Codes

Status | Description
------ | -----------
200 OK | returned when successful
401 Not Authorized | returned when invalid credentials are provided
404 Not Found | returned when an invalid user is specified

## Update Account

```shell
curl -X "PUT" "http://partner.url/api/v2/users/:user_id:/accounts/:account_id:" -u "%geezeo-api-key%" -d ":request_payload:"
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts/:account_id:')
key = ':geezeo-aip-key:'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Put.new uri.request_uri
  request.basic_auth key,''
  request.body = :request_payload:

  response = http.request request

  puts response.body
end

```

```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id";
int accountId = account_id;
var sdk = new SDK(apiKey, url, userId);
var accountToUpdate = new Account
{
	Name = "Renamed Checking"
};

var accountRequest = new AccountRequestModel {Account = accountToUpdate};

bool response = sdk.UpdateAccount(accountId, accountRequest); //returns a bool indicating whether delete was successful


```


> Request Payload

```json
{
  "account": {
    "name": "Joint Checking"
  }
}
```


Update an account for the given user.


### Parameters

| Parameter | Description |
|-----------|-------------|
| `name` | The name of the account. |

### Status Codes

| Status | Description |
|--------|-------------|
| 204 No Content | returned when successful |
| 401 Not Authorized | returned when invalid credentials are provided |
| 404 Not Found | returned when an invalid user is specified |


## Delete Account

```shell
curl -X "DELETE" "http://partner.url/api/v2/users/:user_id:/accounts/:account_id:" -u "%geezeo-api-key%""
```

```ruby
uri = URI('https://partner.url/api/v2/users/:user_id:/accounts/:account_id:')
key = ':geezeo-aip-key:'

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https') do |http|

  request = Net::HTTP::Delete.new uri.request_uri
  request.basic_auth key,''

  response = http.request request

  puts response.body
end

```

```csharp
var apiKey = "geezeo-api-key";
var url = "partner.url";
var userId = "user_id";
int accountId = account_id;
var sdk = new SDK(apiKey, url, userId);
bool deleted = sdk.DeleteAccount(accountId); //returns a bool indicating whether delete was successful
```

Delete an account for the given user.

### Request

`DELETE /api/v2/users/:user_id:/accounts/:account_id:`

### Status Codes

| Status | Description |
|--------|-------------|
| `204 No Content` | returned when successful |
| `401 Not Authorized` | returned when invalid credentials are provided |
| `404 Not Found` | returned when an invalid user is specified |

## Error Codes

In the event you run into an error code for an account refer to the following error codes.

### User Failure

| Failure Category               | Error Code | Description                                        |
|--------------------------------|------------|----------------------------------------------------|
| Login Failure                  |            |                                                    |
|                                | 300        | Login Failure                                      |
|                                | 301        | Login Failure - Invalid Login Credentials          |
|                                | 305        | Invalid Client or Account Identifier               |
|                                | 306        | Incorrect FI Selection                             |
|                                | 307        | Account Locked                                     |
|                                | 701        | Add attempt did not retrieve any accounts          |
| MFA Failure                    |            |                                                    |
|                                | 303        | Additional information required for authentication |
|                                | 304        | Incorrect answer provided for challenge questions  |
| Account Classification Failure |            |                                                    |
|                                | 209        | Incorrect Account Type classification              |
| Account Identification Failure |            |                                                    |
|                                | 201        | Site Change - Account maintenance needed           |
|                                | 203        | Account not found                                  |
|                                | 204        | Account no longer exists                           |
| User Attention Required at FI  |            |                                                    |
|                                | 302        | Website Attention required                         |

### FI Website Failure

| Failure Category   | Error Code | Description                          |
|--------------------|------------|--------------------------------------|
| FI Website Failure |            |                                      |
|                    | 103        | Un-existing URL (or) network failure |
|                    | 104        | Time out error                       |
|                    | 105        | Target server error or server down   |
|                    | 106        | Connection failed                    |
|                    | 107        | SSL Error                            |
|                    | 108        | Server error (FI website intense)    |
|                    | 109        | Client error                         |
|                    | 110        | Account Information unavailable      |

### Script / Software Failure

| Failure Category    | Error Code | Description                                       |
|---------------------|------------|---------------------------------------------------|
| Layout Failure      |            |                                                   |
|                     | 100        | Internal software error                           |
|                     | 200        | Site change                                       |
|                     | 202        | Account identification failure - multiple matches |
|                     | 205        | Account identification failure - no accounts      |
|                     | 311        | Harvest failure                                   |
| Software Failure    |            |                                                   |
|                     | 400        | Database update failure                           |
|                     | 999        | Internal software error - unknown error           |
| Account Not Updated |            |                                                   |
|                     | 121        | Account is not updated                            |
