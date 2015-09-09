/**
 * Created by Miranda on 9/5/15.
 */
/**
 * Created by Miranda on 9/5/15.
 */

$(document).ready(function() {

  var plantName;
  var bg;
  var $plantpick = $('.plant-pick');
  var $namepick = $('.name-pick');
  var $bgpick = $('.bg-pick');

  $("#plant-pick").imagepicker();
  $("#bg-pick").imagepicker();

  $(".save").click(function() {
    var postdata = {};
    plantName = $('.plant-name-box').val();
    if (plantName !== '') {
      postdata['plantName'] = plantName;
    }
    bg = $("#bg-pick").val();
    if (bg !== '') {
      postdata['background'] = bg;
    }
    $.ajax({
      url: '#',
      dataType: 'text',
      type: 'post',
      data: postdata,
      success: function(data, status) {
        console.log(data);
        if (data === 'error') {
          alert("An error has occurred!");
        } else {
          window.location.href = data;
        }
      }
    });
  });

});
