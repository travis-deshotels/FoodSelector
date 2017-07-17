var choices = [];
var indexes = [];

function addRestaurant(){
	let textbox = document.getElementById("restaurant");
	let div = createDiv(textbox.value);
	document.getElementById("newElements").appendChild(div);
	indexes.push(choices.length-1);
	choices.push(textbox.value);
	textbox.value = "";
}

function createDiv(text){
	let div = document.createElement("div");
	let textNode = document.createTextNode(text);
	div.appendChild(textNode);
	div.setAttribute("id",choices.length-1);
	
	return div;
}

function removeRandomElement(){
	let element = getRandomElement();
	element.parentNode.removeChild(element);
}

function getRandomElement(){
	//get random element by choosing an index, removing that index from indexes
	//then returning the element
	let x = Math.floor(Math.random() * indexes.length);
	let y = indexes[x];
	indexes.splice(x, 1);

	return document.getElementById(y);
}
