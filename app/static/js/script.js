function calcular(){
    let operation = document.getElementsByName('operation');
    let text = document.getElementById('text-claro').value;
    let clave = document.getElementById('clave-input').value;
    let op;

    if(operation[0].checked)
        op = "/MD4"
    if(operation[1].checked)
        op = "/MD5"
    if(operation[2].checked)
        op = "/SHA1"
    if(operation[3].checked)
        op = "/SHA256"
    if(operation[4].checked)
        op = "/HMAC"
    ruta = 'data=' + text

    if(operation[4].checked)
        ruta += "&clave="+clave

    $.ajax({
        url: op,
        data: ruta,
        type: 'POST',
        success: function(response){
            document.getElementById("output").innerHTML = response;
        }
    })
}

function mostrar(){
    let div = document.getElementById("input-clave");
    div.style.display = "block"
}

function ocultar(){
    let div = document.getElementById("input-clave");
    div.style.display = "none"
}