var anterior = document.getElementById("anterior");
var proximo = document.getElementById("proximo");
var i = 1;
var url = "../static/ep668/" + i.toString() +".JPG";
var imagem = document.getElementById("img");
imagem.style.width = '500px';
imagem.style.height = '800px';

proximo.onclick = function(){
    if (i < 16){
         i++;
         url = "../static/ep668/" + i.toString() +".JPG";
         imagem.src = url;
    }
}
anterior.onclick = function(){
    if (i > 1){
        i--;
        url = "../static/ep668/" + i.toString() +".JPG";
        imagem.src = url;
    }
}

