# Responsive Tile Implementation

## Getting Started

> Script example

```html
<script>
window.geezeo = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    g = window.geezeo || {};
  if (d.getElementById(id)) return g;
  js = d.createElement(s);
  js.id = id;
  js.src = 'partner.url';
  fjs.parentNode.insertBefore(js, fjs);
  g._e = [];
  g.ready = function(f) {
    g._e.push(f);
  };
  return g;
}(document, 'script', 'geezeo-tiles'));
</script>
```

To get started, the host page will need add the following HTML snippet to the web page. This will retrieve the tiles library and setup the global `geezeo` object.


## The token

The partner will generate a JWT via a Geezeo SDK (or via their own means) and set it using the `setAuth()` method. All platform SDK’s have a JWT generation method added to them. Please work with your Geezeo implementation team to get the appropriate platform SDK.

Please see the [JWT](#jwt) section of our documentation for detailed information regarding JWT.

Geezeo has made an online [JWT generator](https://geezeo-tiles.s3.amazonaws.com/jwt/index.html) you may use for testing purposes.

Note: Since JWT's can technically be generated anywhere including on the client side it would be a huge security risk to do so as they require an API key to create. All JWT generation should be done server side.

## Implementation Options

### Declarative API

With this approach the tiles library will look for elements within the DOM that are using classnames associated with the registered tiles. If found, the tile be rendered into the matching element. By default, the tiles library will scan the DOM immediately after loading. In some situations if the host page is using a SPA framework with client side routing or manipulating the DOM, the host javascript should call the `geezeo.tiles.load()` function to invoke DOM scanning manually after the DOM has changed.

>  Declaritive example:

```html
<div class="geezeo-my-tile"></div>
```

### Programmatic API

> programmatic example:

```js
geezeo.tiles.createMyTile(el, { primaryColor:'#005695',secondaryColor:'#A8D8FC' })
```

A programmatic implementation is the more common and flexible approach to tiles. This allows the caller to pass the associated dom element. An example of why this might be used is if someone wanted to wrap a tile in the consumers framework component and avoid scanning the dom.

Implementing tiles is a flexible process. For example the ready function, detailed below in the Methods section, can easily be wrapped in a promise. Remember: that if you're making a call on a geezeo object it needs to be after the bootstrap script so the object exists.

>Promise example

```js
function isGeezeoReady() {
  return new Promise(function(resolve, reject) {
    geezeo.ready(resolve)  
  })
}
```
>jQuery example

```js
$(function () {
  geezeo.ready(function() {
    geezeo.tiles.createSpending($('#somediv')[0])
  })
})
```

## Tile Mapping

Tiles are created in one of two ways depending on the implementation. For Declarative changing the class `<div class="geezeo-my-tile"></div>` will determine what tile gets generated. For a programmatic implementation changing the function name `geezeo.tiles.createMyTile(el)` will determine what tile gets generated.



| Responsive Tile                 | Declarative Class      | Programmatic Function |
|------------------------|------------------------|-----------------------|
| Budgets                | geezeo-budgets         | createBudgets         |
| Budgets Small          | geezeo-budgets-small   | createBudgetsSmall    |
| Cashflow               | geezeo-cashflow        | createCashflow        |
| Cashflow Small         | geezeo-cashflow-small  | createCashflowSmall   |
| Goals                  | geezeo-goals           | createGoals           |
| Goals Small            | geezeo-goals-small     | createGoalsSmall      |
| Networth               | geezeo-net-worth       | createNetWorth        |
| Networth Small         | geezeo-net-worth-small | createNetWorthSmall   |
| Spending               | geezeo-spending        | createSpending        |
| Spending Small         | geezeo-spending-small  | createSpendingSmall   |
| Spending Wheel (Donut) | geezeo-spending-wheel  | createSpendingWheel   |
| Transactions           | geezeo-transactions    | createTransactions    |

## Tile Options

Tile options are passed differently depending on the implementation method. While using declarative use html 5 data attributes for options. While using programmatic use an options object.

Tiles will attempt to grow to fit their container and some tiles will change their appearance at certain widths. If you need tiles to be a certain size use standard CSS to constrain the container elements to fit your use cases.

> Declarative Spending example with options

```js
<div class="geezeo-spending" data-layout="2" data-show-header="true" data-disable-rules="false"></div>
```

> Programatic Spending example with options

```js
geezeo.tiles.createSpending(el, {layout:'2',showHeader:'true',disableRules:'false'});
```

## Implementing White Label Options

**Color**

Geezeo tile colors can be white labeled to match your website's color scheme. this will work with most tiles.

>Example of implementation color modifiers with a Declarative implementation:

```html
<div class="geezeo-my-tile" data-primary-color="#006699"></div>
```

>Example of implementing color modifiers using a Programatic implementation:

```js
geezeo.tiles.createMyTile(el,{primaryColor:'#005695',secondaryColor:'#A8D8FC',showHeader:'false',disableRules:'false'});
```

If you want to stick with a default color you can omit the attribute.

*Note: Not all color options are supported with every tile. If you include a color option for a tile where it is not supported the tile will still render.



*Note: If primaryDarkColor/primaryLightColor or secondaryLightColor/secondaryDarkColor are not passed they are based off of primaryColor and secondaryColor respectively*

| Declarative Option         | Programatic Option  | Default Value                                                                                                   |
|----------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------|
| data-primary-color         | primaryColor        | programmatic                                                                                                         |
| data-primary-light-color   | primaryLightColor   | #2ed7ff                                                                                                         |
| data-primary-dark-color    | primaryDarkColor    | #003c8f                                                                                                         |
| data-secondary-color       | secondaryColor      | #1fad36                                                                                                         |
| data-secondary-light-color | secondaryLightColor | #61e065                                                                                                         |
| data-secondary-dark-color  | secondaryDarkColor  | #007c00                                                                                                         |
| data-success-color         | successColor        | #66BB6A                                                                                                        |
| data-warning-color         | warningColor        | #FFF179                                                                                                         |
| data-error-color           | errorColor          | #FF6464                                                                                                         |
| data-positive-color        | positiveColor       | #4CAF50                                                                                                        |
| data-negative-color        | negativeColor       | #F44336                                                                                                          |
| data-donut-colors          | donutColors         | ['#f7e000', '#c585d5', '#ff5b69', '#00c7b6',,'#008f80', '#ffc04f', '#5a7576', '#8fdaff',,'#42577d', '#ea9fe2',] |

**Date Range**

The default range of data that is shown can be changed to be consistent with the rest of the user experience. By default to the largest possible date range of the three below that would make sense for the user.

| Value | Dates shown |
|-------|-------------|
|   1m  | 1 Month     |
|   3m  | 3 Months    |
|   6m  | 6 Months    |



>>Declarative example

```html
<div class="geezeo-spending-wheel" data-date-range="6m"></div>
```

>Pragmatic example

```js
geezeo.tiles.createSpendingWheel(el, {dateRange:'6m'})
```

## Spending Analysis

**layout**: A string value that specifies whether the tag break down section should appear below ('1') or to the right ('2') of the line chart when on desktop. On mobile the mobile layout is always used.

string value containing either '1' or '2'. defaults to '1'. This is used to specify whether the tag break down section should appear below ('1') or to the right ('2') of line chart when on desktop. If on mobile, the mobile layout is always used.

There are six white label options available for spending analysis.

**PrimaryColor**: Represented in red. PrimaryColor effects part of the highlight gradient in the graph while a spending category is selected, as well as the ‘use split tag’ and ‘save’ buttons when a transaction is selected. Note that the ‘Delete’ button is not affected by this option. Default is #1976D2.

**PrimaryLightColor**: Represented in green. PrimaryLightColor effects the other part of the highlight gradient in the graph while a spending category is selected.

**PrimaryDarkColor**: Represented in blue. PrimaryDarkColor effects the outline of the graph while a spending category is selected, as well as the tags on transactions and the header color while viewing a spending category or a specific transaction.

<img src="../images/pc1.png" alt="Primary Colors" style="width: 200px;"/>
<img src="../images/pc2.png" alt="Primary Colors" style="width: 200px;"/>
<img src="../images/pc3.png" alt="Primary Colors" style="width: 200px;"/>


**SecondaryColor**: Represented in red. SecondaryColor effects part of the gradient in the graph while no spending category is selected, as well as the ‘view transactions button’ and the percentage bars for the spending categories. Default is #1fad36.

**SecondaryLightColor**: Represented in green. SecondaryLightColor effects part of the gradient in the graph while no spending category is selected.

**SecondaryDarkColor**: Represented in blue. SecondaryDarkColor effects the outline of the graph while no spending category is selected.


<img src="../images/sc1.png" alt="Secondary Colors" style="width: 200px;"/>
<img src="../images/sc2.png" alt="Secondary Colors" style="width: 200px;"/>


##Spending Donut

**PrimaryColor**: PrimaryColor effects the loading animation used before the spending donut appears.

**DonutColors**: Up to 10 colors are able to be represent different categories in the spending donut. This should be structured as an array:

**donutSize**: Number of pixels for the height and width of the donut visualization. By default the donut will be sized off of the container height.

**dateRange**: The default range of data that is shown can be changed to be consistent with the rest of the user experience. By default to the largest possible date range of the three below that would make sense for the user.

| Value | Dates shown |
|-------|-------------|
|   1m  | 1 Month     |
|   3m  | 3 Months    |
|   6m  | 6 Months    |

**layout** = A string value that specifies whether the date button appears on the top right ('1') or on top ('2') of the donut visitation. Defaults to '1'.

**showControls** = A boolean value to show the date buttons when using layout '1'.

>Example attribute (with default colors):

```js


tile = geezeo.tiles.createSpendingWheel(el, {donutColors : [ '#000000', '#c585d5', '#ff5b69', '#00c7b6', '#008f80', '#ffc04f', '#5a7576', '#8fdaff', '#42577d', '#ea9fe2' ]});

```

<img src="../images/sd.png" alt="Secondary Colors" style="width: 200px;"/>

## Budgets Tile

**usePattern**: A boolean value used to determine whether the meters in budgets will use the diagonal pattern.


**showHeader**: A boolean value that removes the money manager header from the mobile budget screens.

##Cashflow Tiles

**showHeader**: A boolean value that removes the header from the desktop cashflow screens.

##Goals Tile

**showHeader**: A boolean value that removes the header from the desktop goals screens.

##Net Worth Tile
**showHeader**: A boolean value that removes the header from the desktop and mobile net worth screens.

##Methods

**geezeo.setAuth(token)**: This method is used to use a JWT with tiles. Please see the JWT section for additional information on JWT.

| Param | Type   | Description   |
|-------|--------|---------------|
| token | string | The JWT token |

>setAuth() example

```html
<div id="tile"></div>
<script>
geezeo.ready(function () {

  // example of setting a JWT token
  geezeo.setAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxIiwiYXVkIjoiZ2VlejNvLmdlZXplby5jb20iLCJzdWIiOiJhYXJvbnRlc3QxIiwiaWF0IjoxNDg2NzU1NjM4LCJleHAiOjE0ODY3NTkyMzh9.RZIEzHmQv-BMwHV6vp1H-DOKajDQCU6lpJRxxJSbkQo');

  var el = document.getElementById('tile');
  geezeo.tiles.createMyTile(el, {
    primaryColor: '#006699'
  });
});
</script>
```

**tile.setErrorHandler()**: Allows the FI to set and customize what happens when there is an error within the tile. In the case of the example to the side if an image url is returned the tile will replace itself with the provided image. If no image is returned a generic error message will be displayed.


>setErrorHandler(), setNoDataHandler, and ready() example

```js

geezeo.ready(function () {

  var el = document.getElementById('tile');
  tile = geezeo.tiles.createSpending();
  tile.setErrorHandler(function (error) {
    return 'http://url-to-image-to-display.jpg';
  });
  tile.setNoDataHandler(function (error) {
    return 'http://url-to-image-to-display.jpg';
  });

});
```

**tile.setNoDataHandler()**: Allows the FI to set and customize what happens when there is no account or user data. In the case of the example to the side if an image url is returned the tile will replace itself with the provided image. If no image is returned a generic error message will be displayed.


**geezeo.ready(fn)**: Any functions called within the ready function won't be called until the tile is fully loaded. This ensures functions aren't ran too early and prevents unnecessary errors.

| Param     | Type   | Description                              |
|-----------|--------|------------------------------------------|
| function  | string | The function (or functions) you want to run after the tile is fully loaded |

**tiles.on(eventName, listener)**: This function is used to support event callback registration.

| Param     | Type   | Description                              |
|-----------|--------|------------------------------------------|
| eventName | string | The event that will trigger the function |
| listener  | string | The result of the trigger (aka a function)|

**tiles.createMyTile()**: Used to programmatically initialize tiles.

**tiles.load()**: Triggers DOM scanning for tiles. This is only used when implementing tiles using the Declarative API. This will rescan and initialize tiles after a routing process in SPA apps.

**Supported Events**

* 'close' - used to notify when a tile has been closed.

>on() and close event example switching between the spending wheel and transactions tile:

```js
function loadSpendingWheel() {
  geezeo.tiles
    .createSpendingWheel(element)
    .on('click', loadTransactions);
}

function loadTransactions(data) {
  geezeo.tiles
    .createTransactions(element, {
      showHeader : true,
      tags       : data.tag,
      startDate  : data.startDate,
      endDate    : data.endDate
    })
    .on('close', loadSpendingWheel);
}
```
