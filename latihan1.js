//a2//
var sisi = 5;

var volume = sisi*sisi*sisi;
console.log(volume);

//a3//
var r = 7;
var pi = 3.14;

var luas = pi*r*r
console.log(luas);

var pi = 3.14
var r = 5
console.log(Math.ceil(pi * r));

//======================================//
var angka = 2;

if(angka == 1){
    console.log("Angka 1");
}else{
    console.log("Angka selain 1");
}

var bumi = 2;
if(bumi < 2){
    console.log("Angka di bawah 2");
}else if(bumi >2){
    console.log("Angka di atas 2");
}else{
    console.log("Angka 2");
}

var umur = 17;
if(umur>= 17){
    console.log("Bisa bikin KTP");
}else{
    console.log("Belum bisa bikin KTP");
}

//b2//

var minuman = "kopi";
switch(minuman){
    case'kopi':
      console.log("Kamu pilih kopi");
      break;
    case 'teh':
        console.log("Kamu pilih teh");
        break;
}

//b3//

var usia = 17;
var tinggi = 155;
if(usia < 17){
    if(tinggi < 150){
   console.log("tidak boleh masuk");
}else{
    console.log("boleh masuk")
}
}else{
    console.log("boleh masuk")
}
//============================================//
for(var i = 1; i < 5; i++){
    var temp = '';
    for(var j = 1; j <= i; j++){
        temp = temp + j;
    }
    console.log(temp);
}
//===================================================//

//e3//
var murid = [
    [1, "Roma", 3.5],
    [2,"Ulina",3.0],
    [3, "Manusia", 2.5]
]
for(var i = 0; i < murid.length; i++){
    if(murid[i][2] >=3.0){
        console.log(murid[i][0] +"."+murid[i][1]+
            ",IPK = "+murid[i][2]+",Lulus");
    }else{
        console.log(murid[i][0]+"."+murid[i][1]+
            ", IPK = " +murid[i][2]+", Gagal" );
    }
}
//=============================================================//
//f3//

function countLength(str){
    var countWord = str.Length;
    return countWord;
}
function checkLength(str){
    var strLength = countLength(str);
    if(strLength >= 5 && strLength <= 12){
        return "Kata sandi diterima";
    }else{
        return "Masukkan karakter antara 5 dan 12";
    }
}
console.log(checkLength("123wrhlrgnlsdkll"));
console.log(checkLength("kjegnelf753"));

//=======================================================================//

//g1 objek//
function chaneToObject(array){
    var result = {}
    result.jenis = array[0];
    result.harga = array[1];
    result.enak = array[2];
    return result;
}
console.log(chaneToObject(["Durian",
                           7500,
                           true]));

//g2 method//
var mobil = {
    name : "bmw",
    cc : 5000,

starEngine : function () {
    console.log("Mesin Menyala");
}
}
//g3//
var caca = {
    nama : "caca",
    berat: 45,
    tinggi : 155,
    hobi : ["nonton","makan"],

    sebutkanHobi : function(){
        console.log("Hobi caca: ");
        for(var i = 0; i < this.hobi.length ; i++){
            console.log(i+1 + ". " + this.hobi[i]);
        }
    }
}
caca.sebutkanHobi();

//============================================================================//
//h1 larik//
function apa(array2D){
    var kamu = [];
    var tempo = {};

    for(var i = 0; i < array2D.length; i++){
        tempo.nama = array2D[i][0];
        tempo.tipe = array2D[i][1];
        tempo.harga = array2D[i][2];

        result.push(tempo);
        tempo = {};
    }
    return kamu;
}
//h2//
var murid = [
    ["mika", "A", 87],
    ["endo", "A", 75],
    ["aji", "B", 81],
    ["ella","B", 78],
]
function bisa(arr2D){
    var dia = []
    var kelasA= {
        kelas : "A",
        murid: [],
        nilai: [],
    }
    var kelasB = {
        kelas: "B",
        murid: [],
        nilai: [],
    }
    for(var i = 0; i < arr2D.length; i++){
        if(arr2D[i][1] === "A"){
            kelasA.murid.push(arr2D[i][0]);
            kelasA.nilai.push(arr2D[i][2]);
        }else{
            kelasB.murid.push(arr2D[i][0]);
            kelasB.nilai.push(arr2D[i][2]);
        }

    }
    dia.push(kelasA);
    dia.push(kelasB);

    return dia;
}
console.log(bisa(murid));

//================================================================================//



//i1//