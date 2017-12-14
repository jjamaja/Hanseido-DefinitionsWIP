# .net SDK

The Geezeo .net SDK is available [here](https://github.com/Geezeo/net-sdk-public)

For access to Geezeo's github provide your github username to your Geezeo contact and we will give you access.

The .net SDK provides :

* Concrete types for all API endpoints
* Simple scoped access to user resources
* Caching
* Aggregation of endpoints for easier UI work

For more information, please contact your account representative and ask for an introduction to the .net SDK!

## JWT

 The Geezeo API supports [JWT](#jwt) for authentication. Each SDK has a method to generate a JWT token. The JWT token should be passed into the .net SDK via the setAuth method.

### Using JWT

To initialize the SDK using JWT pass apiKey, hostName, userId, partnerId, as well as "true" to tell the SDK to use JWT for all calls.

 > initialize the .NET SDK with JWT

```
var sdk = new SDK(apiKey, hostName, userId, partnerId,true);
```



You can also control the time to live (TTL) in seconds of JWT by passing in additional parameter as a string

>

```
var sdk = new SDK(apiKey, hostName, userId, partnerId,true,"3600");
```

Passing in the User Id and storing the API Key and Hostname in the App.config file as shown below.

```
var sdk = new SDK(userId,true);
```
> App.config

```xml
<appSettings>
       <add key="apiKey" value="KEY GOES HERE" />
       <add key="hostName" value="HOST GOES HERE" />
   <add key="partnerId" value="PARTNER ID GOES HERE" />
   <add key="timeToLive" value="VALUE IN SECONDS GOES HERE" />
</appSettings>
```
### Generating JWT

```
sdk.generateJWT(partnerId,partnerCustomerId,domain, ttl, secret)
```
