import React, { useState } from 'react';
import './login.css';
import google from './google2.png';

function Login() {
    const [isRotated, setIsRotated] = useState(false);

    const handleRotateClick = () => {
        setIsRotated(!isRotated);
    };

    return (
        <div className='Login'>
            {/* LEFT INFO */}
            <div className='side-info'>
                <div className='info-cont'>
                    <h1>
                        Connect, Share, and Discover Moments That Matter.
                        Your community, your voice, all in one feed.
                    </h1>
                    <br />
                    <p>
                        <span>Playto Community</span> connects you with people
                    </p>
                </div>
            </div>

            {/* RIGHT LOGIN */}
            <div className='side-login'>
                <div className={`card ${isRotated ? 'rotated' : ''}`}>

                    {/* LOGIN SIDE */}
                    <div className='card-side front'>
                        <h1>Welcome Back! 👋</h1>
                        <br />
                        <p>Enter your credentials to access your Account</p>

                        <form>
                            <div className='inputs'>
                                <div className='email-input'>
                                    <input type='email' placeholder=' ' required />
                                    <label>Enter Email</label>
                                </div>

                                <div className='pass-input'>
                                    <input type='password' placeholder=' ' required />
                                    <label>Enter Password</label>
                                </div>

                                <div className='remember'>
                                    <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                                        <input type='checkbox' />
                                        <label>Remember me</label>
                                    </div>
                                    <a href='#'>Forgot Password?</a>
                                </div>

                                <div className='dont-have'>
                                    Dont have an account?{' '}
                                    <span id='register' onClick={handleRotateClick}>
                                        click here!
                                    </span>
                                </div>

                                <div className='btn'>
                                    <button type='button'>Login</button>
                                </div>
                            </div>
                        </form>
                    </div>

                    {/* REGISTER SIDE */}
                    <div className='card-side back'>
                        <h1>Register 😊</h1>
                        <br />
                        <p>Let's Connect</p>

                        <form>
                            <div className='inputs'>
                                <div className='email-input'>
                                    <input type='text' placeholder=' ' required />
                                    <label>Enter User Name</label>
                                </div>

                                <div className='email-input'>
                                    <input type='email' placeholder=' ' required />
                                    <label>Enter Email</label>
                                </div>

                                <div className='pass-input'>
                                    <input type='password' placeholder=' ' required />
                                    <label>Enter Password</label>
                                </div>

                                <div className='pass-input'>
                                    <input type='password' placeholder=' ' required />
                                    <label>Confirm Password</label>
                                </div>

                                <div className='remember'>
                                    <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                                        <input type='checkbox' />
                                        <label>Remember me</label>
                                    </div>
                                    
                                </div>

                                <div className='dont-have'>
                                    Already have an account?{' '}
                                    <span id='register' onClick={handleRotateClick}>
                                        click here!
                                    </span>
                                </div>

                                <div className='btn'>
                                    <button type='button'>Register</button>
                                </div>
                            </div>
                        </form>
                    </div>

                </div>
            </div>
        </div>
    );
}

export default Login;
