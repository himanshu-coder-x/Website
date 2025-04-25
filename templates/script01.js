// script.js
window.onload = function() {
    // Get the cart from local storage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
  
    // Display the products in the cart
    let cartProductsHtml = '';
    cart.forEach((product, index) => {
      cartProductsHtml += `
        <div class="bg-white border border-gray-200 p-4 rounded-lg shadow-lg text-center">
          <h3 class="mt-2 text-lg font-semibold">${product.productName}</h3>
          <p class="text-gray-600">$${product.price}</p>
          <button class="bg-pink-500 hover:bg-pink-700 text-white font-bold py-2 px-4 rounded" onclick="removeFromCart(${index})">Remove</button>
        </div>
      `;
    });
    document.getElementById('cart-products').innerHTML = cartProductsHtml;
  }
  
  function removeFromCart(index) {
    // Get the cart from local storage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
  
    // Remove the product from the cart
    cart.splice(index, 1);
  
    // Save the cart to local storage
    localStorage.setItem('cart', JSON.stringify(cart));
  
    // Update the cart display
    window.location.reload();
  }