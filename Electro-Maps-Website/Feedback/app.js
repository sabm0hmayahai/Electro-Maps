var express = require("express"),
  expressSanitizer = require("express-sanitizer");
(bodyParser = require("body-parser")),
  (mongoose = require("mongoose")),
  (methodOverride = require("method-override")),
  (app = express());

//APP CONFIG
mongoose.connect("mongodb://localhost/maps_feedback");
app.use(express.static("public")); // to serve public directory for express
app.set("view engine", "ejs"); // extention not needed if this line is active
app.use(
  bodyParser.urlencoded({
    extended: true
  })
);
app.use(expressSanitizer());
app.use(methodOverride("_method"));

// MONGOOSE MODEL CONFIG
var myFeedbackSchema = new mongoose.Schema({
  title: String,
  body: String,
  created: {
    type: Date,
    default: Date.now
  }
});
var Feedback = mongoose.model("Feedback", myFeedbackSchema);

app.get("/", function(req, res) {
  res.redirect("/feedback");
});

// INDEX ROUTE
app.get("/feedback", function(req, res) {
  Feedback.find({}, function(err, feedback) {
    if (err) {
      console.log(err);
    } else {
      res.render("index", {
        feedback: feedback
      });
    }
  });
});

//NEW ROUTE
app.get("/feedback/new", function(req, res) {
  res.render("new");
});

//CREATE ROUTE
app.post("/feedback", function(req, res) {
  //create
  req.body.feedback.body = req.sanitize(req.body.feedback.body);
  Feedback.create(req.body.feedback, function(err, newFeedback) {
    if (err) {
      res.render("new");
    } else {
      res.redirect("/feedback");
    }
  });
});

//SHOW ROUTE
app.get("/feedback/:id", function(req, res) {
  Feedback.findById(req.params.id, function(err, foundPost) {
    if (err) {
      console.log(err);
    } else {
      res.render("show", {
        post: foundPost
      });
    }
  });
});

//EDIT ROUTE
app.get("/Feedback/:id/edit", function(req, res) {
  Feedback.findById(req.params.id, function(err, foundPost) {
    if (err) {
      req.render("/feedback");
    } else {
      res.render("edit", {
        post: foundPost
      });
    }
  });
});

//UPDATE ROUTE
app.put("/feedback/:id", function(req, res) {
  //Feedback.findByIdAndUpdate(id , new data, callback)
  req.body.Feedback.body = req.sanitize(req.body.Feedback.body);
  Feedback.findByIdAndUpdate(req.params.id, req.body.Feedback, function(
    err,
    updatePost
  ) {
    if (err) {
      res.redirect("/feedback");
    } else {
      res.redirect("/feedback/" + req.params.id);
    }
  });
});

//DELETE ROUTE
app.delete("/feedback/:id", function(req, res) {
  //destroy
  Feedback.findByIdAndDelete(req.params.id, function(err) {
    if (err) {
      res.redirect("/feedback");
    } else {
      res.redirect("/feedback");
    }
  });
  //redirect to homepage
});

// Tell express to listen for requests (start server)
var server = app.listen(3000, "0.0.0.0", function() {
  var host = server.address().address;
  var port = server.address().port;
  console.log("listening at http://%s:%s", host, port);
});
