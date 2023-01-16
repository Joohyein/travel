
let Caff = 'global';
let Hot = 'global';
let Sweet = 'global';

$(document).ready(function(){
    $('.question-hot').hide();
    $('.question-sweet').hide();
    $('.result-btn').hide();
});

function caff(num) {
    Caff = num;
    console.log("카페인"+num);
    $('.question-caffeine').hide();
    $('.question-hot').show();
    $('.question-sweet').hide();
    $('.result-btn').hide();
}
function hot(num) {
    Hot = num;
    console.log("뜨거운거"+num);
    $('.question-caffeine').hide();
    $('.question-hot').hide();
    $('.question-sweet').show();
    $('.result-btn').hide();
}

function sweet(num) {
    Sweet = num;
    console.log("달달한거"+num);
    $('.question-caffeine').hide();
    $('.question-hot').hide();
    $('.question-sweet').hide();
    $('.result-btn').show();
    $('.description').hide();
}

function btnClick() {
      $.ajax({
        type: "POST",
        url: "/select/result",
        data: {"Caffeine_give":Caff, "Hot_give":Hot, "Sweet_give":Sweet},
        success: function (response) {
            let url = response['msg']
            //console.log(url);/**/
            //console.log(Caff,Hot,Sweet);
            //response.sendRedirect($(url));
            location.href=url;
            // $(location).attr('href',$(url));
        }
      })
}