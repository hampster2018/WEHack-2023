<script>
	import { onMount } from 'svelte';
	import Map from './Map.svelte';
	import { API_KEY } from './api_key';
	import { mapCenter } from './storage';
	import Saos from "saos";
	export let ready = false;

	
	const CBRE_GREEN = '#538184';
	const DARK_CBRE_GREEN = '#1c293c';
	const WHITE = '#ffffff';

	// Write a function that smoothly scrolls to the map on a slight delay after setting ready to true
	function scrollToMap() {
		ready = true;
		mapCenter.set(geoselect);
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


	const fetchValue = async (/** @type {number} */ sqft, /** @type {number} */ acrage, /** @type {number} */ parcelVal, /** @type {string} */ description, /** @type {string} */ city) => {
    	const url = `http://localhost:5000/${sqft}/${acrage}/${parcelVal}/${description}/${city}`;
    	const res = await fetch(url);
    	const data = await res.json();
    	let value = data['value']
		console.log(value)
	};
	fetchValue(15196, 0.36537, 193080, 'Residential', 'Dallas');


	/**
	 * @type {{ lat: number; lng: number; }}
	 */
	let geoselect;

</script>

<head>
	<meta name="color-scheme" content="light only">
</head>

<main id="main" style="--theme-color-primary: {CBRE_GREEN}; --theme-color-complement: {WHITE}; --theme-color-darker: {DARK_CBRE_GREEN};">
	<div id="welcome" class="fullscreen-page">

		<h1>Welcome to our project!</h1>

		<!-- Make an input field with a transparent default text of "Enter an address, zipcode, city, or state" and hide the placeholder on focus -->
		<form id="zipcode-form" on:submit|preventDefault={scrollToMap}>
			<!-- <input id="zipcode-input" type="text" placeholder="Enter a zipcode" bind:value={geocode} /> -->
			<select bind:value={geoselect} id="zipcode-input" name="places">
				<option value={{lat: 32.76147508980729, lng: -96.78377976258415}} selected>Dallas</option>
				<option value={{lat: 34.07864944413756, lng: -118.13828026065687}}>SoCal</option>
				<option value={{lat: 39.9398775, lng: -75.2141587}}>Philadelphia</option>
			</select>
			<button id="submit-button" >Ready?</button>
		</form>

	</div>

	{#if ready}
		<div id="map" class="fullscreen-page">
			<Map PUBLIC_API_KEY="{API_KEY}" />
		</div>

		<div id="summary" class="fullscreen-page">
			<Saos top={100} once={true} animation={"fade-in 2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both"}>
				<h1>Summary</h1>
			</Saos>

			<div class="summary-section">
				<Saos top={100} once={true} animation={"fade-in 2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both"}>
					<h2>The first, and best result would be worth $2.5 million within 10 years.</h2>
				</Saos>
				<Saos top={100} once={true} animation={"fade-in 2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both"}>
					<h2>The second result would be worth $1.3 million within 10 years.</h2>
				</Saos>
			</div>

		</div>
	{/if}

</main>

<style>

	#summary {
		justify-content: flex-start;
	}

	.summary-section {
		display: flex;
		flex-direction: column;
		/* Align the items on the left of the screen */
		align-items: flex-start;
		/* Make the items take up the full width of the screen */
		width: 95%;
		/* Add padding, 10% on left and right. */
		margin-left: 2.5%;
		margin-right: 2.5%;
	}

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
		color: var(--theme-color-darker);
	}

	h2 {
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 1.5rem;
		font-weight: 300;
		color: var(--theme-color-primary);
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
		background-color: var(--theme-color-complement);
		color: var(--theme-color-primary);
	}

	/* Animate the button when hovering */
	#submit-button:hover {
		transition: 0.3s;
	}

	#zipcode-form {
		display: flex;
		flex-direction: column;
		align-items: center;
		border-color: var(--theme-color-darker);
	}

	/* Style the input field similarly to the submit-button */
	#zipcode-input {
		text-align: center;
		padding: 0.5rem 1rem;
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 1.5rem;
		font-weight: 300;
		background-color: var(--theme-color-complement);
		color: var(--theme-color-primary);
		border: 1px solid var(--theme-color-primary);
		border-radius: 0.25rem;
		width: 100%;
	}

	/* Style the submit button to be minimalistic and nice */
	#submit-button {
		border: 1px solid var(--theme-color-primary);
		border-radius: 0.25rem;
		margin-top: 1rem;
		cursor: pointer;
		padding: 0.5rem 1rem;
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 1.5rem;
		font-weight: 300;
		background-color: var(--theme-color-complement);
		color: var(--theme-color-primary);
		width: 60%;
	}

	@keyframes -global-fade-in {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
	}


</style>