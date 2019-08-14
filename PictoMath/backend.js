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
      if (this.files[2] != null){
        this.removeFile(this.files[0]);
      } else if (this.files[1] != null) {
        $('#oneImage').toggle();
        $('#twoImage').toggle();
      } else if (this.files[0] != null) {
        $('#oneImage').toggle();
      }
    });
  }
};

$('#transpose').click(function() {
  alert("You clicked transpose");
});


$('#svd').click(function() {
  alert("You clicked svd");
});

$('#scalarMult').click(function() {
  //Prompt user to give a scalar to multiply by
  alert("You clicked scalar mult");
});

$('#inverse').click(function() {
  alert("You clicked inverse");
});

$('#add').click(function() {
  alert("You clicked add");
});

$('#multiply').click(function() {
  alert("You clicked multiply");
});

function postImage(input) {
  $.ajax({
      type: "POST",
      url: "functions.py",
      data: { param: input },
      success: callbackFunc
  });
}

function callbackFunc(response) {
    displayImage(response);
    console.log("sucess");//remove later
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