# Data Source Setup

Geezeo provides robust transaction enrichment for partner and aggregated accounts. The first step in any implementation is connecting the platform to a data source for all partner accounts.

Geezeo provides a standard XML specification for harvesting transactions and accounts. Partners must provide an endpoint that meets the XML specifications below to provide data.

The Geezeo platform will harvest users data based on a predefined schedule.

Geezeo also provides a file transfer using the same XML spec. File transfers are often used in larger implementations for bulk data. This format is similar to the RequestResponse format but with a slight variation.

If a data source is setup to pull by date and the user has no transactions stored at Geezeo we will harvest exactly 90 days worth. If the user does have transactions Geezeo will harvest all transactions after the day before the account's latest transaction even if this time is greater than 90 days. In the event that the users latest harvested transaction is more than 180 days old Geezeo will not create, modify, or delete said transactions. 

## Customer User data format

> Users Request XML

```xml
<PartnerRequest
    id="2"
    sso_partner_id="abc122">
  <UserList>
    <Users>
      <User>
        <PartnerCustomerId>1234</PartnerCustomerId>
      </User>
    </Users>
  </UserList>
</PartnerRequest>
```


> Users Response XML


```xml
<PartnerResponse
    request_id="2">
  <Users>
    <User>
      <Action>New</Action>
      <PartnerCustomerId>123</PartnerCustomerId>
      <FirstName>FirstName</FirstName>
      <LastName>LastName</LastName>
      <Email>flastname@geezeo.com</Email>
      <ZipCode>06000</ZipCode>
      <UserExperience>pfm</UserExperience>
    </User>
  </Users>
</PartnerResponse>
```

> Users XML File Example

```xml
<?xml version="1.0" encoding="utf-8"?>
<Users>
  <User>
    <Details>
      <Action>New</Action>
      <PartnerCustomerId>322079353</PartnerCustomerId>
      <FirstName>RITA                </FirstName>
      <LastName>WILLIAMS                                </LastName>
      <Email>rita@williams.us</Email>
      <ZipCode>19975-3918</ZipCode>
    </Details>

  </User>
  <User>
    <Details>
      <PartnerCustomerId>322079353</PartnerCustomerId>
      <FirstName>JOE</FirstName>
      <LastName>MOMMA</LastName>
      <Email>jmomma@badjoke.com</Email>
      <ZipCode>20171     </ZipCode>
    </Details>

  </User>
  <User>
    <Details>
      <Action>Delete</Action>
      <PartnerCustomerId>322079353</PartnerCustomerId>
      <FirstName>WILLIAM</FirstName>
      <LastName>HOUSES</LastName>
      <Email>whouses@aol.com</Email>
      <ZipCode>20110     </ZipCode>
    </Details>

  </User>
</Users>
```


Geezeo will request a list of users by sending User elements containing only their PartnerCustomerIds.


Tag | Type | Usage | Description |
----|------|-------|-------------|
\<Users> | Container | Required |Contains all \<User> records in the set |
\<User> | Container | Required | Contains data defining a single customer |
\<Action> | [Enum](#ActionType)| Required | If this element is left out, Geezeo will attempt to update the record, or add it if it does not exist; specify “Delete" if the account is to be deleted |
\<PartnerCustomerId> | String (255) | Required; Unique | Unique alphanumeric ID; used to identify the customer and match accounts to it |
\<FirstName> | String (255) | Required | Customer's first name|
\<LastName> |String (255) | Required | Customer's last name |
\<Email> | String (255) | Required | Customer's email address; should be a properly formatted email address |
\<ZipCode> | String (255) | Required |Customer's zip code; should be a valid US postal code |
\<UserExperience> | String (255) | Optional |Customer user experience (PFM or TruBiz) |


## Customer Account data format

> Accounts Request XML

```xml
<PartnerRequest
    id="2"
    sso_partner_id="abc122">
  <AccountList>
      <Accounts>
        <Account>
          <PartnerCustomerId>4453</PartnerCustomerId>
        </Account>
      </Accounts>
    </AccountList>
</PartnerRequest>
```


> Accounts Response XML


```xml
<PartnerResponse
    request_id="2">
  <Accounts>
    <Account>
      <Action>NEW</Action>
      <PartnerCustomerId>12345</PartnerCustomerId>
      <AccountId>999</AccountId>
      <AccountFiName>JOHN Q PUBLIC</AccountFiName>
      <AccountNickname>John's Savings</AccountNickname>
      <AccountType>Savings</AccountType>
      <AccountBalances>
        <AccountBalance>
          <BalanceType>Current</BalanceType>
          <BalanceAmount>1999.99</BalanceAmount>
          <CurrencyCode>USD</CurrencyCode>
        </AccountBalance>
      </AccountBalances>
      <AccountExperience>pfm</AccountExperience>
    </Account>
  </Accounts>
</PartnerResponse>
```

> Accounts XML File example

```xml
<?xml version="1.0" encoding="utf-8"?>
<Accounts>

      <Account>
        <Details>
          <Action>New</Action>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000129251-S0011</AccountId>
          <AccountFiName>SUPER MONEY MARKET            </AccountFiName>
          <AccountType>savings</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>430947.36</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>
      </Account>
</Accounts>
```
Geezeo will request a list of accounts belonging to a user by sending an Account element containing only the user's PartnerCustomerId. You may optionally respond with updated account information instead of all account information. We will create any accounts that do not exist in the Geezeo database, update any accounts that do exist, and mark as closed any accounts that are in the Geezeo database but not in the response.


Tag | Type | Usage | Description |
----|------|-------|-------------|
\<Accounts> | Container | Required | Contains all \<Account> records in the set |
\<Account> | Container | Required | Contains data defining a single account |
\<Action> | [Enum](#ActionType) | Optional | If this element is left out, Geezeo will attempt to update the record, or add it if it does not exist; specify “Delete" if the account is to be deleted |
\<PartnerCustomerId> | String (255) | Required | Matches the account with the proper customer |
\<AccountId> | String (255) |Required; Unique| |Unique ID, may contain letters and numbers; used to identify the account and match transactions to it. Full credit card numbers must not be sent as the account ID. |
\<AccountNumber> | String (255) | Optional | Further identifying information show to the user in certain circumstances to help identify the account to them. Full credit card numbers must not be supplied. |
\<AccountFiName> | String (255) | Required | Account name as provided by partner |
\<AccountNickname> | String (255) | Optional |Account nickname if set by partner |
\<AccountType> | [Enum](#AccountType) | Required | Account type from closed list
\<AccountBalances> | Container | Required |Contains [\<AccountBalance>\(#AccountBalance) elements|
\<Properties> | Container | Optional | Contains [\<Property>](#Properties) elements |
\<AccountExperience> | String (255) | Optional | Account experience (PFM or Trubiz)

<a name="AccountBalance"></a>

| AccountBalance | Type | Usage | Description |
| -------------- | ---- | ----- | ----------- |
\<BalanceType> | [Enum](#BalanceType) | Required | The type of balance |
\<BalanceAmount> | Decimal | Required |The relative value of the balance type to two decimal places, e.g. 505.12 or -1110.56; a negative number should be preceded by a minus sign. Two decimal places are always required, even for .00 amounts. |
\<CurrencyCode> | [Enum](#CurrencyType) | Required | The currency code (currently only USD or CAD) |



### <a name="AccountType"></a> Account Types

| AccountType   | BalanceType |
|---------------|-------------|
| cd            | deposit     |
| checking      | deposit     |
| savings       | deposit     |
| investment    | deposit     |
| asset         | deposit     |
| money_market  | deposit     |
| cards         | credit      |
| student_loans | credit      |
| loans         | credit      |
| autos         | credit      |
| home          | credit      |
| loan          | credit      |
| creditline    | credit      |


<a name="BalanceType"></a>

For deposit AccountTypes these are the possible balance types. All deposit accounts must have at least the BalanceType 'Current' with additional BalanceTypes being optional.

### BalanceType (Deposit Accounts)

| Value Name | Usage | Description |
| ---------- | ----- | ----------- |
Current | Required | The amount currently in the account without any holds |
Available | Optional | The amount after any holds; the effective balance |

For credit AccountTypes these are the possible balance types. All credit accounts must have at least the BalanceType 'Outstanding' with additional BalanceTypes being optional.

### BalanceType (Credit Accounts)

| Value Name | Usage | Description |
| ---------- | ----- | ----------- |
CurrentLimit | Optional | Current charge limit |
AvailableCredit | Optional | Amount left to spend after any charges |
Outstanding | Required | Amount currently charged to card |
CashAdvanceLimit | Optional | Limit on cash advances |
MinimumPaymentDue | Optional | Current minimum payment due |
PreviousAmountDue | Optional | Previous minimum payment due |
PastDueAmount | Optional | Past due amount |
FinanceCharges | Optional | Finance charges for current bill |

### <a name="Properties"></a> Properties Container

The properties container is used to define non-balance based information and statistics. For example, in the future, items such as reward points, airline miles, and special promotion information would be provided through the properties container.

| Tag | Type | Usage | Description |
| --- | ---- | ----- | ----------- |
\<Property> | Container | Required | Contains property information|
\<PropertyType> | [Element](#PropertyType)| Required | The type of property in the record|
\<PropertyValue> | String (255) | Required | The property's value |

### <a name="PropertyType"></a> Property Types

| Tag | Type | Usage | Description |
| --- | ---- | ----- | ----------- |
PurchasesApr | Decimal | Optional | APR for Purchase with one decimal of precision; e.g. 24.5% would be 25.5, not .255|
PaymentDueDate | DateTime | Optional | Due date for current pay period |
InternalTransaction | String (255) | Optional | Add type to internal transaction with these possible options: “bill pay", “transfer"; added for clarity to user |

## Customer Transaction data format

> Transactions Request XML

```xml
<PartnerRequest
    id="2"
    sso_partner_id="abc122">
 <TransactionList>
    <AccountId>12345</AccountId>
    <LastTransactionId>9876</LastTransactionId>
  </TransactionList>
</PartnerRequest>
```


> Trasactions Response XML


```xml
<PartnerResponse
    request_id="2">
  <Transactions>
    <Transaction>
      <TransactionId>12345</TransactionId>
      <AccountId>9999901</AccountId>
      <TransactionType>Debit</TransactionType>
      <PostedDate>2009-03-19T11:40:50-04:00</PostedDate>
      <OriginationDate>2009-03-19T15:31:36-04:00</OriginationDate>
      <Amount>112.03</Amount>
      <Pending>true</Pending>
      <Memo>DUNKINDONUTS*100094</Memo>
    </Transaction>
  </Transactions>

</PartnerResponse>
```

> Transactions XML File example

```xml
<Transactions>

          <Transaction>
            <TransactionId>85</TransactionId>
            <AccountId>0000129251-S0011</AccountId>
            <TransactionType>Credit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>20.00</Amount>
            <Memo>AMAZON</Memo>
          </Transaction>
</Transactions>
```

Geezeo will request a list of transactions belonging to a particular account by sending a TransactionList element containing an AccountId. We may provide you with the last TransactionId that we received. In that case, please respond with only transactions newer than that transaction. If we do not provide a TransactionId (for example when adding a new user), simply respond with all transactions.


Tag | Type | Usage | Description |
--- | ---- | ----- | ----------- |
\<Transactions> | Container | Required | Contains all \<Transaction> records in the file |
\<Transaction> | Container | Required | Contains data defining a single transaction |
\<Action> | [Enum](#ActionType) | Required | If this element is left out, Geezeo will attempt to update the record, or add it if it does not exist; specify “Delete" if the transaction is to be deleted |
\<TransactionId> | String (255) | Required; Unique | Unique alphanumeric ID; used to identify the transaction. This must be unique within each account, and never change. |
\<AccountId> | String(255) | Required | Used to match the transaction with its account |
\<TransactionType> | Closed List | Required | “Debit" for a negative transaction, “Credit" for a positive transaction |
\<PostedDate> | DateTime | Required | The time that the transaction posted to the user's account |
\<OriginationDate> | DateTime | Optional | The time the transaction actually occurred |
\<Amount> | Decimal | Required | The absolute value of the transaction; do not use a dash to indicate a negative number. Two decimal places are required, even if they amount is even (5.00). |
\<Pending> | Closed List | Optional | If this is a pending transaction, pass “true"; otherwise do not include this field |
\<Memo> | String (255) | Required | The transaction description. What is provided in this field should match what's shown on the users statement, and/or in the FIs OLB |
\<CheckNumber> | String (255) | Optional | If the transaction is a check, a check number may be included in this field. |


## Partner Request

> Request Format

```xml
<PartnerRequest
    id="2"
    sso_partner_id="abc122">
    <!-- Payload -->
</PartnerRequest>
```

All requests will come within a Partner Request.

Attribute | Type | Element | Description
--------- | ---- | ------- | -----------
id | Integer | PartnerRequest | An integer to identify the request. These request IDs will be unique per day, but no tracking or verification is necessary.
sso_partner_id | String(128) | PartnerRequest | This value is identical to the partner_id value submitted in the SSO assertion. It can be used by Resellers that use a single end point for all related FIs as a differentiator, if the PartnerCustomerId values are not globally unique.
request_id | Integer | PartnerResponse | The value of this attribute must be the value of the “id" attribute from the corresponding PartnerRequest.

## Partner Response

> Request Format

```xml
<PartnerResponse
    request_id="2">
    <!-- Payload -->
</PartnerResponse>

```

All responses should be come in the form of a PartnerResponse.

Attribute | Type | Element | Description
--------- | ---- | ------- | -----------
id | Integer | PartnerRequest | An integer to identify the request. These request IDs will be unique per day, but no tracking or verification is necessary.
sso_partner_id | String(128) | PartnerRequest | This value is identical to the partner_id value submitted in the SSO assertion. It can be used by Resellers that use a single end point for all related FIs as a differentiator, if the PartnerCustomerId values are not globally unique.
request_id | Integer | PartnerResponse | The value of this attribute must be the value of the “id" attribute from the corresponding PartnerRequest.

## Flat File

Geezeo also accepts a flat file transfer using a similar XML spec. Flat file transfers are often used in larger implementations for bulk data. When sending data using this method all data should be put into one file. The format for a flat file is similar to the standard format for the Geezeo API but has some slight differences. All elements explained in the [Users](#users), [Accounts](#accounts), and [Transactions](#transactions) sections apply to the flat file as well. See provided example.



When you have finished uploading a file to our SFTP server you can notify us of the new file by sending a simple POST request to an API endpoint.


The URL for this endpoint is, https://partner.url/api/v2/uploads/received, and it takes several query string parameters:


api_key={API_KEY}
filename={FILENAME}
hash={MD5}


The completed URL should look something like:
https://partner.url/api/v2/uploads/received?api_key=abc123&filename=data.xml&hash=hashhashhash


Where API_KEY is your Geezeo API key, the filename is the name of the file you uploaded to the SFTP server (flatfiler.gzo), and MD5 is the full md5 hash of the file you uploaded.


> Flat File XML Example

```xml
<?xml version="1.0" encoding="utf-8"?>
<Users>
  <User>
    <Details>
      <PartnerCustomerId>322079353</PartnerCustomerId>
      <FirstName>RITA                </FirstName>
      <LastName>WILLIAMS                                </LastName>
      <Email>rita@williams.us</Email>
      <ZipCode>19975-3918</ZipCode>
    </Details>

      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000129251-S0000</AccountId>
          <AccountFiName>REGULAR SAVINGS               </AccountFiName>
          <AccountType>savings</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>5.13</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000129251-S0011</AccountId>
          <AccountFiName>SUPER MONEY MARKET            </AccountFiName>
          <AccountType>savings</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>430947.36</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

          <Transaction>
            <TransactionId>83</TransactionId>
            <AccountId>0000129251-S0011</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>-10.00</Amount>
            <Memo>Dunkin Donuts</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>85</TransactionId>
            <AccountId>0000129251-S0011</AccountId>
            <TransactionType>Credit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>20.00</Amount>
            <Memo>AMAZON</Memo>
          </Transaction>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000129251-S0017</AccountId>
          <AccountFiName>ADVANTAGE CHECKING            </AccountFiName>
          <AccountType>checking</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>9868.66</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000129251-S0028</AccountId>
          <AccountFiName>TRADITIONAL IRA SHARE         </AccountFiName>
          <AccountType>investment</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>11895.88</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

          <Transaction>
            <TransactionId>84</TransactionId>
            <AccountId>0000129251-S0028</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>-10.00</Amount>
            <Memo>EBAY</Memo>
          </Transaction>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000129251-L0001</AccountId>
          <AccountFiName>SIGNATURE LOC FIXED RATE      </AccountFiName>
          <AccountType>loan</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Outstanding</BalanceType>
              <BalanceAmount>0.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>

  </User>
  <User>
    <Details>
      <PartnerCustomerId>322079353</PartnerCustomerId>
      <FirstName>KOBE</FirstName>
      <LastName>BRYANT                                    </LastName>
      <Email>kbryant@gmail.com</Email>
      <ZipCode>22030-6090</ZipCode>
    </Details>

      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-S0000</AccountId>
          <AccountFiName>REGULAR SAVINGS               </AccountFiName>
          <AccountType>savings</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>15.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

          <Transaction>
            <TransactionId>66</TransactionId>
            <AccountId>0000173112-S0000</AccountId>
            <TransactionType>Credit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>10.00</Amount>
            <Memo>STEAMGAMES</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>67</TransactionId>
            <AccountId>0000173112-S0000</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>0.00</Amount>
            <Memo>TEST                                      </Memo>
          </Transaction>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-S0012</AccountId>
          <AccountFiName>SECOND CHECKING               </AccountFiName>
          <AccountType>checking</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>40.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

          <Transaction>
            <TransactionId>61</TransactionId>
            <AccountId>0000173112-S0012</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>-5.00</Amount>
            <Memo>NONBLANK</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>62</TransactionId>
            <AccountId>0000173112-S0012</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>-5.00</Amount>
            <Memo>NINTENDO</Memo>
          </Transaction>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-S0017</AccountId>
          <AccountFiName>ADVANTAGE CHECKING            </AccountFiName>
          <AccountType>checking</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>0.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-S0021</AccountId>
          <AccountFiName>TRADITIONAL IRA SHARE         </AccountFiName>
          <AccountType>investment</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>0.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-S0029</AccountId>
          <AccountFiName>ROTH IRA SHARE                </AccountFiName>
          <AccountType>investment</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>90.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

          <Transaction>
            <TransactionId>63</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Credit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>10.00</Amount>
            <Memo>TRANSACTION MEMO NONBLANK</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>64</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>0.00</Amount>
            <Memo>TEST                                      </Memo>
          </Transaction>
          <Transaction>
            <TransactionId>65</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>-10.00</Amount>
            <Memo>TRANSACTION MEMO NONBLANK</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>74</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Credit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>100.00</Amount>
            <Memo>TRANSACTION MEMO NONBLANK</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>75</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>0.00</Amount>
            <Memo>Check Received 100.00                     </Memo>
          </Transaction>
          <Transaction>
            <TransactionId>78</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>-10.00</Amount>
            <Memo>TRANSACTION MEMO NONBLANK</Memo>
          </Transaction>
          <Transaction>
            <TransactionId>79</TransactionId>
            <AccountId>0000173112-S0029</AccountId>
            <TransactionType>Debit</TransactionType>
            <PostedDate>2016-07-07</PostedDate>
            <OriginationDate>2016-07-07</OriginationDate>
            <Amount>0.00</Amount>
            <Memo>Check 00 0 Disbursed 10.00                </Memo>
          </Transaction>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-S0122</AccountId>
          <AccountFiName>COVERDELL ESA SHARE           </AccountFiName>
          <AccountType></AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Current</BalanceType>
              <BalanceAmount>0.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-L0092</AccountId>
          <AccountFiName>HOME EQUITY PRIME             </AccountFiName>
          <AccountType>loan</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Outstanding</BalanceType>
              <BalanceAmount>25.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
      <Account>
        <Details>
          <PartnerCustomerId>322079353</PartnerCustomerId>
          <AccountId>0000173112-L0095</AccountId>
          <AccountFiName>HOME EQUITY PRIME             </AccountFiName>
          <AccountType>loan</AccountType>
          <AccountBalances>
            <AccountBalance>
              <BalanceType>Outstanding</BalanceType>
              <BalanceAmount>25.00</BalanceAmount>
              <CurrencyCode>USD</CurrencyCode>
            </AccountBalance>
          </AccountBalances>
        </Details>

      </Account>
  </User>
</Users>
```


## Reporting Errors

> Error Response

```xml
<Errors>
  <Error>
    <Code>500</Code>
    <Description>
      Unable to find account 12345 for member 99999.
    </Description>
  </Error>
  ...
</Errors>
```


If an API request cannot be processed, please include any applicable errors by code and/or description in the body of the response.


## General reused types

### Account Types

|AccountType | Description |
|-----------| ------------ |
| checking | Checking Account |
| savings | Savings Account |
| cards | Credit Card Account |
| autos | Auto Loan |
| home | Mortgage |
| loan | Other Loan type account not listed specifically |
| asset | Other Asset type account not listed specifically |
| investment | Investment Accounts (positions/transactions will not be created) |

### <a name="ActionType"></a> Action Types

|ActionType|
|-----------|
|New|
|Update|
|Delete|
