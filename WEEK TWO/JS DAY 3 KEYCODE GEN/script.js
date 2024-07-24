// selector
const overlay = document.querySelector('#overlay');
const container = document.querySelector('.container');
const eventKey = document.querySelector('#infoEventKey');
const eventCode = document.querySelector('#infoEventCode');
const eventKeyCode = document.querySelector('#infoEventKeyCode');
const headeOne = document.querySelector('#one');
const btn = document.querySelector('button');
const vid = document.querySelector('#vid');
const imgs = document.querySelector('#drag');
const drops = document.querySelector('.drag');

imgs.addEventListener('drag', (e) =>{
// console.log(e)
})
drops.addEventListener('drop', (e) =>{
    e.preventDefault()
console.log(e)
})

// media event play
vid.addEventListener('play', (e) =>{
console.log("📢[script.js:11]: e: ", e.type);

})
// media event pause
vid.addEventListener('pause', (e) =>{
console.log("📢[script.js:11]: e: ", e.type);

})
// media event playing
vid.addEventListener('playing', (e) =>{
console.log("📢[script.js:11]: e: ", e.type);

})
// media event ended
vid.addEventListener('ended', (e) =>{
console.log("📢[script.js:11]: e: ", e.type);
alert('thank you the video has ended now')
})

btn.addEventListener('click', () =>{
    btn.innerText = 'you clicked'
    console.log('you clicked me')
})
headeOne.addEventListener('copy', (e) =>{
    headeOne.innerText = 'You Copyed'
    console.log(e.target)
})
// event listener
window.addEventListener('keydown', (e) =>{
    // on key press hide the overlay
    overlay.style.display = 'none'
    if(e.code === 'Space'){
        console.log("📢[script.js:10]: e: ", e.code);
        eventKey.innerText = 'SpaceBar'
        eventCode.innerText = e.code
        eventKeyCode.innerText = e.keyCode

    } else {

        eventKey.innerText = e.key
        eventCode.innerText = e.code
        eventKeyCode.innerText = e.keyCode
    }
})