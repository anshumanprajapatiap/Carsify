$(document).ready(function(){
        $(".ajaxloader").hide();

        // Product Filter Start
        
        
        $("#chsort, #rangeInputM, #rangeInputYearM, #rangeInputKmM").on('click, change, change, change',function(){
            

            var _filterObj={};

            //orderby

            var _orderby = $('#chsort').val();
            _filterObj.orderby=_orderby;

            //Year

            var _minYear=$('#maxYearM').attr('min');
            var _maxYear=$('#maxYearM').val();
            _filterObj.minYear=_minYear;
            _filterObj.maxYear=_maxYear;


            //price
            var _minPrice=$('#maxPriceM').attr('min');
            var _maxPrice=$('#maxPriceM').val();
            _filterObj.minPrice=_minPrice;
            _filterObj.maxPrice=_maxPrice;

            


            //Km
            var _minKm=$('#maxKmM').attr('min');
            var _maxKm=$('#maxKmM').val();
            _filterObj.minKm=_minKm;
            _filterObj.maxKm=_maxKm;




            $(".filter-checkbox").each(function(index,ele){
                var _filterVal=$(this).val();
                var _filterKey=$(this).data('filter');
                _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                    return el.value;
                });
            });
            console.log(_filterObj);

            // Run Ajax
            $.ajax({
                 url:'/filter-data',
                 data:_filterObj,
                 dataType:'json',
                 beforeSend:function(){
                    $(".ajaxloader").show();
                 },
                 success:function(res){

                    $("#filteredcars").html(res.data);
                    $(".ajaxloader").hide();
                    document.querySelector(".sort").style.display="none";
                    document.querySelector("body").style.position="static";
                 }
            });
        });
        //end


});