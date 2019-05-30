import React, { Component } from 'react';
import './css/Main.css';

class Recipe extends Component {

     // Initialize state of component
    state = {
       loading: true
    }

   // Asynchronous function gets quote from backend or API then changes the state of component when quote has been obtained
  async componentDidMount(){
    const RECIPE_URL = "http://localhost:5000/recipe"; // URL of Flask backend endpoint
    const response = await fetch(RECIPE_URL);
    const data = await response.text(); // we could also potentially use response.formData()
    
    // Change state of component
    this.setState({recipe: data, loading: false})
  }

  render(){
    return(
      <div className="Recipe">
          {this.state.loading ? <div> Loading...</div> : <div dangerouslySetInnerHTML={{__html: this.state.recipe}}></div>}
      </div>
    )
  }
}

export default Recipe