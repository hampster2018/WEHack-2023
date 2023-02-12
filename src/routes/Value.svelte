<script>
    import { onMount } from 'svelte';

    /**
     * @type {boolean}
    */
   let ready = false

    /**
     * @type {number}
     */
     let value = 8;

     const fetchValue = async (/** @type {number} */ sqft, /** @type {number} */ acrage, /** @type {number} */ parcelVal, /** @type {string} */ description, /** @type {string} */ city) => {
    	const url = `http://localhost:5000/${sqft}/${acrage}/${parcelVal}/${description}/${city}`;
    	const res = await fetch(url);
    	const data = await res.json();
    	let value = data['value']
		console.log(value)
	};

    
     onMount(async () => {
        this.value = await fetchValue(15196, 0.36537, 193080, 'Residential', 'Dallas');
     })

</script>

<main>
    {#if !ready}
    <div>
        
    </div>
    {/if}
</main>