<script>
    import { onMount } from 'svelte';
    import { Spinner } from 'flowbite-svelte';
    import { houses, selectedHouse } from './storage';

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
        let currentHouse = $houses[$selectedHouse];
        let val = await fetchValue(currentHouse.sqft, currentHouse.acres, currentHouse.parcelValue,
                                    currentHouse.description, currentHouse.city);
        change(val);
        ready = true;
     })

</script>

<main>
    {#if !ready}
    <div>
        <Spinner size={'20'} />
    </div>
    {:else}
        <div id="valueText">The value is ${Number(value).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
    {/if}
</main>

<style>
    #valueText {
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		font-size: 5rem;
		font-weight: 300;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
</style>