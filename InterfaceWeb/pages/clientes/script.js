const formulario = document.getElementById("form");

function exibirToast(mensagem, tipo = "sucesso", tempo = 3000) {
    let container = document.getElementById("toast-container");
    if (!container) {
        container = document.createElement("div");
        container.id = "toast-container";
        document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    toast.className = `toast ${tipo}`;
    toast.textContent = mensagem;

    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add("esconder");
        setTimeout(() => {
            toast.remove();
        }, 400);
    }, tempo);
}

async function obterFormulario(event) {
    event.preventDefault();

    const dadosClientes = {
        nome_completo: document.getElementById("nome_completo").value,
        nome_mae: document.getElementById("nome_mae").value,
        cpf: document.getElementById("cpf").value,
        data_nascimento: document.getElementById("data_nascimento").value || null,
        endereco: document.getElementById("endereco").value
    };

    try {
        const resposta = await fetch("/clientes/registrar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dadosClientes)
        });

        if (!resposta.ok) {
            const erroJson = await resposta.json().catch(() => ({ detail: "Erro desconhecido" }));
            exibirToast(erroJson.detail || "Erro ao cadastrar cliente", "erro");
            return;
        }

        const dados = await resposta.json();
        exibirToast("Cliente cadastrado com sucesso!", "sucesso");
        formulario.reset();

    } catch (erro) {
        exibirToast("Erro de conexão com o servidor", "erro");
    }
}

if (formulario) {
    formulario.addEventListener("submit", obterFormulario);
}