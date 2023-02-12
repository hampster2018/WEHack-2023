<script>
	import { Loader } from '@googlemaps/js-api-loader';
	import { onMount } from 'svelte';
	import { API_KEY } from './api_key';
    import { mapCenter, houses, selectedHouse } from './storage';

    /**
	 * @type {string}
	 */
     export let PUBLIC_API_KEY;

    /**
	 * @type {HTMLDivElement}
	 */
    let container;

    /**
	 * @type {google.maps.Map<HTMLDivElement>}
	 */
    let map;

    /**
     * @type {number}
     */
    let zoom = 8;

    onMount(async () => {


        const loader = new Loader({
            apiKey: PUBLIC_API_KEY,
        });
        
        var stylesArray = [
            {
                "featureType": "poi.business",
                "stylers": [
                {
                    "visibility": "off"
                }
                ]
            },
            {
                "featureType": "poi.park",
                "elementType": "labels.text",
                "stylers": [
                {
                    "visibility": "off"
                }
                ]
            }
        ]

    const mapOptions = {
        center: $mapCenter,
        zoom: zoom,
        styles: stylesArray,
    };
    
    loader.load().then((google) => {
            // @ts-ignore
            map = new google.maps.Map(container, mapOptions);
            
            const infoWindow = new google.maps.InfoWindow();

            // For every house in houses we want to make a marker and add it to the map
            $houses.forEach((house, index) => {
                const marker = new google.maps.Marker({
                    position: house.coords,
                    map: map,
                    title: `${house.city} Listing`,
                });

                /**
				 * @param {google.maps.Map<HTMLDivElement>} subMap
				 * @param {number} max
				 * @param {number} cnt
				 */
                function smoothZoom (subMap, max, cnt) {
                    if (cnt >= max) {
                        return;
                    }
                    else {
                        const z = google.maps.event.addListener(subMap, 'zoom_changed', function(event){
                            google.maps.event.removeListener(z);
                            smoothZoom(subMap, max, cnt + 1);
                        });
                        setTimeout(function(){subMap.setZoom(cnt)}, 200); 
                    }
                }

                marker.addListener("click", ({ domEvent, latLng }) => {
                    const { target } = domEvent;

                    console.log(`Click on: ${index}`);

                    map.panTo(latLng);

                    setTimeout(() => {
                        smoothZoom(map, 18, map.getZoom());
                        setTimeout(() => {
                            selectedHouse.set(index);
                        }, 4000);
                    }, 200);



                    // infoWindow.close();
                    // @ts-ignore
                    // infoWindow.setContent(`<p>${house.sqft} sqft <br /> ${house.bed} bedroom(s) <br /> ${house.bath} bathroom(s) 
                    //     <br /> ${house.acres} acre(s)</p>`);

                    // @ts-ignore
                    // infoWindow.open(marker.map, marker);
                });
            });

        }).catch(e => {
            console.error(e);
        });

    });

    mapCenter.subscribe((value) => {
        if(map) {
            map.setCenter(value);
            map.setZoom(zoom);
        }
    });

</script>

<style>
    .full-screen {
        width: 100%;
        height: 100%;
    }
</style>

<div class="full-screen" bind:this={container}></div>