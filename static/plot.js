// Dropdown menu func "init" ////////////////////////////////////
function init() {
    // ACTORS //
    var selector = d3.select("#selCast");
    d3.csv(filePath + "/archive/top100_actors.csv").then(function (data) {
    let actors = data
      actors.forEach((actor) => {
        {selector
          .append("option")
          .text(actor.name)
          .property("value", actor.name)
        }
      });
    })

    // COMPOSERS //
    var compose = d3.select("#selComposer");
    d3.csv(filePath +"archive/top100_composers.csv").then( function (data) {
    var composers = data
        composers.forEach((composer) => {
            {compose
              .append("option")
              .text(composer.name)
              .property("value", composer.name)
            }
          });
        })

    // DIRECTORS //
    var direct = d3.select("#selDirector");
    d3.csv(filePath +"archive/top100_directors.csv").then(function (data) {
    var directors = data
      directors.forEach((director) => {
        {direct
          .append("option")
          .text(director.name)
          .property("value", director.name)
        }})
      });

    // GENRE //
    var gen = d3.select("#selGenre");
    d3.csv(filePath +"archive/alph_genres.csv").then (function(data) {
    var genres = data
      genres.forEach((genre) => {
        {gen
          .append("option")
          .text(genre.name)
          .property("value", genre.name)
        }
      });
    })

  // RATING //
  var rate = d3.select("#selRating");
  d3.csv(filePath +"archive/avg_rev_vote.csv").then (function(data) {
  var ratings = data
    ratings.forEach((rating) => {
      {rate
        .append("option")
        .text("Ratings vs Revenue")
        .property("value", rating.vote)
      }
    });
  })
};
init()