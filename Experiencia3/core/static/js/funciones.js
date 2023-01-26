
//definimos una funcion de saludo
function Saludar(){
    alert("Hola Mundo 2023");
}

//funcion que muestra datos 
function Mostrar(){
    var nom="Cachupin";
    var edad=10;
    document.write('El nombre es: ' +nom);
    document.write('<br>');
    document.write('La edad es: ' + edad);
}

//funcion que ingresa datos
function Ingresar(){
    var nom, edad; 
    nom = prompt('Ingrese su nombre ');
    edad= prompt('Ingrese su edad ');
    document.write('El nombre ingresado es: ' + nom + ' y la edad es: ' + edad);
}

//funcion que suma dos numeros
function Sumar(){
    var n1, n2, suma; 
    n1 = prompt('Ingrese un numero ');
    n2 = prompt('Ingrese otro numero ');
    suma = parseInt(n1) + parseInt(n2);
    alert("La suma es: " + suma);
}

//funcion que verifica si un numero es positivo o negativo
function Verificar(){
    var n; 
    n = document.getElementById('num1').value;
    if (parseInt(n)>0){
        alert("El numero es positivo ");
    }
    else{
        if (parseInt(n)<0){
            alert("El numero es negativo ");
        }
        else{
            alert("El numero es neutro");
        }
    }
}

//Sumar dos números
function SumarNum(){
    var a,b, suma;
    a=document.getElementById('num2').value;
    b=document.getElementById('num3').value;
    suma= parseInt(a) + parseInt(b);
    alert("La suma de " + a + " + " + b + " = " + suma);
}

//Multiplicar dos numeros 
function MultiplicarNum(){
    var a,b, multi;
    a=document.getElementById('num2').value;
    b=document.getElementById('num3').value;
    multi= parseInt(a) * parseInt(b);
    alert("La multiplicación de " + a + " * " + b + " = " + multi);
}

//ParImpar
function ParImpar(){
    var a;
    a=document.getElementById('num4').value;

    if (parseInt(a)==0)
    {
        alert("El numero cero es neutro");
    }
    else{
        if(parseInt(a)%2==0)
        {
            alert("El numero " + a + " Es par :)");
        }
        else 
        {
            alert("El numero " + a + " Es impar :)");
        }
    }
     
}

//Multiplicacion por sumas sucesivas
function MultiSuma(){
    var a,b, multi=0;
    a = document.getElementById('num5').value;
    b = document.getElementById('num6').value;
    for(x=1; x<=parseInt(b); x++){
        multi = multi + parseInt(a); 
        
    }
    alert("La multiplicación por sumas sucesivas es: " + multi);
}

function VerMenSaje(){
    var mensaje; 
    mensaje = document.getElementById('texto7').value;
    for (x=1; x<=10; x++){
        document.write('Iteracion '+ x + ' : ' + mensaje);
        document.write('<br>');
    }
}