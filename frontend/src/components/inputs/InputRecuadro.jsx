import React from 'react';
import styled from 'styled-components';

const InputRecuadro = ({label}) => {
  return (
    <StyledWrapper>
      <div className="nebula-input">
        <input required type="text" name="text" autoComplete="off" className="input" />
        <label className="user-label">{label}</label>
        <div className="nebula-particle" style={{ '--x': '0.2', '--y': '-0.4', '--delay': '0.1s' }} />
        <div className="nebula-particle" style={{ '--x': '0.5', '--y': '-0.2', '--delay': '0.3s' }} />
        <div className="nebula-particle" style={{ '--x': '0.3', '--y': '0.3', '--delay': '0.5s' }} />
        <div className="nebula-particle" style={{ '--x': '0.7', '--y': '0.1', '--delay': '0.2s' }} />
        <div className="nebula-particle" style={{ '--x': '0.1', '--y': '-0.7', '--delay': '0.4s' }} />
        <div className="nebula-particle" style={{ '--x': '0.6', '--y': '0.4', '--delay': '0.6s' }} />
      </div>
    </StyledWrapper>
  );
}

const StyledWrapper = styled.div`
  .nebula-input {
    position: relative;
    width: 250px;
    margin: 30px auto;
  }

  .nebula-input .input {
    width: 100%;
    padding: 15px;
    border: 2px solid #4b94e2;
    background: transparent;
    color: white;
    font-size: 16px;
    outline: none;
    border-radius: 8px;
    transition: all 0.4s ease-out;
  }

  .nebula-input .user-label {
    position: absolute;
    left: 15px;
    top: 15px;
    pointer-events: none;
    color: #4b94e2;
    transition: all 0.4s ease-out;
    padding: 0 5px;
  }

  .nebula-input .input:focus {
    border-color: #008eecd0;
    box-shadow:
      0 5px 8px #17508C,
      0 10px 20px #103965,
      0 15px 40px #0A233D;
  }

  .nebula-input .input:focus ~ .user-label,
  .nebula-input .input:valid ~ .user-label {
    transform: translateY(-35px);
    font-size: 12px;
    color: #4b94e2;
    left: 10px;
  }

  .nebula-particle {
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    pointer-events: none;
    opacity: 0;
    top: 50%;
    left: 10px;
    filter: blur(0.8px);
    mix-blend-mode: screen;
    transition: opacity 0.3s ease;
  }

  .nebula-input .input:focus ~ .nebula-particle {
    animation: nebula-float 2s forwards ease-out;
  }

  @keyframes nebula-float {
    0% {
      transform: translate(0, -50%) scale(0.8);
      opacity: 0;
      background: #4b94e2;
    }
    20% {
      opacity: 0.8;
    }
    100% {
      transform: translate(calc(var(--x) * 140px), calc(var(--y) * 35px))
        scale(1.1);
      opacity: 0;
      background: #6df2ff;
    }
  }`;

export default InputRecuadro;
