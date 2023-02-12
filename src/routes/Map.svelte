<script>
	import { Loader } from '@googlemaps/js-api-loader';
	import { onMount } from 'svelte';
	import { API_KEY } from './api_key';
    import { mapCenter } from './storage';

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
            
            const marker = new google.maps.Marker({
                position: $mapCenter,
                map: map,
                title: "CBRE Main Office!",
            });

            marker.addListener("click", ({ domEvent, latLng }) => {
                const { target } = domEvent;

                console.log(`Click at: ${latLng.lat()}, ${latLng.lng()}`);

                infoWindow.close();
                // @ts-ignore
                infoWindow.setContent(marker.title);
                // @ts-ignore
                infoWindow.open(marker.map, marker);
            });
        }).catch(e => {
            console.error(e);
        });

    });

    mapCenter.subscribe((value) => {
        if(map) {
            map.setCenter(value);
            map.setZoom(8);
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