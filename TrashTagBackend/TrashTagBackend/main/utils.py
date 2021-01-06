"""
JSCOde to get Current Latitude & Longitude
navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
    console.log(pos)
});
"""