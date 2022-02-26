import * as fs from "fs";
import * as maps from "@googlemaps/google-maps-services-js";

const GOOGLE_MAPS_API_KEY = "AIzaSyDXQH0Gkkp_DyXSU2euFoTjCH6HMDDeLnM";
const merchants = JSON.parse(fs.readFileSync("../input.json"));

/**
 * return the map data for this merchant
 * @param client the `Client` that should be making the maps API requests
 */
async function getMapData(client, merchant) {
    let mapData = {};

    let placeFromTextResponse = await client.findPlaceFromText({
        params: {
            key: GOOGLE_MAPS_API_KEY,
            fields: ["place_id"],
            input: [merchant.address],
            inputtype: "textquery",
        }
    }).catch(console.warn);
    let primaryCandidate = placeFromTextResponse.data.candidates[0];
    let placeId = primaryCandidate["place_id"];

    let placeDetailsResponse = await client.placeDetails({
        params: {
            key: GOOGLE_MAPS_API_KEY,
            place_id: placeId,
            fields: ["ALL"]
        }
    }).catch(console.warn);
    let placeDetails = placeDetailsResponse.data.result;

    for (let key of ["website", "formatted_address", "name"]) {
        mapData[key] = placeDetails[key];
    }
    if (placeDetails.photos) {
        mapData.photos = placeDetails.photos.map(photo => ({
            width: photo.width,
            height: photo.height,
        }));
    }
    else {
        mapData.photos = undefined;
    }

    return JSON.stringify(mapData);
}

const client = new maps.Client();
for (let merchant of merchants.slice(0, 20))
    getMapData(client, merchant).then(data => console.log(JSON.parse(data)));
