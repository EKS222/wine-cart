// Reviews.js
import React, { useState } from 'react';
import './Reviews.css'

function Reviews() {
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState('');

  const handleReviewChange = (e) => {
    setNewReview(e.target.value);
  };

  const handleAddReview = () => {
    if (newReview.trim() !== '') {
      setReviews([...reviews, newReview]);
      setNewReview('');
    }
  };

  return (
    <div className="reviews-container">
      <h1 className="reviews-heading">Customer Reviews</h1>
      <div className="review-input">
        <textarea
          rows="4"
          cols="50"
          placeholder="Write your review..."
          value={newReview}
          onChange={handleReviewChange}
        ></textarea>
        <br />
        <button className="add-review-button" onClick={handleAddReview}>
          Add Review
        </button>
      </div>
      <div className="review-list">
        <h2 className="review-list-heading">Reviews:</h2>
        <ul className="reviews">
          {reviews.map((review, index) => (
            <li className="review" key={index}>
              {review}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Reviews;