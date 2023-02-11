<script>
	import { Loader } from '@googlemaps/js-api-loader';

    /**
	 * @type {HTMLDivElement}
	 */
    let container;
    let map;
    let zoom = 8;
    let center = { lat: 32.7916841, lng: -96.804615};


    const loader = new Loader({
        apiKey: "",
    });

    const mapOptions = {
        center: center,
        zoom: zoom,
    };

    loader.load().then((google) => {
        new google.maps.Map(container, mapOptions);
    }).catch(e => {
        console.error(e);
    });

</script>

<style>
.full-screen {
    width: 100%;
    height: 100%;
}
</style>

<div class="full-screen" bind:this={container}></div>