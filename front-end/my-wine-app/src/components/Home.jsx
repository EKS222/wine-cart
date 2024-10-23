import React from 'react';
import './Home.css';

function Home() {
  return (
    
    <div className="home-page">
     {/* <Link to="/wines" className="cta-button">
        Shop Now
      </Link> */}

      {/* Homepage Content */}
      <header className="headerf">
        <h1>Welcome to VinesJourney🍷</h1>
        <p>Your Wine Journey Begins Here!</p>
        <div className = "imgf">
        <img src ="https://i.pinimg.com/564x/3f/fe/dc/3ffedcb7f3be93bb84361751b9166ec0.jpg" alt="wines"/>
        </div>
      </header>      
      <section className="gif">
             <img src='https://i.pinimg.com/originals/22/07/81/220781f7c2a3d5c986dd7cc34db24b42.gif'alt="winery"/>
             <div className="text">
              <p>Indulge in the exquisite flavors and aromas<br/> that dance on your palate,<br/> transporting you to the sun-soaked vineyards <br/>of Italy, the lush valleys of France, and beyond.<br/> <br/>Each bottle tells a story, and VinesJourney<br/> is your storyteller, unveiling the secrets behind every label. <br/>With our expertly curated selection, <br/>you'll find the perfect wine for every occasion, <br/>whether it's a cozy evening by the fireplace or <br/>a celebratory toast with friends. <br/>Elevate your wine experience with our helpful guides,<br/> reviews, and ratings from fellow wine enthusiasts. <br/><br/>Join us on this epicurean voyage, and let your wine journey begin with VinesJourney. Cheers to a world of wine wonders!</p>
        </div>
      </section>
      
      <section className="wine-galleryf">
        <h2>FEATURED WINE TYPES</h2>


        {/* Wine categories */}
        <div className="wine-categoryf">
          <div className="wine-category-imagef">
            <img src="https://i.pinimg.com/236x/59/15/a3/5915a3540f01f148b13b50b022077a56.jpg" alt="Red Wines" />
          </div>
          <h3>Red Wines</h3>
          <p>Red wines: Bold, rich, with deep flavors to savor.</p>
        </div>

        <div className="wine-categoryf">
          <div className="wine-category-imagef">
            <img src="https://i.pinimg.com/236x/0f/0f/05/0f0f0587a2f73ebd1098b0a1ef0b3ace.jpg" alt="Vintage Wines" />
          </div>
          <h3>Rosé</h3>
          <p>Rosé wines: Light, elegant, and perfect for summer sipping.</p>
        </div>

        <div className="wine-categoryf">
          <div className="wine-category-imagef">
            <img src="https://i.pinimg.com/236x/90/7d/29/907d29ea4ee97d1554e820e797d0f6e0.jpg" alt="White Wines" />
          </div>
          <h3>White Wines</h3>
          <p>White wines: Crisp, refreshing, and bursting with fruitiness.</p>
        </div>

        <div className="wine-categoryf">
          <div className="wine-category-imagef">
            <img src="https://i.pinimg.com/236x/a7/08/5d/a7085da262fb2ded24df4b117c47873d.jpg" alt="Sparkling" />
          </div>
          <h3>Sparkling</h3>
          <p>Sparkling: Bubbly, adding effervescence to <br/>special moments.</p>
        </div>
      
      </section>
    </div>
  );
}

export default Home;