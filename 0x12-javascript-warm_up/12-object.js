#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
