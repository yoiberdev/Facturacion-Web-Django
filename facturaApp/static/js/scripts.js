var btn = document.getElementById('agregar');
console.log(btn);
var producto = document.getElementById('id_producto');
var precio = document.getElementById('id_precio');
var cantidad = document.getElementById('id_cantidad');
var contenedor = document.getElementById('almacenar');
var contadorInput = document.getElementById('contador');

var contador = 0;

btn.addEventListener('click',function(){

if(producto.value == "" || precio.value ==  "" || cantidad.value ==""){ //si no ingresa nada en el input le manda mensaje de que ingrese un nombre
  alert('Ingresa un producto');
  return false;
}else if(contadorInput.value == 10){
  alert('Maximo de 10 productos');
  return false;
}else{
  contador++;
 
 console.log(contador);

   var inputProd = document.createElement('input');//creo elemento input y le creo un salto de línea
   var inputPre = document.createElement('input');//creo elemento input y le creo un salto de línea
   var inputCant = document.createElement('input');

   var salto = document.createElement('br');
   var btn_eliminar = document.createElement('button');
   btn_eliminar.innerText= "Eliminar";//Crea boton eliminar
   btn_eliminar.type = 'button';
   btn_eliminar.id = "btn"+contador;

   //Crea los 3 inputs
   inputProd.type = 'text';
   inputProd.id = "prodbtn"+contador;
   inputProd.name = 'prodbtn'+contador;
   inputProd.value = producto.value;
   inputProd.setAttribute('readonly',''); // propiedad disabled

   inputPre.type = 'text';
   inputPre.id = "preciobtn"+contador;
   inputPre.name = 'preciobtn'+contador;
   inputPre.value = precio.value;
   inputPre.setAttribute('readonly',''); // propiedad disabled

   inputCant.type = 'text';
   inputCant.id = "cantbtn"+contador;
   inputCant.name = 'cantbtn'+contador;
   inputCant.value = cantidad.value;
   inputCant.setAttribute('readonly',''); // propiedad disabled

   contenedor.append(salto);//todo lo agrego al div de almacenar
   contenedor.append(inputProd);
   contenedor.append(inputPre);
   contenedor.append(inputCant);
   contenedor.append(btn_eliminar);
   
  
  //Actualizar contador
  contadorInput.value=contador;
  console.log(contadorInput)
  var botones = document.getElementById('btn'+contador);
  
  botones.addEventListener('click', function(){
     
    var btn_id = document.getElementById(this.id);
    
    var input_prod = document.querySelector('input[name='+'prod'+this.id+']');
    var input_precio = document.querySelector('input[name='+'precio'+this.id+']');
    var input_cant = document.querySelector('input[name='+'cant'+this.id+']');
       contenedor.removeChild(btn_id);
       contenedor.removeChild(input_prod);
       contenedor.removeChild(input_precio);
       contenedor.removeChild(input_cant);
       contenedor.removeChild(salto);
       contador--;
       contadorInput.value=contador
  
    
  });
  
}


});