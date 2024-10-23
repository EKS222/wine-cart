import React, { useState } from 'react';

function WineReview({ wineName, onReviewSubmit }) {
  const [rating, setRating] = useState(0);
  const [reviewText, setReviewText] = useState('');

  const handleRatingChange = (e) => {
    setRating(parseInt(e.target.value));
  };

  const handleReviewTextChange = (e) => {
    setReviewText(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onReviewSubmit({
      wineName,
      rating,
      reviewText,
    });
    // Clear the input fields
    setRating(0);
    setReviewText('');
  };

  return (
    <div className="wine-review">
      <h3>Add Review for {wineName}</h3>
      <form onSubmit={handleSubmit}>
        <label>
          Rating:
          <select value={rating} onChange={handleRatingChange}>
            <option value={0}>Select Rating</option>
            <option value={1}>1 Star</option>
            <option value={2}>2 Stars</option>
            <option value={3}>3 Stars</option>
            <option value={4}>4 Stars</option>
            <option value={5}>5 Stars</option>
          </select>
        </label>
        <label>
          Review:
          <textarea
            rows="4"
            value={reviewText}
            onChange={handleReviewTextChange}
            placeholder="Write your review here..."
          ></textarea>
        </label>
        <button type="submit">Submit Review</button>
      </form>
    </div>
  );
}

export default WineReview;