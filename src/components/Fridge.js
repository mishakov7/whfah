import React from 'react';
import './css/Fridge.css';
import './css/Fonts.css';
import sectionTitle from './css/sectionTitle.js';

const Fridge = () => {
    return (
        <div className="Fridge">
            <h2 style={sectionTitle}>Select your ingredient(s):</h2>
            <form method="POST" action="http://localhost:5000/userIngredients" target="_blank">
                {/* <label>Ingredi<input type="text" name="ingredient"/> 
                <button type="submit">Submit</button>
                <button type="reset">Reset</button> */}
                <ul className="ingredients">
                    <li><input name="ingredient" value="apple" type="checkbox" /><label for="ingredient">Apple</label></li>
                    <li><input name="ingredient" value="potato" type="checkbox" /><label for="ingredient">Potato</label></li>
                    <li><input name="ingredient" value="cucumber" type="checkbox" /><label for="ingredient">Cucumber</label></li>
                    <li><input name="ingredient" value="carrot" type="checkbox" /><label for="ingredient">Carrot</label></li>
                    <li><input name="ingredient" value="peanut butter" type="checkbox" /><label for="ingredient">Peanut Butter</label></li>
                    <li><input name="ingredient" value="onion" type="checkbox" /><label for="ingredient">Onion</label></li>
                    <li><input name="ingredient" value="celery" type="checkbox" /><label for="ingredient">Celery</label></li>
                    <li><input name="ingredient" value="celery" type="checkbox" /><label for="ingredient">Celery</label></li></ul>
                <ul className="ingredients">
                    <li><input name="ingredient" value="apple" type="checkbox" /><label for="ingredient">Apple</label></li>
                    <li><input name="ingredient" value="potato" type="checkbox" /><label for="ingredient">Potato</label></li>
                    <li><input name="ingredient" value="cucumber" type="checkbox" /><label for="ingredient">Cucumber</label></li>
                    <li><input name="ingredient" value="carrot" type="checkbox" /><label for="ingredient">Carrot</label></li>
                    <li><input name="ingredient" value="peanut butter" type="checkbox" /><label for="ingredient">Peanut Butter</label></li>
                    <li><input name="ingredient" value="onion" type="checkbox" /><label for="ingredient">Onion</label></li>
                    <li><input name="ingredient" value="celery" type="checkbox" /><label for="ingredient">Celery</label></li>
                    <li><input name="ingredient" value="celery" type="checkbox" /><label for="ingredient">Celery</label></li>
                </ul>
                <ul className="ingredients">
                    <li><input name="ingredient" value="apple" type="checkbox" /><label for="ingredient">Apple</label></li>
                    <li><input name="ingredient" value="potato" type="checkbox" /><label for="ingredient">Potato</label></li>
                    <li><input name="ingredient" value="cucumber" type="checkbox" /><label for="ingredient">Cucumber</label></li>
                    <li><input name="ingredient" value="carrot" type="checkbox" /><label for="ingredient">Carrot</label></li>
                    <li><input name="ingredient" value="peanut butter" type="checkbox" /><label for="ingredient">Peanut Butter</label></li>
                    <li><input name="ingredient" value="onion" type="checkbox" /><label for="ingredient">Onion</label></li>
                    <li><input name="ingredient" value="celery" type="checkbox" /><label for="ingredient">Celery</label></li>
                    <li><input name="ingredient" value="celery" type="checkbox" /><label for="ingredient">Celery</label></li>
                </ul>
                <div className="Buttons">
                    <button type="Submit">Enter</button>
                    <button type="Reset">Reset</button>
                </div>
            </form>
        
        </div>
    )
}

export default Fridge;