$(function(){
    var text = params2text(getUrlParams());
    $("#sent_params").text(text);
});


function getUrlParams() {
    var urlValues = decodeURIComponent(window.location.search.substring(1)).split('&');
    var urlParams = {};

    for (var i = 0; i < urlValues.length; i++) {
        var params = urlValues[i].split('=');
        urlParams[params[0]] = params[1];
    }

    return urlParams;
};


function params2text(params) {
    var text = "";
    $.each(params, function(key, value) {
        if (text.length) text += ", ";
        text += key + ": " + value;
    });
    return text;
}
