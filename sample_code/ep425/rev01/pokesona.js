const pokemon = require('./pokemon.js');

p=(a) => {
    b=0;
    for(i=0;i<a.length;i++){
        b=b+a.charCodeAt(i)
    };
    return pokemon[(b+244)%(pokemon.length)];
}

console.log(p('anthonywritescode'));
