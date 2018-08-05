// Run this example by adding <%= javascript_pack_tag 'hello_react' %> to the head of your layout file,
// like app/views/layouts/application.html.erb. All it does is render <div>Hello React</div> at the bottom
// of the page.

import React from 'react'
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'

const HelloWorld = () => (
  <p> Hello World, from React!</p>
)

document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <HelloWorld />,
    document.body.appendChild(document.createElement('div')),
  )
})
