$(document).ready(function(){
        $(".ajaxloader").hide();

        // Product Filter Start
        $(".filter-checkbox, #rangeInput, #rangeInputYear,#rangeInputKm, #cars" ).on('click, change, change, change, change',function(){
            var _filterObj={};

            //orderby
            var _orderby = $('#cars').val();
            _filterObj.orderby=_orderby;
            

            //price
            var _minPrice=$('#maxPrice').attr('min');
            var _maxPrice=$('#maxPrice').val();
            _filterObj.minPrice=_minPrice;
            _filterObj.maxPrice=_maxPrice;

            //Year

            var _minYear=$('#maxYear').attr('min');
            var _maxYear=$('#maxYear').val();
            _filterObj.minYear=_minYear;
            _filterObj.maxYear=_maxYear;


            //Km
            var _minKm=$('#maxKm').attr('min');
            var _maxKm=$('#maxKm').val();
            _filterObj.minKm=_minKm;
            _filterObj.maxKm=_maxKm;

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
        //end

        // Filter Product According to the price
       $("#maxPrice").on('blur',function(){
                var _min=$(this).attr('min');
                var _max=$(this).attr('max');
                var _value=$(this).val();
                if(_value < parseInt(_min) || _value > parseInt(_max)){
                    alert('Values should be '+_min+'-'+_max);
                    $(this).val(_min);
                    $(this).focus();
                    $("#rangeInput").val(_min);
                    return false;
                }
       });
       // End

});