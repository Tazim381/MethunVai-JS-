$("#tablee").hide();

$(document).ready(function () {
  //button id
  $("#submitbutton").click(function () {
    var path = $("#myfile").val();
    var pathname = path.replace("C:\\fakepath\\", "");
    $("#tablee").show();
    $("#form").hide();
    $("table").append(
      "<tr> <td>" +
        $("#id").val() +
        "</td> <td>" +
        $("#name").val() +
        "</td><td>" +
        $("#textarea").val() +
        "</td><td>" +
        $("#date").val() +
        "</td><td>" +
        '<img src="image/' +
        pathname +
        '"style="width:150px;height:150px;"/>' +
        "</td></tr>"
    );
  });

  //button id
  $("#resetbutton").click(function () {
    //form id
    $("#tabl")[0].reset();
  });

  $("#back").mouseenter(function () {
    $("#tablee").hide();
    $("#form").show();
  });

  $("input").focus(function () {
    $(this).css("border", "2px solid green");
  });
});
