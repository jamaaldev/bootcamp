// const friuts = ['mango','banana','orange'];

//for loop
// for(let i = 0;i < friuts.length; i++ ){
//     console.log(friuts[i]);
// }
// let numbers = 0;
// while (numbers <= 10){
//     numbers++
//     console.log(numbers);
// }
//while loop
// let cards = ['club','daimond','spade','heart'];
// let currentCard = 'club'
// while(currentCard != 'spade'){
// console.log(currentCard);
// currentCard = cards[Math.floor(Math.random() * 4)]
// }
// do while
// let x = 5;
// let y = 0;
// do{
// x += y;
// console.log(x);
// y++
// } while(y < 10)
// task 1 started

let favourMovies = ['The Shawshank Redemption',' The Godfather','The Dark Knight','12 Angry Men','The Lord of the Rings: The Return of the King'];
favourMovies.push('The Matrix ')
favourMovies.push('Fight Club')
for(let i = 0; i < favourMovies.length; i++){
    console.log(favourMovies[i])
}

//task 1 ended

// task 2 start
let randomNumber = 0;
while (randomNumber <= 10){
    let gen100 = Math.floor(Math.random() * 100) + 1;
    console.log("📢[script.js:41]: randomNumber: ", gen100);
    
    
    randomNumber++;
}
//task 2 ended

// task 3 start backwards
let backward = 21;
while(backward > 1){
    backward--
    console.log("📢[script.js:49]: backward: ", backward);
    
}
// task 3 ended

//task 4 start divisible
let divisible = 51;

for(let i = 1; i < divisible; i++){
    
    if(i % 5 === 0){
        console.log("📢[script.js:58]: is divisible: ", i);
        
    } else {
      
        console.log("📢[script.js:68]: not divisible: ", i);
    }
}
