#CORS

Geezeo uses CORS (Cross Origin Resource Sharing) to whitelist domains for an extra layer of security. You can read up more on the specifics of CORS [here](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).

Here is a quick rundown of how CORS works:

Suppose your local development testing environment domain is http://domain.dev/. When your browser calls Geezeo's service with an HTTP OPTIONS verb asking for allowed hosts, and our platform will respond with a list of allowed hosts. If the host in your address bar is not in that list, your browser will manufacture a 4xx.

Geezeo maintains a list of CORS white label domains. Please provide a list of hostnames for your development and testing environments to your Geezeo contact and we will add them to our whitelist.
