

let mapIndex = 0;

function initMap(lat, lng) {
  let map = new google.maps.Map(document.getElementById('map' + String(mapIndex)), {
    center: {lat: lat, lng: lng},
    zoom: 15
  });

  new google.maps.Marker({
    position:{lat:lat, lng: lng},
    map:map
  })

  mapIndex++;
}

$(function (){

  const htmlRegex = /(<([^>]+)>)/ig

  const userBox = `
  <div class="row">
    <div class="col">
      <div class="user btn btn-success">
      </div>
    </div>
  </div>
  `;

  const botBox = `
  <div class="row">
    <div class="col d-flex justify-content-end">
      <div class="bot btn btn-primary">
      </div>
    </div>
  </div>
  `;

  const spinner = `
  <div class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
  `;

  function botMap(){
    return `
<div class="row">
    <div class="col d-flex justify-content-end">
      <div id=map${String(mapIndex)} class="map">
      </div>
    </div>
  </div>
  `
  }

  $( "form" ).on('submit', function(event) {
    event.preventDefault();

    let inputText = $("input:text").val();
    //Display the request
    $(".chat-box").append(userBox);
    $(".user:last").append(inputText.replace(htmlRegex, ""))

    $.post("/search", { query: $('input:text').val()}, function(data){
      if (data){
        // Display the address
        $(".bot:last").empty().append(`Je pense que ça se trouve au ${data["address"]}`);

        // Display the map
        $(".chat-box").append(botMap());
        initMap(data["lat"], data["lng"]);

        // Display a story
        if(data["title"] && data["intro"]){
          $(".chat-box").append(botBox);
          $(".bot:last").append(`
Ce lieu me dit quelque chose ... eh ... ${data["title"]}<br>
C'est bien sûr !!! c'est ${data["intro"]}<br>Voilà, désires-tu autre chose ? 
`);
        }
        else {
          $(".bot:last").append("Je ne connais pas encore ce coin.");
        }
        
      }
      else {
        $(".bot:last").empty().append("Je n'ai pas compris ta question.");
      }
    })
    $(".chat-box").append(botBox);
    $(".bot:last").append(spinner);    
  });
});
