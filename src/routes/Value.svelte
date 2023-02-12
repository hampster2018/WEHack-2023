<script>
    import { onMount } from 'svelte';
    import { Spinner } from 'flowbite-svelte';

    /**
     * @type {boolean}
    */
   let ready = false

   const change = (/** @type {string} */ val) => {value = val};

    /**
     * @type {string}
     */
     let value;

     const fetchValue = async (/** @type {number} */ sqft, /** @type {number} */ acrage, /** @type {number} */ parcelVal, /** @type {string} */ description, /** @type {string} */ city) => {
    	const url = `http://localhost:5000/${sqft}/${acrage}/${parcelVal}/${description}/${city}`;
    	const res = await fetch(url).then(async (data) => {
            return await data.json()
        }).catch((e) => {
            console.log(e)
        });
        console.log(res['value'])
        return (res['value'])

	};

    
     onMount(async () => {
        let val = await fetchValue(15196, 0.36537, 193080, 'Residential', 'Dallas');
        change(val);
        ready = true;
     })

</script>

<main>
    {#if !ready}
    <div>
        <Spinner />
    </div>
    {:else}
        <div>The value is ${value}</div>
    {/if}
</main>