const campo_busca = document.getElementById("busca");
const lista_clientes = document.getElementById("lista_clientes");
const formulario = document.getElementById("formulario-busca");
let clienteEncontrado = null;

if (campo_busca) {
    campo_busca.addEventListener("input", async (event) => {
        const texto = event.target.value.trim();

        if (texto.length >= 1) {
            try {
                const resposta = await fetch(`/clientes/buscar`,{
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ nome: texto })
                });

                const dados = await resposta.json();

                if (dados != null) {
                    clienteEncontrado = dados;
                } else {
                    clienteEncontrado = null;
                }

                if (clienteEncontrado != null) {
                    lista_clientes.innerHTML = "";
                    const option = document.createElement("option");
                    option.value = clienteEncontrado;
                    lista_clientes.appendChild(option);
                }
            } catch (erro) {
                clientesEncontrados = null;
                exibirNotificacao('Erro de conexão com o servidor', '400', "error");
            }
        } else {
            clientesEncontrados = null;
            if (lista_clientes) lista_clientes.innerHTML = "";
        }
    });
};

function criar_formulario_edicao(contrato_div){
    let formulario_edicao = document.createElement("form")
    formulario_edicao.setAttribute("method", "post")
    formulario_edicao.setAttribute("id", "formulario_edicao")

    let nome_completo = document.createElement("input")
    let label_nome_completo = document.createElement("label")
    label_nome_completo.textContent = "Nome Completo"
    label_nome_completo.setAttribute("for", "nome_completo")
    nome_completo.setAttribute("id", "nome_completo")
    nome_completo.setAttribute("name", "nome_completo")
    nome_completo.setAttribute("type", "text")
    formulario_edicao.appendChild(label_nome_completo)
    formulario_edicao.appendChild(nome_completo)

    let nome_mae = document.createElement("input")
    let label_nome_mae = document.createElement("label")
    label_nome_mae.textContent = "Nome Mae"
    label_nome_mae.setAttribute("for", "nome_mae")
    nome_mae.setAttribute("id", "nome_mae")
    nome_mae.setAttribute("name", "nome_mae")
    nome_mae.setAttribute("type", "text")
    formulario_edicao.appendChild(label_nome_mae)
    formulario_edicao.appendChild(nome_mae)

    let cpf = document.createElement("input")
    let label_cpf = document.createElement("label")
    label_cpf.textContent = "Cpf"
    label_cpf.setAttribute("for", "cpf")
    cpf.setAttribute("id", "cpf")
    cpf.setAttribute("name", "cpf")
    cpf.setAttribute("type", "text")
    formulario_edicao.appendChild(label_cpf)
    formulario_edicao.appendChild(cpf)
   
    let data_nascimento = document.createElement("input")
    let label_data_nascimento = document.createElement("label")
    label_data_nascimento.textContent = "Data Nascimento"
    label_data_nascimento.setAttribute("for", "data_nascimento")
    data_nascimento.setAttribute("id", "data_nascimento")
    data_nascimento.setAttribute("name", "data_nascimento")
    data_nascimento.setAttribute("type", "date")
    formulario_edicao.appendChild(label_data_nascimento)
    formulario_edicao.appendChild(data_nascimento)

    let endereco = document.createElement("input")
    let label_endereco = document.createElement("label")
    label_endereco.textContent = "Endereco"
    label_endereco.setAttribute("for", "endereco")
    endereco.setAttribute("id", "endereco")
    endereco.setAttribute("name", "endereco")
    endereco.setAttribute("type", "text")
    formulario_edicao.appendChild(label_endereco)
    formulario_edicao.appendChild(endereco)

    let numero = document.createElement("input")
    let label_numero = document.createElement("label")
    label_numero.textContent = "Numero"
    label_numero.setAttribute("for", "numero")
    numero.setAttribute("id", "numero")
    numero.setAttribute("name", "numero")
    numero.setAttribute("type", "text")
    formulario_edicao.appendChild(label_numero)
    formulario_edicao.appendChild(numero)

    let bairro = document.createElement("input")
    let label_bairro = document.createElement("label")
    label_bairro.textContent = "Bairro"
    label_bairro.setAttribute("for", "bairro")
    bairro.setAttribute("id", "bairro")
    bairro.setAttribute("name", "bairro")
    bairro.setAttribute("type", "text")
    formulario_edicao.appendChild(label_bairro)
    formulario_edicao.appendChild(bairro)
  
    contrato_div.appendChild(formulario_edicao)
};

function criar_div_cliente(nome_completo, status, data_pedido){
    let card = document.getElementById('card-resultados')
    let contrato_div = document.createElement("div")
    contrato_div.setAttribute("id", "contrato-div")
    
    let p_nome_completo = document.createElement("p")
    p_nome_completo.textContent = nome_completo
    contrato_div.appendChild(p_nome_completo)

    let p_status = document.createElement("p")
    p_status.textContent = status
    contrato_div.appendChild(p_status)

    let p_data_pedido = document.createElement("p")
    p_data_pedido.textContent = data_pedido
    contrato_div.appendChild(p_data_pedido)

    let gerar_contrato = document.createElement("a")
    gerar_contrato.textContent = "contrato"
    gerar_contrato.setAttribute("href", "/clientes/contratos/gerar")
    contrato_div.appendChild(gerar_contrato)

    gerar_contrato.addEventListener("click", (event) => {
        event.preventDefault()
        criar_formulario_edicao(contrato_div)
    })


    card.appendChild(contrato_div)
};



if (formulario) {
    formulario.addEventListener("submit", async (event) => {
        event.preventDefault();

        let form = new FormData(formulario)
        let campos_iterator = form.entries()
        let campos = Object.fromEntries(campos_iterator)
        let campos_json = JSON.stringify(campos)
        let campos_obj = JSON.parse(campos_json)
        let status_code = 0

        resposta = await fetch("/clientes/contratos/buscar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: campos_json
        });

    

        const dados = await resposta.json();
        status_code = resposta.status
        console.log(dados)

        dados.forEach((dados) => {
            criar_div_cliente(dados.nome_completo, dados.status, dados.data_pedido)
        });

        if (resposta.ok == false){
            exibirNotificacao(`${dados.detail}`, `${status_code}`, "error");
        } else {
            exibirNotificacao("Dados trazidos", "200", "sucesso");
            formulario.reset();
        }
    });
};
