//style html
document.getElementsByClassName("container")
document.getElementById("container").style.color="red";
document.getElementById("container").style.backgroundColor="grey";

//create text
document.getElementById("text").innerHTML="This is Imali and I am 21 years old";

//call children
let child=document.getElementById("container").childNodes//text,text id,p,p id,
console.log(child);

let children=document.getElementById("container").children//text,p
console.log(children);

//create element
let p=document.createElement("p");
p.innerHTML="The beginning"
document.getElementById("container").appendChild(p)//atttach to div to be visible in console

p.setAttribute("class","paragraph")//other attributes alt,src,href
p.setAttribute("id","paragraph")

document.getElementById("paragraph").style.color="green";


//add images

let button=document.getElementById("button");
button.addEventListener("click",function(){
    button.innerHTML="Clicked";
    button.style.backgroundColor="purple"
    button.style.padding="20px"
    button.style.borderRadius="10px"
    button.style.borderStyle="none"
})

