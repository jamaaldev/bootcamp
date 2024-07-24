let firtsName = document.querySelector('#firstname');
let lastName = document.querySelector('#lastname');
let email = document.querySelector('#email');

let personJSon = [{"id":1,"first_name":"Faith","last_name":"Dongall","email":"fdongall0@miibeian.gov.cn","gender":"Female","ip_address":"174.127.85.26"},
{"id":2,"first_name":"Mord","last_name":"MacConnel","email":"mmacconnel1@i2i.jp","gender":"Male","ip_address":"88.25.150.222"},
{"id":3,"first_name":"Corbett","last_name":"Sineath","email":"csineath2@sfgate.com","gender":"Male","ip_address":"151.47.166.200"},
{"id":4,"first_name":"Kimberli","last_name":"Buckler","email":"kbuckler3@com.com","gender":"Agender","ip_address":"5.29.143.222"},
{"id":5,"first_name":"Rivkah","last_name":"Hymor","email":"rhymor4@woothemes.com","gender":"Female","ip_address":"123.150.57.27"},
{"id":6,"first_name":"Gwenneth","last_name":"Rasmus","email":"grasmus5@foxnews.com","gender":"Female","ip_address":"210.25.234.27"},
{"id":7,"first_name":"Brena","last_name":"Holcroft","email":"bholcroft6@addthis.com","gender":"Female","ip_address":"155.66.160.255"},
{"id":8,"first_name":"Roselle","last_name":"Altham","email":"raltham7@liveinternet.ru","gender":"Non-binary","ip_address":"208.88.173.95"},
{"id":9,"first_name":"Trever","last_name":"Fawdrie","email":"tfawdrie8@shutterfly.com","gender":"Male","ip_address":"252.246.104.83"},
{"id":10,"first_name":"Catharine","last_name":"Rodson","email":"crodson9@barnesandnoble.com","gender":"Female","ip_address":"255.159.138.165"}];
console.log("📢[script.js:17]: personJSon: ", personJSon);
firtsName.innerText = personJSon[0].first_name;
lastName.innerText = personJSon[0].last_name;
// you can also access this way
email.innerText = personJSon[0]['email'];