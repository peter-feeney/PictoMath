var image1;
var image2;

Dropzone.options.uploadWidget= {
  
  //Change default message and make sure users can only upload images.
  dictDefaultMessage: "Upload images here.",
  acceptedFiles: "image/*",
  //Restrict to only two images.
  accept: function(file, done) {
    console.log("uploaded");
    done();
  },
  init: function() {
    this.on("addedfile", function() {
      if (this.files[2] != null) {
        image1 = this.files[0];
        this.removeFile(this.files[0]);
      } else if (this.files[1] != null) {
        image2 = this.files[1];
        $('#oneImage').toggle();
        $('#twoImage').toggle();
      } else if (this.files[0] != null) {
        image1 = this.files[0];
        $('#oneImage').toggle();
      }
    });
  }
};

$('#transpose').click(function() {
  $.ajax({
    type: "POST",
    url: "/transpose",
    data: {input: 1},
    success: function(response) {
      alert("Succesful");
      //displayImage(response);
      //console.log("success");//remove later
    }
});

  //postImage(image1, "/transpose");
});


$('#svd').click(function() {
  postImage(image1, "/svd");
});

$('#scalarMult').click(function() {
  //Prompt user to give a scalar to multiply by
  postImage(image1, "/scalarMult");
});

$('#inverse').click(function() {
  postImage(image1, "/inverse");
});

$('#add').click(function() {
  alert("You clicked add");
});

$('#multiply').click(function() {
  alert("You clicked multiply");
});

function postImage(input, theUrl) {
  $.ajax({
      type: "POST",
      url: "/transpose",
      data: {input: 1},
      success: function(response) {
        alert("Succesful");
        //displayImage(response);
        //console.log("success");//remove later
      }
  });
}


function displayImage(processed_image) {
  var img = document.createElement("IMG");
  img.src = "images/"+processed_image;
  document.getElementById('output').appendChild(img);
}

/* 
Need to figure out way to restrict input to images. 
and preferiably do it on client-side. Can't tell whether 
or not this code works yet

Dropzone.options.uploadFIle = {
    acceptedFiles: 'image/*'
  };
*/ 

/*
Dropzone.options.uploadFIle = {
  accept: function(file, done) {
    console.log("uploaded");
    done();
  },
  init: function() {
    this.on("addedfile", function() {
      if (this.files[1]!=null){
        this.removeFile(this.files[0]);
      }
    });
  }
};
*/