let fruits = ['banana','apple','orange'];
let numbers = [10,20,30,5,40,50];
fruits.splice(2,0,'mango'); // u can add specific index with value for example
// when using splice you want to add value EX:['banana:target number 1','apple:target number 2','here','orange'].. 
// you target 2 after apple will add the value. the 0 is not remove target 2 apple but we want to add extra value
// after apple that is it.

fruits.push('kiwi'); // it add last index with value
fruits.unshift('lemon') // it add first index with value
fruits.shift() // it will remove first index with out giving a value EX: lemon and return lemon
fruits.pop() // it will remove last index with out giving value EX: kiwi and return kiwi
console.log("📢[script.js:2]: fruits: ", fruits);
// array method
// foreach() loop the items in array one by one dont return
// map() loop the items in array and it will return new value with out modified the orginal array.
function double(num){
    return  num * 2;
}
console.log("📢[script.js:19]: numbers.map(double): ", numbers.map(double));
console.log("📢[script.js:20]: numbers: ", numbers);

let person = {
    fName: 'jamaal',
    lName: 'mahamed',
    address: {
        city:'london',
        street:'city london'
    }

}
// adding new key with value in object
person.mname = 'hassan';
console.log("📢[script.js:33]: person: ", person);
console.log("📢[script.js:34]: person: ", person.address);