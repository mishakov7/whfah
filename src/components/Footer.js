import React from 'react';
import './css/Fonts.css';

const FooterStyle = {
    backgroundColor: "#87bc4a",
    margin: "0 -2em -2em -2em",
    padding: "1em",
    color: "#fff",
    fontFamily: "Adlinnaka"
}

const Footer = () => (
    <div className="Footer" style={FooterStyle}>
      Copyright Misha Lukov All Rights Reserved
    </div>
)

export default Footer