import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Chat from './Chat';


export default function App() {
  return (
    <div>
      <h1>Welcome to the Web Chat</h1>
      <Switch>
        <Route exact path='/chat' render={()=> <Chat/>}/>
      </Switch>
    </div>
  )
}
