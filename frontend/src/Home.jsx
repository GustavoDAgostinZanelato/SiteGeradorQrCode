import { useState } from "react";

function Home(){
    const [url, setUrl] = useState("");

    const handleChange = (e) => {
        setUrl(e.target.value); // Atualiza a variável `url` com o valor do input
    };

    const enviarUrlBackend = async() => {
        try{
            const response = await fetch("http://localhost:5000/processarUrl", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ url: url }),
            });

            const resultado = await response.json();
            console.log(resultado)

            setUrl("") //limpa o que foi digitado no campo após o envio de URL

        } catch (error) {
            console.error("Erro:", error)
        }
    };

        
   return(
    <>
        <div>
            <h1>Gerador de QR Code</h1>
        </div>
        <div>
            <input 
                placeholder="Digite uma URL" 
                value={url} 
                onChange={handleChange} 
            />
        </div>
        <div>
            <button onClick={enviarUrlBackend}>
                Gerar QRCODE
            </button>
        </div>
    </>
   );
}

export default Home;