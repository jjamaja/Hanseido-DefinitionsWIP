# JWT

## The token

The Geezeo API supports JWT for authentication.

A JWT is broken up into three parts:

>Decrypted JWT example

```json

"Header:"
{
  "alg": "HS256",
  "typ": "JWT"
}
"Payload:"
{
  "sub": "123",
  "aud": "fi.mybankhq.com",
  "iat": 1467038374,
  "exp": 1467039374,
  "iss": "1203"
}
```
```javascript
"Signature:"

  HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
  "1e44a00ceafb5b8b0da5"
  )
```

>Encrypted JWT example

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJhdWQiOiJmaS5teWJhbmtocS5jb20iLCJpYXQiOjE0NjcwMzgzNzQsImV4cCI6MTQ2NzAzOTM3NCwiaXNzIjoiMTIwMyJ9.FCu8RexBWr9qEOVbnJzjefhCg9oKU9yz02r30SYGVRw
```




1) Header

A JWT header contains two claims: alg and typ.

|Claim | Purpose | Example |
| ----- | ------- | ------- |
| alg   | The hashtag algorithm that is being used for encryption | HS256 |
| typ   | A field used to let the receiving end know this is a JWT | jwt |


2) Payload

Geezeo will implement the following reserved and public claims:

| Claim | Purpose | Example |
| ----- | ------- | ------- |
| iss   | Partner's SSO ID | 1 |
| sub   | Case-sensitive string that uniquely identifies the partner customer ID of the end user in the partner's system | abc123 |
| aud   | Single case-sensitive Fully Qualified Domain Name of the partner's Geezeo PFM | fi.mybankhq.com |
| exp   | This claim sets the exact time, in seconds from epoch, from which this JWT is considered invalid. No more than 24 hours past the iat value. This value should be a **number** and not a strong. | 1467038374 |
| iat   | A number representing a specific time, in seconds from epoch, at which the JWT was issued. Number must be in the past and no more than 24 hours ago. This value should be a **number** and not a strong. | 1467038374 |

3) Signature

The third and final part of a JWT is the signature. To create the signature you take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.


## Implementation

The partner will generate a JWT via a Geezeo SDK (or via their own means) and either attach it as an Authorization Bearer, or pass that to the initialization of the Client SDK. All platform SDK’s have a JWT generation method added to them. Please work with your Geezeo implementation team to get the appropriate platform SDK.

## Troubleshooting

During implementation testing you may run in to some issues displaying tiles. A common cause for this issue is an invalid JWT.

1) **Grab the JWT** On the page where a tile should be displaying get the JWT. It should be located in the authorization header or the partner can provide it. With any rendered tile you can look in your browser's developer tools to find API calls to the Geezeo platform. These calls will have an authorization header with the value of the JWT being used.

2) **JWT Validation** Once you have the JWT paste it over at the [JWT Debugger](https://jwt.io). The token should break apart into human readable json. Check the data to make sure it is line with how Geezeo uses JWT. You can use this [Epoch Converter](https://www.epochconverter.com/) to make sure the 'iat' and 'exp' values are both a number within our platform rules. From here take the API key provided for that partner and paste it into the lower right hand side of the Debugger page. If the token was created correctly it should validate.

3) **JWT Test** Go to our [Codepen JWT Tester](https://codepen.io/geezeo/pen/qVomGj?#) and navigate through the Spending Wheel example and paste in the JWT and uncomment the 'geezeo.SetAuth()' line. This page has a correctly implemented and barebones spending wheel. As long as your JWT is correct the spending wheel will render with the proper data.
