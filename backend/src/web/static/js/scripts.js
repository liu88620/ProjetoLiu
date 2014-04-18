var img = document.getElementById("img");
var name = g_episodio.split("-")[0]
length = parseInt(g_length);
var id = g_episodio.split("-")[1]
var url_base = "../static/img/" + name + "/ep";
var url = url_base + id + "/1.JPG";
img.src = url;
var anterior = document.getElementById("anterior");
var proximo = document.getElementById("proximo");
var i = 1;

img.style.width = '500px';
img.style.height = '800px';

proximo.onclick = function(){
    if (i < length){
         i++;
         url = url_base + id + "/" + i.toString() +".JPG";
         img.src = url;
    }
};
anterior.onclick = function(){
    if (i > 1){
        i--;
        url = url_base + id + "/" + i.toString() +".JPG";
        img.src = url;
    }
};
