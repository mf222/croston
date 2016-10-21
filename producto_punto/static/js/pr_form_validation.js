function submit_form(){
    $('#download_form_error').hide();
    var field1 = $('#id_numero_vectores').val();
    var reg1 = /^\d+$/; // eliminar (?!1) para que sea >= a 1
    empty = true;
    valid = false;
    if (field1 != '') {
        empty = false;
    }
    if (reg1.test(field1)) {
        valid = true;
    }
    if (!empty && valid){
        $('#download_form').submit();
    }
    else {
        $('#download_form_error').show();
    }
}