// Página de inicio de sesión de la aplicación
import { useState } from 'react';
import { registerUser } from '../../api/authApi';
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import InputMinimalista from '../../components/inputs/InputMinimalista';
import { navegar } from '../../hooks/navegar';

function Register() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setSurname] = useState('');
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { irAInicioSesion } = navegar()

    const handleSubmit = (e) => {
            e.preventDefault();
    
            const user = {
                email,
                username,
                password,
                first_name: firstName,
                last_name: lastName,
            };

            registerUser(user)
                .then(() => {
                    alert("Usuario creado con éxito");
                    irAInicioSesion();
                });
        };

    return (
        <div>
            <h1>Registro</h1>

            <form className="register-form" onSubmit={handleSubmit}>
                <InputMinimalista
                    className="firstName" 
                    type="text" 
                    label="Nombre" 
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />

                <InputMinimalista
                    className="surname" 
                    type="text" 
                    label="Apellido(s)" 
                    value={lastName}
                    onChange={(e) => setSurname(e.target.value)}
                    required={false}
                />

                <InputMinimalista
                    className="username" 
                    type="text" 
                    label="Nombre de usuario" 
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <InputMinimalista
                    className="email" 
                    type="email" 
                    label="Correo electrónico" 
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <InputMinimalista
                    className="password" 
                    type="password" 
                    label="Contraseña" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <BotonPrincipal texto="Crear cuenta" type="submit" />
            </form>

            <BotonPrincipal texto="Volver al inicio de sesión" onClick={irAInicioSesion} />

        </div>
    )
}

export default Register