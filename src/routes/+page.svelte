<script>
	import { onMount } from 'svelte';
	import Map from './Map.svelte';
	export let ready = false;

	// Write a function that smoothly scrolls to the map on a slight delay after setting ready to true
	function scrollToMap() {
		ready = true;
		setTimeout(() => {
			// @ts-ignore
			document.getElementById('map').scrollIntoView({ behavior: 'smooth' });
		}, 1);
	}

	// Make the body visible after the page loads svelte including the transition
	onMount(() => {
		// @ts-ignore
		document.querySelector('body').style.opacity = 1;
	});

</script>

<main id="main">
	<div id="welcome" class="fullscreen-page">
		<h1>Welcome to our Project</h1>
		<!-- <p>Visit our <a href="https://github.com/hampster2018/WEHack-2023">Github repository</a> to check out more about our project!</p> -->
		<!-- Make a button that says "ready?" and when clicked, set ready to true, as well as call a function that smoothly scrolls to the map -->
		<button id="submit-button" on:click={scrollToMap}>Ready?</button>
	</div>

	{#if ready}
		<div id="map" class="fullscreen-page">
			<Map />
		</div>
	{/if}
</main>

<style>

	:global(body) {
		margin: 0;
		padding: 0;
		overflow-x: hidden;
		opacity: 0;
		transition: 3s;
	}

	/* Make the text in the header more nice */
	h1 {
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 3rem;
		font-weight: 300;
	}

	/* Center the header and paragraph */
	.fullscreen-page {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		width: 99vw;
		text-align: center;
	}

	/* Style the submit button to be minimalistic and nice */
	#submit-button {
		margin-top: 1rem;
		padding: 0.5rem 1rem;
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 1.5rem;
		font-weight: 300;
		border: 1px solid #000;
		border-radius: 0.25rem;
		background-color: #FFF;
		color: #000;
		cursor: pointer;
	}

	#submit-button:hover {
		background-color: #000;
		color: #FFF;
	}

	/* Animate the button when hovering */
	#submit-button:hover {
		transition: 0.3s;
	}


</style>