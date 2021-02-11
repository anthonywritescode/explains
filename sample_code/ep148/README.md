# [customize ANY website (beginner - intermediate)](https://youtu.be/Cmz6YGzF0PM)

Today I show how to hack on any behaviour you want to a website! user scripts are one of my favorite productivity boost tools.  I show a few ways to use greasemonkey/tampermonkey to improve some websites and hopefully give some inspiration for things you can do too!

## Interactive examples

### UserScript

Refresh:

```js
// ==UserScript==
// @name         refresh
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://old.reddit.com/r/friendsafari/new/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    window.setTimeout(() => window.location.reload(), 5 * 1000);
})();
```

Pokemon:

```js
// ==UserScript==
// @name         highlight pokemon
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://old.reddit.com/r/friendsafari/new/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    let style = document.createElement('style');
    style.textContent = `
.flair-spiritomb, .flair-wartortle {
    outline: #f00 solid 5px;
}
`;

    document.body.appendChild(style);
})();
```

Discord:

```js
// ==UserScript==
// @name         discordplz
// @namespace    http://asottile.dev/
// @version      0.1
// @description  try to take over the world!
// @author       asottile
// @match        https://discord.com/
// ==/UserScript==

(function() {
    window.location = 'https://discord.com/channels/@me';
})();
```
