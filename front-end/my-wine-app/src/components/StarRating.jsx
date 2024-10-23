import React, { useState } from 'react';

function StarRating({ rating, onRatingChange }) {
  const [hoverRating, setHoverRating] = useState(0);

  const handleMouseEnter = (starRating) => {
    setHoverRating(starRating);
  };

  const handleMouseLeave = () => {
    setHoverRating(0);
  };

  const handleClick = (starRating) => {
    onRatingChange(starRating);
  };

  const stars = [];
  const maxRating = 5;

  for (let i = 1; i <= maxRating; i++) {
    stars.push(
      <span
        key={i}
        className={`star ${i <= (hoverRating || rating) ? 'selected' : ''}`}
        onMouseEnter={() => handleMouseEnter(i)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick(i)}
      >
        ★
      </span>
    );
  }

  return (
    <div className="star-rating">
      {stars}
    </div>
  );
}

export default StarRating;