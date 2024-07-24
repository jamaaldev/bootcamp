// let textEl = document.getElementById('ptext')

// textEl.style.color = 'yellow';
// textEl.style.backgroundColor = 'green';
// textEl.style.border = '5px dotted black';
// textEl.remove();
// let secondP = document.createElement('p');
// secondP.id = 'secp';
// secondP.innerHTML = 'i am second element paragraph'
// document.body.appendChild(secondP)
// function squarePlus(numberIn){
//     let sum = 0;
//     sum = numberIn * numberIn * numberIn;
//     sum = sum +1;
//     return sum;

// }
// function cubeNumber(numberIn){
//     let sum = 0;
//     sum = numberIn * numberIn;
//     return sum;

// }

// function getNumber(){
//     let num = prompt('write a number')
//    let result = cubeNumber(num)
//    console.log("📢[script.js:22]: result: ", result);
// }
// console.log(squarePlus(10))
function getText(){
 // get the user input
    let textEl = prompt('Enter Your Text');
    // invoke the method createEl to return the text
    createEl(textEl);
}
function createEl(textEl){
    // selector
    let headerOne = document.getElementById('one');
    // create h2 element
    let headerTwo = document.createElement('h2');
    // append the element with text in body element
    headerTwo.innerHTML = textEl;
    document.body.appendChild(headerTwo)
    // replace the h1 to new text
    headerOne.innerHTML = textEl;

}

