import React, { useState } from 'react';
import axios from 'axios';
import Dashboard from '../DashBoard/Dashboard';
import './login.css';

function Login() {
  const [email, setEmail] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post(
        'http://127.0.0.1:8000/api/login/',
        { email }
      );

      localStorage.setItem('user', JSON.stringify(res.data));
      alert(res.data.created ? 'Welcome! New user created.' : 'Welcome back!');
      setLoggedIn(true);

    } catch (err) {
      console.error(err);
      alert('Login failed');
    } finally {
      setLoading(false);
    }
  };

  if (loggedIn) return <Dashboard />;

  return (
    <div className="Login">
      <div className="side-login">
        <div className="card">
          <h1>Welcome 👋</h1>

          <form onSubmit={handleLogin}>
            <input
              type="email"
              placeholder="Enter email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />

            <button type="submit" disabled={loading}>
              {loading ? 'Please wait...' : 'Continue'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
