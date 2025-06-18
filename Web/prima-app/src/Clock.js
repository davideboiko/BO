import React from 'react'

export const Clock = (props) => {

    const t= Date.now()+3600*props.timezone*1000;

    const date= new Date(t)
  return (
    <h3>In {props.country} sono le {date.toLocaleDateString()+" "+ date.toLocaleDateString()}  </h3>
  )
}
