$("#submit").click(function (e) {
    e.preventDefault();
    const paragraph =$("#pertanyaan").val();
    const regex = 'siapa nama(.*) yang lahir di (.*)';
    const found = paragraph.toLowerCase().match(regex);
    if(found==null){
      alert("Pertanyaan Tidak Sesuai Format \n Silakan masukan pertanyaan sesuai format \n contoh: Siapa nama (pekerjaan) yang lahir di (daerah)");
    }else{
      $.ajax({
      type: "GET",
      dataType: "json",
      url: "http://127.0.0.1:5000/?sentence=" + $("#pertanyaan").val(),
      success: function (data, status, xhr) {
        console.log("data: ", data);
        $("#query").val(data.set_sparql)
        $("#jawaban").val(data.get_hasil)
        $("#table").show();
      },
    });
      
    }

    console.log(found);
   
  });

  $("#reset").click(function (e) {
    e.preventDefault();
    $("#query").val('')
    $("#jawaban").val('')
    $("#pertanyaan").val(null)
    $("#table").hide();
  });