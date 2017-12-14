# Navless Mobile


Geezeo offers a mobile implementation without a standard navigation bar. This is useful when your existing mobile pfm has a navigation menu that would stack with Geezeo's OR when certain pages of Geezeo mobile are required.

To use navless mobile a user must have an active session cookie - this is obtained by having the user perform a SSO to the platform. Geezeo's recommendation is to implement a hidden window that establishes an SSO session when a user logs into mobile, which can be immediately destroyed. Preloading the session allows navless pages to render without SSO redirects. 

Once the user has their active session cookie they can use any of the navless mobile URLs and display their information on it. It is best practice to have all navless mobile pages implemented inside iframes.


| Navless Page | URL                                                                         |
|--------------|-----------------------------------------------------------------------------|
| Dashboard    | https://partner.url/m?nav=false#/                                        |
| Accounts     | https://partner.url/m?nav=false#/user1/accounts                          |
| Transactions | https://partner.url/m?nav=false#/transactionsearch/transactionsearchhome |
| Cashflow     | https://partner.url/m?nav=false#/cashflow/cashflowhome                   |
| Budget       | https://partner.url/m?nav=false#/budget/budgethome                       |
| Goals        | https://partner.url/m?nav=false#/goals/goalshome                         |
| Networth     | https://partner.url/m?nav=false#/networth/networthhome                   |
| Alerts       | https://partner.url/m?nav=false#/alerts/alertshome                       |
| Help         | https://partner.url/m?nav=false#/help/helphome                           |
| Aggregation  | https://partner.url/m?nav=false#/aggregation/aggregationAdd              |
