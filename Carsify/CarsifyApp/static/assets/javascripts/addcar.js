$(document).ready(function () {
    var current_fs, next_fs, previous_fs;
    var left, opacity, scale;
    var animating;
    $(".steps").validate({
        errorClass: 'invalid',
        errorElement: 'span',
        errorPlacement: function (error, element) {
            error.insertAfter(element.next('span').children());
        },
        highlight: function (element) {
            $(element).next('span').show();
        },
        unhighlight: function (element) {
            $(element).next('span').hide();
        }
    });
    $(".next").click(function () {
        $(".steps").validate({
            errorClass: 'invalid',
            errorElement: 'span',
            errorPlacement: function (error, element) {
                error.insertAfter(element.next('span').children());
            },
            highlight: function (element) {
                $(element).next('span').show();
            },
            unhighlight: function (element) {
                $(element).next('span').hide();
            }
        });
        if ((!$('.steps').valid())) {
            return true;
        }
        if (animating) return false;
        animating = true;
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        next_fs.show();
        current_fs.animate({
            opacity: 0
        }, {
            step: function (now, mx) {
                scale = 1 - (1 - now) * 0.2;
                left = (now * 50) + "%";
                opacity = 1 - now;
                current_fs.css({
                    'transform': 'scale(' + scale + ')'
                });
                next_fs.css({
                    'left': left,
                    'opacity': opacity
                });
            },
            duration: 800,
            complete: function () {
                current_fs.hide();
                animating = false;
            },
            easing: 'easeInOutExpo'
        });
    });
    $(".submit").click(function () {
        $(".steps").validate({
            errorClass: 'invalid',
            errorElement: 'span',
            errorPlacement: function (error, element) {
                error.insertAfter(element.next('span').children());
            },
            highlight: function (element) {
                $(element).next('span').show();
            },
            unhighlight: function (element) {
                $(element).next('span').hide();
            }
            
        });
        if ((!$('.steps').valid())) {
            $("#finalsubmit").show();
            return false;

        }
        if (animating) return false;
        $("#finalsubmit").show();
        animating = true;
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        $("#finalsubmit").show();
        current_fs.animate({
            opacity: 0
        }, {
            step: function (now, mx) {
                scale = 1 - (1 - now) * 0.2;
                left = (now * 50) + "%";
                opacity = 1 - now;
                current_fs.css({
                    'transform': 'scale(' + scale + ')'
                });
                next_fs.css({
                    'left': left,
                    'opacity': opacity
                });
            },
            duration: 8000,
            complete: function () {
                current_fs.hide();
                animating = false;
            },
            easing: 'easeInOutExpo'
        });
    });
    $(".previous").click(function () {
        if (animating) return false;
        animating = true;
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
        previous_fs.show();
        current_fs.animate({
            opacity: 0
        }, {
            step: function (now, mx) {
                scale = 0.8 + (1 - now) * 0.2;
                left = ((1 - now) * 50) + "%";
                opacity = 1 - now;
                current_fs.css({
                    'left': left
                });
                previous_fs.css({
                    'transform': 'scale(' + scale + ')',
                    'opacity': opacity
                });
            },
            duration: 800,
            complete: function () {
                current_fs.hide();
                animating = false;
            },
            easing: 'easeInOutExpo'
        });
    });
});


modules.init();







// const menuBtn = document.querySelector(".menuicon span");
// const searchBtn = document.querySelector(".searchicon");
// const cancelBtn = document.querySelector(".cancelicon");
// const items = document.querySelector(".navitems");
// const form = document.querySelector("form");
//     menuBtn.onclick = ()=>{
//   items.classList.add("active");
//   menuBtn.classList.add("hide");
//   searchBtn.classList.add("hide");
//   cancelBtn.classList.add("show");
// }
// cancelBtn.onclick = ()=>{
//   items.classList.remove("active");
//   menuBtn.classList.remove("hide");
//   searchBtn.classList.remove("hide");
//   cancelBtn.classList.remove("show");
//   form.classList.remove("active");
//   cancelBtn.style.color = "#ff3d00";
// }
// searchBtn.onclick = ()=>{
//   form.classList.add("active");
//   searchBtn.classList.add("hide");
//   cancelBtn.classList.add("show");
// }