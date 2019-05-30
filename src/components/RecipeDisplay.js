import React, {Component} from 'react';
import './css/Main.css';

class RecipeDisplay extends Component {

    // Initialize state of component
   state = {
      loading: true
   }

  // Asynchronous function gets quote from backend or API then changes the state of component when quote has been obtained
 async componentDidMount(){
   const URL_src = "http://localhost:5500/sources"; // URL of Flask backend endpoint
   const response_src = await fetch(URL_src);
   const data_src = await response_src.text(); // we could also potentially use response.formData()
   
   const URL_in = "http://localhost:5500/ingredients"; // URL of Flask backend endpoint
   const response_in = await fetch(URL_in);
   const data_in = await response_in.text(); // we could also potentially use response.formData()

   // Change state of component
   this.setState({source: data_src, loading: false})
   this.setState({ingredients: data_in, loading: false})
 }

 render(){
    return(

        <div className="RecipeDisplay">
            {this.state.loading ? <h3>Loading . . . </h3> : <h3 className="Source" dangerouslySetInnerHTML={{__html: this.state.source}}></h3>}
            {this.state.loading ? <div>Loading . . . </div> : <div className="Ingredients" dangerouslySetInnerHTML={{__html: this.state.ingredients}}></div>}
        </div>
    )
 }
}
export default RecipeDisplay;