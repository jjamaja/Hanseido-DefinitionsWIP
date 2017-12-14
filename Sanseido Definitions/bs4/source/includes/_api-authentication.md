#API Authentication

Geezeo provides an API that exposes all of our platform features. The API address is the same as your SSO relay state, and referred to as partner.url in these documentations.

Geezeo provides two means of API authentication :

## API Key authentication

```shell
curl -X "GET" "http://partner.url/api/v2/resource" -u "%geezeo-api-key%"
```

API Key authentication allows a partner's platform to call the API on behalf of all users, as well as call system API calls.  API Key authentication is only appropriate for secure platform to platform communications.

Authentication with API key is done through Basic http Authentication. Using the API as the username, generate and attach a standard Basic Authentication header.

## JWT Authentication

```shell
curl "https://regions-hackathon-2017.geezeo.com/api/v2/users/regions-hackathon-2017-01/accounts" -H "authorization: Bearer valid.jwt.token"
```

JSON Web Tokens provide a scope and time limited means of access to the API. A partner uses their API key and some other key information to generate a token that allows for time limited access to the API for a single user.  JWT authentication cannot be used for system API calls.

The format and details of the Geezeo tokens can be are found in the [JWT](#jwt) section. Platform SDKs are available for all major platforms to generate tokens. 
