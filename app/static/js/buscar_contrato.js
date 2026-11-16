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

function criar_formulario_produto(contrato_div){
    let div_formulario_produto = document.getElementById("div_produto")

    if (div_formulario_produto) {
        return
    } else {
        div_formulario_produto = document.createElement("div")
        div_formulario_produto.innerHTML = ""
        div_formulario_produto.setAttribute("id", "div_produto")
        div_formulario_produto.setAttribute("name", "div_produto")

        let formulario_produto = document.createElement("form")
        formulario_produto.setAttribute("method", "post")
        formulario_produto.setAttribute("id", "formulario_produto")

        let descricao = document.createElement("textarea")
        let label_descricao = document.createElement("label")
        label_descricao.textContent = "Descricao"
        label_descricao.setAttribute("for", "descricao")
        descricao.setAttribute("id", "descricao")
        descricao.setAttribute("name", "descricao")
        descricao.setAttribute("cols", "30")
        descricao.setAttribute("rows", "5")
        formulario_produto.appendChild(label_descricao)
        formulario_produto.appendChild(descricao)

        let valor = document.createElement("input")
        let label_valor = document.createElement("label")
        label_valor.textContent = "Valor"
        label_valor.setAttribute("for", "valor")
        valor.setAttribute("id", "valor")
        valor.setAttribute("name", "valor")
        valor.setAttribute("type", "text")
        formulario_produto.appendChild(label_valor)
        formulario_produto.appendChild(valor)

        let forma_pagamento = document.createElement("select")
        let label_forma_pagamento = document.createElement("label")
        let pix = document.createElement("option")
        let cartao = document.createElement("option")
        let dinheiro = document.createElement("option")
        label_forma_pagamento.textContent = "Forma Pagamento"
        label_forma_pagamento.setAttribute("for", "forma_pagamento")
        forma_pagamento.setAttribute("id", "forma_pagamento")
        forma_pagamento.setAttribute("name", "forma_pagamento")
        pix.setAttribute("value", "pix")
        dinheiro.setAttribute("value", "dinheiro")
        cartao.setAttribute("value", "cartao")
        pix.textContent = "pix"
        cartao.textContent = "cartao"
        dinheiro.textContent = "dinheiro"
        forma_pagamento.appendChild(pix)
        forma_pagamento.appendChild(cartao)
        forma_pagamento.appendChild(dinheiro)
        formulario_produto.appendChild(label_forma_pagamento)
        formulario_produto.appendChild(forma_pagamento)

        div_formulario_produto.appendChild(formulario_produto)
        contrato_div.appendChild(div_formulario_produto)
    }
};

function criar_formulario_cliente(contrato_div){
    let div_formulario_cliente = document.getElementById("div_cliente")

    if (div_formulario_cliente){
        return
    } else {
        div_formulario_cliente = document.createElement("div")
        div_formulario_cliente.setAttribute("id", "div_cliente")
        div_formulario_cliente.setAttribute("name", "div_cliente")

        let formulario_cliente = document.createElement("form")
        formulario_cliente.setAttribute("method", "post")
        formulario_cliente.setAttribute("id", "formulario_cliente")

        let nome_completo = document.createElement("input")
        let label_nome_completo = document.createElement("label")
        label_nome_completo.textContent = "Nome Completo"
        label_nome_completo.setAttribute("for", "nome_completo")
        nome_completo.setAttribute("id", "nome_completo")
        nome_completo.setAttribute("name", "nome_completo")
        nome_completo.setAttribute("type", "text")
        formulario_cliente.appendChild(label_nome_completo)
        formulario_cliente.appendChild(nome_completo)

        let nome_mae = document.createElement("input")
        let label_nome_mae = document.createElement("label")
        label_nome_mae.textContent = "Nome Mae"
        label_nome_mae.setAttribute("for", "nome_mae")
        nome_mae.setAttribute("id", "nome_mae")
        nome_mae.setAttribute("name", "nome_mae")
        nome_mae.setAttribute("type", "text")
        formulario_cliente.appendChild(label_nome_mae)
        formulario_cliente.appendChild(nome_mae)

        let cpf = document.createElement("input")
        let label_cpf = document.createElement("label")
        label_cpf.textContent = "Cpf"
        label_cpf.setAttribute("for", "cpf")
        cpf.setAttribute("id", "cpf")
        cpf.setAttribute("name", "cpf")
        cpf.setAttribute("type", "text")
        formulario_cliente.appendChild(label_cpf)
        formulario_cliente.appendChild(cpf)
    
        let data_nascimento = document.createElement("input")
        let label_data_nascimento = document.createElement("label")
        label_data_nascimento.textContent = "Data Nascimento"
        label_data_nascimento.setAttribute("for", "data_nascimento")
        data_nascimento.setAttribute("id", "data_nascimento")
        data_nascimento.setAttribute("name", "data_nascimento")
        data_nascimento.setAttribute("type", "date")
        formulario_cliente.appendChild(label_data_nascimento)
        formulario_cliente.appendChild(data_nascimento)

        let endereco = document.createElement("input")
        let label_endereco = document.createElement("label")
        label_endereco.textContent = "Endereco"
        label_endereco.setAttribute("for", "endereco")
        endereco.setAttribute("id", "endereco")
        endereco.setAttribute("name", "endereco")
        endereco.setAttribute("type", "text")
        formulario_cliente.appendChild(label_endereco)
        formulario_cliente.appendChild(endereco)

        let numero = document.createElement("input")
        let label_numero = document.createElement("label")
        label_numero.textContent = "Numero"
        label_numero.setAttribute("for", "numero")
        numero.setAttribute("id", "numero")
        numero.setAttribute("name", "numero")
        numero.setAttribute("type", "text")
        formulario_cliente.appendChild(label_numero)
        formulario_cliente.appendChild(numero)

        let bairro = document.createElement("input")
        let label_bairro = document.createElement("label")
        label_bairro.textContent = "Bairro"
        label_bairro.setAttribute("for", "bairro")
        bairro.setAttribute("id", "bairro")
        bairro.setAttribute("name", "bairro")
        bairro.setAttribute("type", "text")
        formulario_cliente.appendChild(label_bairro)
        formulario_cliente.appendChild(bairro)


        let status = document.createElement("select")
        let label_status = document.createElement("label")
        let pago = document.createElement("option")
        let pendente = document.createElement("option")
        label_status.textContent = "Status"
        label_status.setAttribute("for", "status")
        status.setAttribute("id", "status")
        status.setAttribute("name", "status")
        pago.setAttribute("value", "pago")
        pendente.setAttribute("value", "pendente")
        pago.textContent = "pago"
        pendente.textContent = "pendente"
        status.appendChild(pago)
        status.appendChild(pendente)
        formulario_cliente.appendChild(label_status)
        formulario_cliente.appendChild(status)

        div_formulario_cliente.appendChild(formulario_cliente)
        contrato_div.appendChild(div_formulario_cliente)
    }
   
};

function gerar_contrato(dados,botao_contrato){
    botao_contrato.addEventListener("click", async (event) => {
        try {
                const resposta = await fetch(`/clientes/contratos/gerar_contrato`,{
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(dados)
                });

                const dados_back = await resposta.json();

            } catch (erro) {
                clientesEncontrados = null;
                exibirNotificacao('Erro de conexão com o servidor', '400', "error");
            }
    })
}

function criar_div_cliente(dados){
    let card = document.getElementById('card-resultados')
    let contrato_div = document.createElement("div")
    contrato_div.setAttribute("id", "contrato-div")
    
    let p_nome_completo = document.createElement("p")
    p_nome_completo.textContent = dados.nome_completo
    contrato_div.appendChild(p_nome_completo)

    let p_status = document.createElement("p")
    p_status.textContent = dados.status
    contrato_div.appendChild(p_status)

    let p_data_pedido = document.createElement("p")
    p_data_pedido.textContent = dados.data_pedido
    contrato_div.appendChild(p_data_pedido)

    let edicao_cliente = document.createElement("a")
    edicao_cliente.textContent = "👤"
    edicao_cliente.setAttribute("href", "")
    contrato_div.appendChild(edicao_cliente)

    edicao_cliente.addEventListener("click", (event) => {
        event.preventDefault()
        criar_formulario_cliente(contrato_div)
    })

    let edicao_produto = document.createElement("a")
    edicao_produto.textContent = "📦"
    edicao_produto.setAttribute("href", "")
    contrato_div.appendChild(edicao_produto)

    edicao_produto.addEventListener("click", (event) => {
        event.preventDefault()
        criar_formulario_produto(contrato_div)
    })

    let botao_contrato = document.createElement("a")
    botao_contrato.textContent = "📜"
    botao_contrato.setAttribute("href", "")
    contrato_div.appendChild(botao_contrato)

    botao_contrato.addEventListener("click", (event) => {
        event.preventDefault()
        gerar_contrato(dados,botao_contrato)
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
            criar_div_cliente(dados)
        });

        if (resposta.ok == false){
            exibirNotificacao(`${dados.detail}`, `${status_code}`, "error");
        } else {
            exibirNotificacao("Dados trazidos", "200", "sucesso");
            formulario.reset();
        }
    });
};
