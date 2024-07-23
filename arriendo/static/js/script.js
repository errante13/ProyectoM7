$(document).ready(function() {
    $("#id_region").change(function() {
        var url = "/filtrar-comunas/";
        var regionId = $(this).val();
        $.ajax({
            url: url,
            data: {
                'region': regionId
            },
            success: function(data) {
                $("#id_comuna").html('<option value="">Seleccione una comuna</option>');
                $.each(data, function(key, value) {
                    $("#id_comuna").append('<option value="' + value.id + '">' + value.nombre + '</option>');
                });
            }
        });
    });
});