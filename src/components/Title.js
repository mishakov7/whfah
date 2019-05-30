import React from 'react';
import './css/Fonts.css';

// Styling Tittle component with JSX object
const TitleStyle = {
  color: "#fff",
  gridArea: "title",
  fontFamily: "Adlinnaka",
  backgroundColor: "#87bc4a",
  fontSize: "1em",
  textTransform: "lowercase",
  margin: "-2em -2em 0em -2em"
}

const Title = () => (
    <div style={TitleStyle} className="Title">
      <h2>We Have Food at Home</h2>
    </div>
)

export default Title
