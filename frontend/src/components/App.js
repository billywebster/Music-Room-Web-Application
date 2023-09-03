import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from './HomePage';

export default class App extends Component {
    constructor(props){
        super(props); {/*Must call parent constructor*/}
    }

    render(){
        return (
        <div className="center">
            <HomePage />
        </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv)


{/*Need to render this component inside index.html*/}
{/*React makes main component, will return something and then stored in div/ID container in html*/}