// script.js
let cart = [];

function addToCart(flavor) {
  cart.push(flavor);
  localStorage.setItem('cart', JSON.stringify(cart));
  window.location.href = 'addcart.html';
}

