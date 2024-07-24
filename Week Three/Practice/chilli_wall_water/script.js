let pics = document.querySelectorAll('.pic');
let playerScore = document.querySelector('.pscore');
let botScore = document.querySelector('.bscore');
let pchoose = document.querySelector('.pchoose');
let bchoose = document.querySelector('.bchoose');
let draw = document.querySelector('.draw span')
let start = document.querySelector('.start')
// winner count 
let playerWon = 0;
let botWon = 0;

pics.forEach(pic => {
    pic.addEventListener('click', (e) => {
        // human can choose by string name wall,chilli,water
        let playerChoose = e.target.id;
        // bot can choose by number
        let botChoose = Math.floor(Math.random() * 3)
        // passing 0 to 2 to convert in to a string and return back
        botChoose = botChoosed(botChoose)

        // this function will check who won the game by passing the choose
        winnerGame(playerChoose, botChoose)
    })

})

// this function will return a string name
function botChoosed(choose) {
    // choose has a index number between 0 to 2 
    // in array string we getting by index value and return back
    return ['wall', 'chilli', 'water'][choose];

}

function winnerGame(playerChoose, botChoose) {
    console.log("📢[script.js:31]: botChoose: ", botChoose);
    console.log("📢[script.js:31]: playerChoose: ", playerChoose);

    if (playerChoose === botChoose) {
        console.log('draw')
        draw.innerText = 'Draw No Winner'
        bchoose.innerText = botChoose
        pchoose.innerText = playerChoose
    }
    // check if player won the game
    if (playerChoose === 'chilli' && botChoose === 'wall') {
        console.log('player won')
        playerWon += +1
        playerScore.innerText = playerWon
        draw.innerText = 'Player Won'
        pchoose.innerText = playerChoose
        bchoose.innerText = botChoose

    }
    if (playerChoose === 'water' && botChoose === 'chilli') {
        console.log('player won')
        playerWon += +1
        playerScore.innerText = playerWon
        draw.innerText = 'Player Won'
        pchoose.innerText = playerChoose
        bchoose.innerText = botChoose

    }
    if (playerChoose === 'wall' && botChoose === 'water') {
        console.log('player won')
        playerWon += +1
        playerScore.innerText = playerWon
        draw.innerText = 'Player Won'
        pchoose.innerText = playerChoose
        bchoose.innerText = botChoose

    }
    // check if bot won the game
    if (botChoose === 'chilli' && playerChoose === 'wall') {
        console.log('bot won')
        botWon += +1
        botScore.innerText = botWon
        draw.innerText = 'Bot Won'
        bchoose.innerText = botChoose
        pchoose.innerText = playerChoose

    }
    if (botChoose === 'water' && playerChoose === 'chilli') {
        console.log('bot won')
        botWon += +1
        botScore.innerText = botWon
        draw.innerText = 'Bot Won'
        bchoose.innerText = botChoose
        pchoose.innerText = playerChoose

    }
    if (botChoose === 'wall' && playerChoose === 'water') {
        console.log('bot won')
        botWon += +1
        botScore.innerText = botWon
        draw.innerText = 'Bot Won'
        bchoose.innerText = botChoose
        pchoose.innerText = playerChoose

    }
}
