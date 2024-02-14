#!/usr/bin/node

const data = require('./100-data.js').list;
console.log(data);
const newData = data.map((num, idx) => num * idx);
console.log(newData);
