import React from 'react';
import './AboutPage.css'; // Import the stylesheet for the About Page

const AboutPage = () => {
  return (
    <div className="about-container">
      <h1 className='about-h1'>Wine Recommendations Just For You</h1>
      <p>
        Welcome to our Wine Recommendation App, where your wine journey begins.
        We are passionate about helping you discover the perfect wine for every occasion.
         </p>
         <img className="recomm"
         src ="https://i.pinimg.com/236x/52/86/c3/5286c39dd3fcec5e3b7e4c3cf4bc22ef.jpg" alt="recomm"/>
      
      <div className="section">
        <div className="text">
          <h2>Pairing the Perfect Wine with Your Favorite Dishes</h2>
          <p>
            When it comes to enjoying a good glass of wine, finding the perfect pairing can elevate your culinary experience to new heights. Whether you're a seasoned wine enthusiast or just dipping your toes into the world of wine, understanding how different wines complement various dishes can enhance your dining pleasure. In this article, we'll explore the art of food and wine pairing, offering recommendations to help you make the most of your wine-tasting journey.
          </p>
        </div>
        <div className="pair-image">
          <img src="https://i.pinimg.com/564x/b8/22/8e/b8228e303edc5047ef03c62028fb294d.jpg" alt="pair" />
        </div>
      </div>
      
      <div className="section">
        <div className="text">
          <h2>Understanding the Basics</h2>
          <p>
            Before we dive into specific pairings, let's start with the fundamentals.<br/> The key to successful food and wine pairing lies in balancing the flavors and characteristics of both the wine and the dish.<br/> Here are some essential factors to consider:
          </p>
          <ul>
          <li>Flavor Intensity: Light wines generally pair well with delicate dishes, while bold wines complement robust flavors.</li>
          <li>Acidity: Wines with higher acidity can cut through rich and fatty foods, cleansing the palate.</li>
          <li>Sweetness: Sweet wines often pair beautifully with spicy or salty dishes, creating a harmonious contrast.</li>
          <li>Tannins: Tannic red wines pair nicely with fatty meats, as the tannins help cut the richness.</li>
          <li>Body: Match the weight of the wine with the weight of the dish; light wines with light dishes and full-bodied wines with hearty meals.</li>
        </ul>
        </div>
      </div>
      
      
      <h2>Conclusion</h2>
      <p>
        Pairing wine with food is an art that can enhance your dining experience and open up a world of flavors and aromas. Whether you're enjoying a casual meal or celebrating a special occasion, the right wine can elevate your dish and create lasting memories. So, go ahead and embark on your wine and food pairing adventure, and don't forget to explore the recommendations in our app to find your perfect match. Cheers to delightful dining experiences!
      </p>
    </div>
  );
};

export default AboutPage;