import React from 'react';
import './Footer.css'; // Import the stylesheet for the Footer

const Footer = () => {
  return (
    <footer className="footer-container">
      <div className="footer-content">
        <div className="footer-section">
          <h3>About Us</h3>
          <p>
            Discover, Sip, <br/>and Savor your<br/> wine journey<br/> with VinesJourney!</p>
        </div>

        <div className="footer-section">
          <h3>Quick Links</h3>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/wines">Shop Wines</a></li>
          </ul>
        </div>

        <div className="footer-section">
          <h3>Follow Us</h3>
          <div className="social-icons">
            <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">
              <i className="fa fa-facebook"></i>
            </a>
            <a href="https://twitter.com/yourpage" target="_blank" rel="noopener noreferrer">
              <i className="fa fa-twitter"></i>
            </a>
            <a href="https://www.instagram." target="_blank" rel="noopener noreferrer">
            <i class="fa fa-instagram" aria-hidden="true"></i>

            </a>
            <a href="https://www.linkedin." target="_blank" rel="noopener noreferrer">
            <i class="fa fa-linkedin" aria-hidden="true"></i>
            </a>
          </div>
        </div>
        <div className="footer-section">
  <h3>Contact Us</h3>
  <address>
    <p><strong>Address:</strong> 123 Vineyard Street, Wineville, CA 12345</p>
    <p><strong>Email:</strong> info@vinesjourney.com</p>
    <p><strong>Phone:</strong> +254 712 333 444</p>
  </address>
</div>

      </div>

      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} VinesJourney🍷. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;