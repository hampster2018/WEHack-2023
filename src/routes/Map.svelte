<script>
	import { Loader } from '@googlemaps/js-api-loader';
	import { onMount } from 'svelte';
	import { API_KEY } from './api_key';

    /**
	 * @type {string}
	 */
     export let PUBLIC_API_KEY;

    /**
	 * @type {string}
	 */
     export let geocode;

    /**
	 * @type {HTMLDivElement}
	 */
    let container;

    onMount(async () => {
        const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${geocode}&key=${API_KEY}`;
        const apiData = await fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                return data;
            }).catch(error => {
                console.error(error);
            });

        /**
         * @type {HTMLDivElement}
         */
        let map;
        let zoom = 12;

        let center = { lat: 32.7916841, lng: -96.8004513};
        // @ts-ignore
        if(apiData.results && apiData.results.length > 0) {
            // @ts-ignore
            const { lat, lng } = apiData.results[0].geometry.location;
            center = { lat, lng };
            zoom = 16;
        }



        const loader = new Loader({
            apiKey: PUBLIC_API_KEY,
        });

        const mapOptions = {
            center: center,
            zoom: zoom,
        };

        loader.load().then((google) => {
            // The initMap function alternative

            // @ts-ignore
            const map = new google.maps.Map(container, mapOptions);

            const infoWindow = new google.maps.InfoWindow();

            const marker = new google.maps.Marker({
                position: center,
                map: map,
                title: "CBRE Main Office!",
            });

            marker.addListener("click", ({ domEvent, latLng }) => {
                const { target } = domEvent;

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



</script>

<style>
    .full-screen {
        width: 100%;
        height: 100%;
    }
</style>

<div class="full-screen" bind:this={container}></div>