function func_dropdown(ID){
    let tmp_dropdown = document.getElementById("content_" + ID);
    tmp_dropdown.classList.toggle("show");
    tmp_dropdown.classList.toggle("not_show");
}