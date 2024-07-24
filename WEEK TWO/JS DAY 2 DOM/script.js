// selector 
//get the h1 element
let title = document.getElementById('title');
// get the ul element
let ul = document.getElementsByTagName('ul');
// get listitems
let li = document.querySelectorAll('.listItem');
// add style by class name
// title.setAttribute('class','headOne')
title.classList.add('headOne')
// change text 
title.innerText = 'Welcome Week Two'
// loop each list and apply style color
for(let i = 0; i < li.length; i++){
    li[i].style.color = 'red';
    li[i].classList.add('listStyle')
}
// remove title
// title.remove();