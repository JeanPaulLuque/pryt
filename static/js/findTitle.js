function findT()
{
    let tasks= JSON.parse(localStorage.getItem('tasks'));
    let data = document.getElementById('busqueda').value;
    let finded = false;
    if (!data){return;}
    for(let i=0;i<tasks.length;i++){
        if(tasks[i].titu == data){
            abrir();
            document.getElementById('ventana').value = "Guardar Cambios";
            document.getElementById('titulo').value = data;
            document.getElementById('Descripcion').value = tasks[i].descr;
            deleteTask(data);
            finded = true;
        }
    }

}
function account()
{
    alert("Opcion no disponible por estos momentos.");
}
