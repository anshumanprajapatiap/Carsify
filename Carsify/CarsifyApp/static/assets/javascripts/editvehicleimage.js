// $(function () {

//     $(".js-delete-image").click(function () {
//        event.preventDefault();
//         console.log("hello")
//       $.ajax({
//         //url: '/books/create/',
//         type: 'get',
//         dataType: 'json',
//         beforeSend: function () {
//           $("#image-table").show();
//         },
//         success: function (data) {
//           $("#image-table").html(data.html_form);
//         }
//       });
//     });
  
//   });

// Delete Django Ajax Call
function deleteUser(id) {
    var action = confirm("Are you sure you want to delete this user?");
    if (action != false) {
      $.ajax({
          url: '/deletevehicleimage/',
          data: {
              'id': id,
          },
          dataType: 'json',
          success: function (data) {
              if (data.deleted) {
                $("#image-table #image-" + id).remove();
              }
              else{
                  alert("Image is Already deleted");
              }
          }
      });
    }
  }