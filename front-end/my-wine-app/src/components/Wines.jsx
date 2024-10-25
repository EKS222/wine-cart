import React, { useEffect, useState } from 'react';
import './Wines.css';

function Wines() {
  const [wines, setWines] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    // Check if user is logged in by looking for the token in localStorage
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token);

    // Fetch wines from the backend
    fetch('/api/wines')
      .then((response) => response.json())
      .then((data) => setWines(data))
      .catch((error) => console.error('Error fetching wines:', error));
  }, []);

  const handleAddToCart = (wine) => {
    if (!isLoggedIn) {
      alert('Please log in to add items to the cart');
      return;
    }
    setCart((prevCart) => [...prevCart, wine]);
    console.log(`Added ${wine.name} to cart`);
  };

  return (
    <div className="wine-gallery">
      {wines.length > 0 ? (
        wines.map((wine) => (
          <div key={wine.id} className="wine-category">
            <div clasName="wine-category-image">
              <img src="wine.image"/>
            </div>
            <div className="wine-details">
            <h3>{wine.name}</h3>
            <p>{wine.description}</p>
            <p><strong>Price:</strong> {wine.price}</p>
            <div className="ratings">
              <p>Rating: 3/5</p>
              <StarRating rating={3} onRatingChange={handleRatingChange} />
            </div>
              <p>Reviews: 35</p>
            <button onClick={() => handleAddToCart(wine)}>Add to Cart</button>
            <a
              href={`https://wa.me/254791861308?text=I'm interested in ${wine.name}`}
              target="_blank"
              rel="noopener noreferrer"
              className="whatsapp-button"
            >
              Order via WhatsApp
            </a>
              </div>
          </div>
        ))
      ) : (
        <p>Loading wines...</p>
      )}
    </div>
  );
}

export default Wines;
                           
