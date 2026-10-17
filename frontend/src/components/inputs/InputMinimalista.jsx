import React from 'react';
import styled from 'styled-components';

const InputMinimalista = ({ 
  className, type, label, value, onChange, disabled, required = true, children 
}) => {
  return (
    <StyledWrapper>
      <div className={`form__group ${className}`}>
        {type === "select" ? (
          <select id={className}
            className="form__field"
            value={value}
            onChange={onChange}
            disabled={disabled}
            required={required}
          >
            {children}
          </select>
        ) : (
          <input id={className}
            type={type} 
            className="form__field"
            value={value}
            onChange={onChange}
            placeholder={label} 
            disabled={disabled}
            required={required} />
        )}
        <label htmlFor={className} className="form__label">{label}</label>
      </div>
    </StyledWrapper>
  );
}

const StyledWrapper = styled.div`
  .form__group {
    position: relative;
    padding: 20px 0 0;
    width: 100%;
  }

  .form__field {
    font-family: inherit;
    width: 100%;
    border: none;
    border-bottom: 2px solid #9b9b9b;
    outline: 0;
    font-size: 17px;
    color: #fff;
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
  }

  .form__field::placeholder {
    color: transparent;
  }

  .form__field:placeholder-shown ~ .form__label {
    font-size: 17px;
    cursor: text;
    top: 20px;
  }

  .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 17px;
    color: #9b9b9b;
    pointer-events: none;
  }

  .form__field:disabled,
  .form__field:focus {
    padding-bottom: 6px;
    font-weight: 700;
    border-width: 3px;
    border-image: linear-gradient(to right, #247CDB, #C2DBF5);
    border-image-slice: 1;
  }
  .form__field:disabled ~ .form__label,
  .form__field:focus ~ .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 17px;
    color: #4B94E2;
    font-weight: 700;
  }

  #cantidad-ingreso,
  #select-ingreso {
    color: #aae99d !important;
  }

  #cantidad-gasto,
  #select-gasto {
      color: #E24E4B !important;
  }

  /* reset input */
  .form__field:required, .form__field:invalid {
    box-shadow: none;
  }`;

export default InputMinimalista;
