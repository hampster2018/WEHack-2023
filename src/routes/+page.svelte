<script>
	import { onMount } from 'svelte';
	import Map from './Map.svelte';
	import { API_KEY } from './api_key';
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
		<h1>Welcome to our project!</h1>

		<!-- Make an input field with a transparent default text of "Enter an address, zipcode, city, or state" and hide the placeholder on focus -->
		<form id="zipcode-form" on:submit|preventDefault={scrollToMap}>
			<input id="zipcode-input" type="text" placeholder="Enter a zipcode" />
			<button id="submit-button" >Ready?</button>
		</form>
	</div>

	{#if ready}
		<div id="map" class="fullscreen-page">
			<Map PUBLIC_API_KEY="{API_KEY}" />
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

	#submit-button:hover {
		background-color: #000;
		color: #FFF;
	}

	/* Animate the button when hovering */
	#submit-button:hover {
		transition: 0.3s;
	}

	#zipcode-form {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	/* Style the input field similarly to the submit-button */
	input {
		text-align: center;
		padding: 0.5rem 1rem;
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 1.5rem;
		font-weight: 300;
		background-color: #FFF;
		color: #000;
		border: 1px solid #000;
		border-radius: 0.25rem;
		width: 80%;
	}

	/* Style the submit button to be minimalistic and nice */
	#submit-button {
		border: 1px solid #000;
		border-radius: 0.25rem;
		margin-top: 1rem;
		cursor: pointer;
		padding: 0.5rem 1rem;
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 1.5rem;
		font-weight: 300;
		background-color: #FFF;
		color: #000;
		width: 50%;
	}

</style>