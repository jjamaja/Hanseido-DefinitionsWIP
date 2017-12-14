# Push Data Source

Geezeo provides robust transaction enrichment for partner and aggregated
accounts. The first step in any implementation is connecting the platform to a
data source for all partner accounts.

Geezeo provides a Push Data Source mechanism for integrations that require
real-time data enrichment.

Geezeo’s Push Data Source allows partners to asynchronously submit transactions
via a batch JSON interface.

Each request submitted to the Push Data Source should provide a callback URL
where the results will be returned to. Once the Geezeo platform has completed
processing the batch, the platform will call back the URL with the results.

All requests to and from the Push Data Source will use JWT tokens to validate
authenticity as well as forced TLS with certificate validation.

Initial queuing requests will also respond with a unique token for that batch.
That token will also be on the response. That token should be used to tracking
and troubleshooting.

All data provided to this interface is considered an upsert and will replace the
data in the Geezeo platform.

## Callback URL

Requests should include a callback URL. Once the Geezeo platform has completed
processing the submitted batch, the platform will call the callback URL with the
payload in the POST body.

The request will come with a JWT token to ensure authenticity.

## Push Batch of Data

> Sample request

```json
{
  "callback": "https://url.to.post.to/",
  "users": [
    {
      "partner_customer_id": "1234",
      "first_name": "Firstname",
      "last_name": "Lastname",
      "email": "flastname@geezeo.com",
      "zip_code": "06000",
      "accounts": [
          {
            "reference_id": "13579",
            "name": "Savings",
            "account_type": "savings",
            "account_balances": [
              {
                "balance_type": "current",
                "balance_amount": "2591.71"
              }
            ],
            "transactions": [
              {
                "balance": "-112.03",
                "memo": "DUNKINDONUTS*100094",
                "posted_at": "2009-03-19T11:40:50-04:00",
                "reference_id": "4567",
                "transaction_type": "debit"
              }
            ]
          }
      ]
    }
  ]
}
```

> Sample response

```json
{
  "batch_id": "4403f9f7-0b0b-484e-b73b-bf948ecd2b9f"
}
```

> Sample callback

```json
{
  "batch" : {
    "batch_id": "4403f9f7-0b0b-484e-b73b-bf948ecd2b9f",
    "status": "success",
    "totals": {
      "users": {
        "total": 1,
        "success": 1,
        "error": 0
      },
      "accounts" : {
        "total": 1,
        "success": 1,
        "error": 0
      },
      "transactions" : {
        "total": 1,
        "success": 1,
        "error": 0
      }
    }
  },
  "users": [
    {
      "user_id": "10000001",
      "partner_customer_id": "1234",
      "first_name": "Firstname",
      "last_name": "Lastname",
      "email": "flastname@geezeo.com",
      "zip_code": "06000",
      "accounts": [
          {
            "account_id": "20000001",
            "reference_id": "13579",
            "name": "Savings",
            "account_type": "savings",
            "account_balances": [
              {
                "balance_type": "current",
                "balance_amount": "2591.71"
              }
            ],
            "transactions": [
              {
                "transaction_id": "2009_03_19_4567_20000001",
                "balance": "-112.03",
                "memo": "DUNKINDONUTS*100094",
                "posted_at": "2009-03-19T11:40:50-04:00",
                "reference_id": "4567",
                "transaction_type": "Debit",
                "original_name": "DUNKINDONUTS*100094",
                "nickname": "Dunkin Donuts",
                "tags": [
                  {
                    "name": "Coffee",
                    "balance": 112.03
                  }
                ]
              }
            ]
          }
      ]
    }
  ]
}
```

Create or update one or more users, accounts, or transactions in bulk.

`PUT /api/v2/batches`

### Status Codes

| Status             | Description |
|--------------------|-------------|
| 200 OK             | returned when a batch was submitted successfully |
| 400 Bad Request    | returned when no batch content is provided |
| 401 Not Authorized | returned when invalid credentials are provided |


### User Properties

| Property            | Required | Description |
|---------------------|----------|-------------|
| partner_customer_id | Yes      | Identifier of the user, unique to the submitter |
| first_name          | Yes      | First name/given name of the user |
| last_name           | Yes      | Last name/family name of the user |
| email               | Yes      | Email address |
| zip_code            | No       | ZIP code |
| accounts            | No       | Array of accounts, as defined in Account Properties |

### User Result Properties

On callback, additional properties may be returned in a user.

| Property | Description |
|----------|-------------|
| user_id  | Geezeo user identifier |

### Account Properties

| Property         | Required | Description |
|------------------|----------|-------------|
| reference_id     | Yes      | Identifier of the account, unique to the submitter |
| name             | No       | Account name, as defined by the user |
| account_type     | Yes      | Account type; allowed values are below |
| account_balances | Yes      | Array of account balances, as defined in Account Balance Properties |
| transactions     | No       | Array of transactions, as defined in Transaction Properties |

### Account Result Properties

On callback, additional properties may be returned in an account.

| Property   | Description |
|------------|-------------|
| account_id | Geezeo account identifier |

### Account Balance Properties

| Property       | Required | Description |
|----------------|----------|-------------|
| balance_type   | Yes      | Type of balance; allowed values are 'current', 'available' |
| balance_amount | Yes      | Amount |

### Transaction Properties

| Property         | Required | Description |
|------------------|----------|-------------|
| balance          | Yes      | Amount of the transaction, where credits are positive and debits are negative |
| check_number     | No       | If the transaction was a check, a check number |
| hide             | No       | If the transaction should be hidden from the user interface, set to true |
| memo             | No       | Transaction memo |
| nickname         | No       | The user-assigned transaction memo |
| posted_at        | Yes      | An ISO-8601 date (YYYY-MM-DD) or date-time (YYYY-MM-DDTHH:MM:SS-00:00) that the transaction was posted|
| reference_id     | Yes      | Unique identifier of the transaction within the account |
| transaction_type | No       | Set to "credit" or "debit", and must match how "amount" is signed |

### Transaction Result Properties

On callback, additional properties may be returned in a transaction.

| Property       | Description |
|----------------|-------------|
| tags           | List of tags that have been assigned to the transaction, with corresponding amounts that will total the amount of the transaction |
| transaction_id | Geezeo transaction identifier |
| original_name  | The transaction memo, exactly as it was provided to the API |

### Account Types

| Account Type  |
|---------------|
| asset         |
| autos         |
| bill          |
| cards         |
| cd            |
| certificates  |
| checking      |
| creditline    |
| home          |
| investment    |
| loan          |
| money_market  |
| savings       |
| student_loans |


## Get Batch Status

```shell
curl -X "GET" "http://partner.url/api/v2/batches/{batch_id}" --header 'Authorization: Bearer x'
```

`GET /api/v2/batches/{batch_id}`

> Response payload

```json
{
  "batch_id": "4403f9f7-0b0b-484e-b73b-bf948ecd2b9f",
  "status": "partial-success",
  "totals": {
    "users": {
      "total": 1,
      "success": 1,
      "error": 0
    },
    "accounts": {
      "total": 1,
      "success": 1,
      "error": 0
    },
    "transactions": {
      "total": 2,
      "success": 1,
      "error": 1
    }
  },
  "errors": [
    {
      "context": "transaction",
      "identifier": "4567",
      "message": "Missing posted_at"
    }
  ]
}
```

Retrieve the status of a submitted push batch.

### Status Codes

| Status             | Description |
|--------------------|-------------|
| 200 OK             | returned when a a batch was found and returned successfully |
| 401 Not Authorized | returned when invalid credentials are provided |
| 404 Not Found      | returned when the requested batch was not found |

### Batch Data Properties

| Property |  Description |
|----------|--------------|
| batch_id | Batch ID |
| status   | Status of processing; allowed values are 'new', 'processing', 'success', 'partial-success', or 'error'. A batch that is ingested, but with some data errors, will come back as 'partial-success'. A batch that is ingested without errors will come back as 'success'. |
| totals   | Object containing statuses of the three data types allowed in a push request; 'users', 'accounts', and 'transactions' |
| errors   | List of errors, if any |

### Totals Properties

| Property |  Description |
|----------|--------------|
| total    | Number of items received in the batch |
| success  | Number of items processed successfully |
| error    | Number of items processed with errors |

### Error Description Properties

| Property   |  Description |
|------------|--------------|
| context    | The object type where the error was found; allowed values are 'user', 'account', or 'transaction' |
| identifier | The provided identifier for that object, 'partner_customer_id' for user, 'reference_id' for 'account' or 'transaction' |
| message    | Description of the error |



## Get Completed Batch Content

```shell
curl -X "GET" "http://partner.url/api/v2/batches/{batch_id}/content" --header 'Authorization: Bearer x'
```

`GET /api/v2/batches/{batch_id}/content`

> Response payload

```json
{
  "batch" : {
    "batch_id": "4403f9f7-0b0b-484e-b73b-bf948ecd2b9f",
    "status": "success",
    "totals": {
      "users": {
        "total": 1,
        "success": 1,
        "error": 0
      },
      "accounts" : {
        "total": 1,
        "success": 1,
        "error": 0
      },
      "transactions" : {
        "total": 1,
        "success": 1,
        "error": 0
      }
    }
  },
  "users": [
    {
      "user_id": "10000001",
      "partner_customer_id": "1234",
      "first_name": "Firstname",
      "last_name": "Lastname",
      "email": "flastname@geezeo.com",
      "zip_code": "06000",
      "accounts": [
          {
            "account_id": "20000001",
            "reference_id": "13579",
            "name": "Savings",
            "account_type": "savings",
            "account_balances": [
              {
                "balance_type": "current",
                "balance_amount": "2591.71"
              }
            ],
            "transactions": [
              {
                "transaction_id": "2009_03_19_4567_20000001",
                "balance": "-112.03",
                "memo": "DUNKINDONUTS*100094",
                "posted_at": "2009-03-19T11:40:50-04:00",
                "reference_id": "4567",
                "transaction_type": "Debit",
                "original_name": "DUNKINDONUTS*100094",
                "nickname": "Dunkin Donuts",
                "tags": [
                  {
                    "name": "Coffee",
                    "balance": 112.03
                  }
                ]
              }
            ]
          }
      ]
    }
  ]
}
```

Retrieve the callback content of a submitted push batch.

### Status Codes

| Status             | Description |
|--------------------|-------------|
| 200 OK             | returned when a a batch was found and returned successfully |
| 401 Not Authorized | returned when invalid credentials are provided |
| 404 Not Found      | returned when the requested batch was not found or the batch has not completed processing |


### Properties

| Property |  Description |
|----------|--------------|
| batch    | Batch data |
| users    | User data structure |

### Batch Data Properties

| Property |  Description |
|----------|--------------|
| batch_id | Batch ID |
| status   | Status of processing; allowed values are 'new', 'processing', 'success', 'partial-success', or 'error'. A batch that is ingested, but with some data errors, will come back as 'partial-success'. A batch that is ingested without errors will come back as 'success'. |
| totals   | Object containing statuses of the three data types allowed in a push request; 'users', 'accounts', and 'transactions' |
| errors   | List of errors, if any |

### Totals Properties

| Property |  Description |
|----------|--------------|
| total    | Number of items received in the batch |
| success  | Number of items processed successfully |
| error    | Number of items processed with errors |

### Error Description Properties

| Property   |  Description |
|------------|--------------|
| context    | The object type where the error was found; allowed values are 'user', 'account', or 'transaction' |
| identifier | The provided identifier for that object, 'partner_customer_id' for user, 'reference_id' for 'account' or 'transaction' |
| message    | Description of the error |

### User Properties

| Property            | Required | Description |
|---------------------|----------|-------------|
| user_id             | Yes      | Geezeo user identifier |
| partner_customer_id | Yes      | Identifier of the user, unique to the submitter |
| first_name          | Yes      | First name/given name of the user |
| last_name           | Yes      | Last name/family name of the user |
| email               | Yes      | Email address |
| zip_code            | No       | ZIP code |
| accounts            | No       | Array of accounts, as defined in Account Properties |

### Account Properties

| Property         | Required | Description |
|------------------|----------|-------------|
| account_id       | Yes      | Geezeo account identifier |
| reference_id     | Yes      | Identifier of the account, unique to the submitter |
| name             | No       | Account name, as defined by the user |
| account_type     | Yes      | Account type; allowed values are above |
| account_balances | Yes      | Array of account balances, as defined in Account Balance Properties |
| transactions     | No       | Array of transactions, as defined in Transaction Properties |

### Account Balance Properties

| Property       | Required | Description |
|----------------|----------|-------------|
| balance_type   | Yes      | Type of balance; allowed values are 'current', 'available' |
| balance_amount | Yes      | Amount |

### Transaction Properties

| Property         | Required | Description |
|------------------|----------|-------------|
| transaction_id   | Yes      | Geezeo transaction identifier |
| balance          | Yes      | Amount of the transaction, where credits are positive and debits are negative |
| check_number     | No       | If the transaction was a check, a check number |
| hide             | No       | If the transaction should be hidden from the user interface, set to true |
| memo             | No       | Transaction memo |
| nickname         | No       | The user-assigned transaction memo |
| original_name    | Yes      | The transaction memo, exactly as it was provided to the API |
| posted_at        | Yes      | An ISO-8601 date (YYYY-MM-DD) or date-time (YYYY-MM-DDTHH:MM:SS-00:00) that the transaction was posted|
| reference_id     | Yes      | Unique identifier of the transaction within the account |
| tags             | No       | List of tags that have been assigned to the transaction, with corresponding amounts that will total the amount of the transaction |
| transaction_type | No       | Set to "credit" or "debit", and must match how "amount" is signed |
