/*
console.log("Lesson 2 GetElementById");
// -----------------------------------
var banner = document.getElementById('page-banner');
*/


/*
console.log("Lesson 3 GetElementsByClassName");
// -----------------------------------
var titles = document.getElementsByClassName('title');
titles[0];
var lis  = document.getElementsByTagName('li');

for(i=0; i < titles.length; i++){
    console.log(titles[i]);

var titles = document.getElementsByClassName('title');
titles.forEach(function(item){ // WILL NOT WORK -- not an array
    console.log(item);

console.log(`document.getElementsByClassName('title') is an Array?: ${Array.isArray(titles)}`);
console.log(`Array.from(document.getElementsByClassName('title')) is an Array?: ${Array.isArray(Array.from(titles))}`);

Array.from(titles).forEach(function(item){ // NOW WORKS
    console.log(item);
})
*/


/*
console.log("Lesson 4 Query Selector");
// -----------------------------------

const wrap = document.querySelector('#wrapper');
console.log("wrap");
console.log(wrap);

const wmf = document.querySelector('#book-list li:nth-child(2) .name');
console.log("wmf");
console.log(wmf);

const book = document.querySelector('#book-list li .name'); // RETURNS ONLY 1 ELEM
console.log("book");
console.log(book);

const books = document.querySelectorAll('#book-list li .name'); // RETURNS ALL
console.log("books");
console.log(books);

Array.from(books).forEach(function(book){
    console.log("ForEach Book:");
    console.log(book);
})
*/


/*
console.log("Lesson 5 Changing Text & HTML Content");
// -----------------------------------
var books = document.querySelectorAll("#book-list li .name") // book is NodeList - already an Array
books.forEach(function(book){
    console.log(book.textContent);
    // book.textContent = 'test';
    book.textContent += ' (book title)';
})

const bookList = document.querySelector("#book-list");
console.log(bookList.innerHTML);
//bookList.innerHTML = '<h2>Books and more books </h2>';
bookList.innerHTML += '<p>This is how U add HTML</p>';
*/


/*
console.log("Lesson 6 Nodes");
// -----------------------------------
const banner = document.querySelector('#page-banner');
// https://www.w3schools.com/jsref/prop_node_nodetype.asp
console.log('#page-banner node type is:', banner.nodeType);
console.log('#page-banner node name is:', banner.nodeName);
console.log('#page-banner has child name is:', banner.hasChildNodes());

//const clonedBanner = banner.cloneNode(false); // COPY BANNER ONLY (one, top elem)
const clonedBanner = banner.cloneNode(true); // RECURSIVE COPY
console.log(clonedBanner);
*/

/*
console.log("Lesson 7 Traversing the DOM");
// -----------------------------------
const bookList = document.querySelector('#book-list');
console.log("the parent node", bookList.parentNode);
console.log("the parent element", bookList.parentElement);
console.log("the parent element of parent", bookList.parentElement.parentElement);

console.log(bookList.childNodes); // Will get even like brakes in html (those, which beetween html elements)
console.log(bookList.children);
*/

/*
console.log("Lesson 8 Traversing the DOM - siblings");
// -----------------------------------
const bookList = document.querySelector("#book-list");

console.log('bookList next sibling is:', bookList.nextSibling); // return linebreak
console.log('bookList next sibling is:', bookList.nextElementSibling);

console.log('bookList previous sibling is:', bookList.previousSibling); // return linebreak
console.log('bookList previous sibling is:', bookList.previousElementSibling);

bookList.previousElementSibling.querySelector('p').innerHTML += '<br /> Too cool' // search inside header and add text
*/

/*
console.log("Lesson 9 Events");
// -----------------------------------
// https://www.w3schools.com/jsref/dom_obj_event.asp
var h2 = document.querySelector('#book-list h2')
h2.addEventListener('click', function(e){
    console.log(e.target);
    console.log(e);
})

var btns = document.querySelectorAll("#book-list .delete")
console.log(btns)

btns.forEach(function(btn){ // Make delete btm realy delete HTML elems
    btn.addEventListener('click', function(e){

        const li = e.target.parentElement;
        li.parentNode.removeChild(li);

    });
});

const link = document.querySelector('#page-banner a')
link.addEventListener('click', function(e){
    e.preventDefault();
    console.log('navigation to', e.target.textContent, ' was prevented')
});
*/

console.log("Lesson 10 Event Bubbling");
// -----------------------------------


/*
console.log("Others");
// -----------------------------------
const link = document.querySelector('#page-banner a')

var newLinks = ['some', 'new', 'text'];

/*
function changeLink(i){
    newLinks.forEach(function(newLink){
        console.log(newLink)
        link.innerHTML = newLink;
        if (--i > -1) {
          setTimeout(function () { changeLink(i); }, 2000);
    }
    });
}
changeLink(5);

//
//newLinks.forEach(function(newLink){
//    console.log(newLink)
//    link.innerHTML = newLink;
//    setTimeout(() => console.log('t'), 1000)
//});

var newLinks = ['some', 'new', 'text'];

const link = document.querySelector('#page-banner a')
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))

const repeatedGreetings = async () => {
  await sleep(1000)
  console.log("First")
  link.innerHTML = newLinks[0];
  await sleep(1000)
  link.innerHTML = newLinks[1];
  await sleep(1000)
  link.innerHTML = newLinks[2];
}
repeatedGreetings();
*/
var newLinks = ['some', 'new', 'text'];

const link = document.querySelector('#page-banner a')
newLinks.forEach(function(newLink){
  (function(newLink) {
    setTimeout(function() {
      link.innerHTML = newLink;
    }, 1000 * i)
  })(newLink);
});
