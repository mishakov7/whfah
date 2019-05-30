import React, { Component } from 'react';
import './App.css';
import Title from './components/Title';
import Fridge from './components/Fridge';
//import Button from './components/Button';
import RecipeDisplay from './components/RecipeDisplay';
import Recipe from './components/Recipe';
import RecipeTitle from './components/RecipeTitle';
import Overview from './components/Overview';
import Footer from './components/Footer';

class App extends Component {
  render() {
    return (
        <div className="main">
          <Title/>
          <Overview/>
          <Fridge/>
          <div className="RecipeElement">
            <RecipeTitle />
            <RecipeDisplay/>
            <Recipe/>
          </div>
          <Footer/>
        </div>
    );
  }
}

export default App;
