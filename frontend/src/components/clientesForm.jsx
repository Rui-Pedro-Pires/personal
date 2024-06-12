import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import * as React from "react";

function ClientesForm({ route }) {
    const [name, setName] = useState("");
    const [telem, setTelem] = useState("");
    const [email, setEmail] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await api.post(route, { name, telem, email })
            navigate("/")
        } catch (error) {
            alert(error)
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Nome:
                <input type="text" value={name} onChange={e => setName(e.target.value)} />
            </label>
            <label>
                Telemovel:
                <input type="text" value={telem} onChange={e => setTelem(e.target.value)} />
            </label>
            <label>
                Email:
                <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
            </label>
            <input type="submit" value="Submit" />
        </form>
    )
}

export default ClientesForm