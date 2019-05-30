import React, {Component} from 'react';
import sectionTitle from './css/sectionTitle.js';
import './css/Fonts.css';

class RecipeTitle extends Component {

    // Initialize state of component
   state = {
      loading: true
   }

  // Asynchronous function gets quote from backend or API then changes the state of component when quote has been obtained
 async componentDidMount(){
   const URL = "http://localhost:5500/title"; // URL of Flask backend endpoint
   const response = await fetch(URL);
   const data = await response.text(); // we could also potentially use response.formData()
   
   // Change state of component
   this.setState({title: data, loading: false})
 }

 render(){
    return(
        <div className="RecipeTitle">
            {this.state.loading ? <h2> Loading . . . </h2> : <h2 style={sectionTitle}dangerouslySetInnerHTML={{__html: this.state.title}}></h2>}
        </div>
    )
 }
}
export default RecipeTitle;