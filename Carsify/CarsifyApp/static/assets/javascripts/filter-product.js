$(document).ready(function(){
        $(".ajaxloader").hide();
        // Product Filter Start
        $(".filter-checkbox").on('click',function(){
            var _filterObj={};

            $(".filter-checkbox").each(function(index,ele){
                var _filterVal=$(this).val();
                var _filterKey=$(this).data('filter');
                _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                    return el.value;
                });
            });
            //console.log(_filterObj);

            // Run Ajax
            $.ajax({
                 url:'/filter-data',
                 data:_filterObj,
                 dataType:'json',
                 beforeSend:function(){
                    $(".ajaxloader").show();
                 },
                 success:function(res){
                    console.log(res);
                    $("#filteredcars").html(res.data);
                    $(".ajaxloader").hide();
                 }
            });
        });
});