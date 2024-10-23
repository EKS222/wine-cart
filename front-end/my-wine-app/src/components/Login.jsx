import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css';

function Login() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    isRegistering: false,
  });

  const [message, setMessage] = useState(''); // To display success/failure messages

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.isRegistering) {
      // Registration logic
      try {
        const response = await fetch('https://wine-backend.onrender.com/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: formData.email,
            password: formData.password,
          }),
        });

        if (response.ok) {
          setMessage('Registration successful');
        } else {
          setMessage('Registration failed');
        }
      } catch (error) {
        setMessage('Error: ' + error);
      }
    } else {
      // Login logic
      try {
        const response = await fetch('https://wine-backend.onrender.com/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: formData.email,
            password: formData.password,
          }),
        });

        if (response.ok) {
          setMessage('Login successful');
        } else {
          setMessage('Login failed');
        }
      } catch (error) {
        setMessage('Error: ' + error);
      }
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const toggleForm = () => {
    setFormData({ ...formData, isRegistering: !formData.isRegistering });
    setMessage(''); // Clear the message when switching between login and registration
  };

  return (
    <div className="login-container">
      <h1>{formData.isRegistering ? 'Register' : 'Login'}</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
        <button type="submit">
          {formData.isRegistering ? 'Register' : 'Login'}
        </button>
      </form>
      {message && <p className="message">{message}</p>}
      <p className="already-have-account">
        {formData.isRegistering
          ? 'Already have an account?'
          : "Don't have an account?"}
        <Link to="#" onClick={toggleForm}>
          {formData.isRegistering ? 'Already have an account? Login' : "Don't have an account? Register'"}
        </Link>
      </p>
    </div>
  );
}

export default Login;