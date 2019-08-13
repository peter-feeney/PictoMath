var picCount = 0;

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