<script>
	import Map from './Map.svelte';
</script>

<main>
	<div id="welcome" class="fullscreen-page">
		<h1>Welcome to our Project</h1>
		<p>Visit <a href="https://github.com/hampster2018/WEHack-2023">our Github repository</a> to check out more about our project!</p>
	</div>

	<div id="map" class="fullscreen-page">
		<Map />
	</div>

</main>

<style>

	/* Remove the margin so the page is full height */
	:global(body) {
		margin: 0;
		padding: 0;
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
		width: 100%;
		text-align: center;
	}

</style>