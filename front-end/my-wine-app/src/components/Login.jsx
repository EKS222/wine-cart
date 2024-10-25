import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Login.css';

function Login() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    isRegistering: false,
  });

  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = formData.isRegistering
      ? 'api/register'
      : 'api/login';

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: formData.email,
          password: formData.password,
        }),
      });

      const result = await response.json();
      if (response.ok) {
        setMessage('Login successful');
        localStorage.setItem('token', result.token); // Store token for session
        navigate('/wines'); // Redirect to the wine listing page
      } else {
        setMessage(result.message || 'An error occurred');
      }
    } catch (error) {
      setMessage('Error: ' + error.message);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const toggleForm = () => {
    setFormData({ ...formData, isRegistering: !formData.isRegistering });
    setMessage('');
  };

  return (
    <div className="login-container">
      <h1>{formData.isRegistering ? 'Register' : 'Login'}</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} />
        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} />
        <button type="submit">{formData.isRegistering ? 'Register' : 'Login'}</button>
      </form>
      {message && <p className="message">{message}</p>}
      <p>
        {formData.isRegistering ? 'Already have an account?' : "Don't have an account?"}
        <Link to="#" onClick={toggleForm}>
          {formData.isRegistering ? 'Login' : 'Register'}
        </Link>
      </p>
    </div>
  );
}

export default Login;
          
