const COORDS = "coords";

const saveCoords = (coordsObj) => {
  localStorage.setItem(COORDS, JSON.stringify(coordsObj));
};

const handleGeoSucces = (position) => {
  const latitude = position.coord.latitude;
  const longitude = position.coord.longitude;
  const coordsObj = {
    latitude,
    longitude,
  };
  saveCoords(coordsObj);
};

const handleGeoError = () => {
  console.log("Can loaded Geo Locations");
};

const askForCoords = () => {
  navigator.geolocation.getCurrentPosition(handleGeoSucces, handleGeoError);
};

const loadCoords = () => {
  const loadedCoords = localStorage.getItem(COORDS);
  if (loadedCoords == null) {
    askForCoords();
  } else {
  }
};

const initWeather = () => {
  loadCoords();
};

initWeather();
