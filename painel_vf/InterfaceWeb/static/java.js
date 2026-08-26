console.log("Ola fui carregado");

const formulario = document.getElementById("form");

async function obterFormulario(event) {
    event.preventDefault(); 
    const nome_completo = document.getElementById("nome_completo").value;
    const nome_mae = document.getElementById("nome_mae").value;
    const cpf = document.getElementById("cpf").value;
    const data_nascimento = document.getElementById("data_nascimento").value;
    const endereco = document.getElementById("endereco").value;
    
    
    const dadosClientes = {
        nome_completo: nome_completo,
        nome_mae: nome_mae,
        cpf: cpf,
        data_nascimento: data_nascimento,
        endereco: endereco
    }

    const resposta = await fetch("/clientes", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(dadosClientes)
    })

    const dados = await resposta.json();

    console.log("Resposta do FastAPI:", dados);
}


formulario.addEventListener("submit", obterFormulario);